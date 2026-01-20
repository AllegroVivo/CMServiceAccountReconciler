from __future__ import annotations

import re
from abc import ABC, abstractmethod
from datetime import timedelta, datetime
from typing import Optional, Mapping, Tuple

from Utilities import Utilities as U
from ..Exceptions import *
from ..SheetRecord import SheetRecord
from App.Classes import MemberName

if TYPE_CHECKING:
    from GClient.Client import GSheetsClient
    from App.Spreadsheet import Spreadsheet
    from App.Classes import ServiceAccountRecord
################################################################################

__all__ = ("_WorksheetBase", )

_DATE_SUFFIX_RE = re.compile(r"(?:\s*-\s*\d{2}-\d{2}-\d{4})+\s*$")

################################################################################
class _WorksheetBase(ABC):

    __slots__ = (
        "_client",
        "_parent",
        "_raw",
        "_data",
        "_records",
        "_errors",
        "_reconciled",
    )

    RELEVANT_COLS: str = None  # type: ignore

################################################################################
    def __init__(self, client: GSheetsClient, parent: Spreadsheet, payload: Dict[str, Any]) -> None:

        assert self.RELEVANT_COLS is not None, "RELEVANT_COLS must be defined in subclass"

        self._client: GSheetsClient = client
        self._parent: Spreadsheet = parent
        self._raw: Dict[str, Any] = payload.copy()
        self._data: Dict[str, Any] = payload["data"][0]
        self._errors: List[ReconcilerException] = []
        self._reconciled: List[SheetRecord] = []

        self._records: List[SheetRecord] = []
        self._parse_row_data()

################################################################################
    @property
    def id(self) -> int:

        return self.properties["sheetId"]

################################################################################
    @property
    def rich_data(self) -> Mapping[str, Any]:

        return self._data

################################################################################
    @property
    def row_data(self) -> List[Mapping[str, Any]]:

        return self._data["rowData"]

################################################################################
    @property
    def properties(self) -> Mapping[str, Any]:

        return self._raw["properties"]

################################################################################
    @property
    def title(self) -> str:

        return self.properties["title"]

################################################################################
    def with_date_string(self, date_str: str) -> str:

        return f"{self.title} - {date_str}"

################################################################################
    def column_sizes(self) -> Dict[int, int]:

        return {
            i: x["pixelSize"]
            for i, x
            in enumerate(self._data["columnMetadata"])
        }

################################################################################
    @property
    def max_row(self) -> int:
        """Returns the last row index that contains data."""

        return next(
            # This is the first empty row, so subtract 1 for last row with data.
            (record._row - 1 for record in self._records if record.is_empty()),
            len(self._records)
        )

################################################################################
    def next_row(self) -> int:
        """Returns the next available row index for new data."""

        return self.max_row + 1

################################################################################
    @property
    def relevant_col_start(self) -> str:

        return self.RELEVANT_COLS.split(":")[0]

################################################################################
    @property
    def relevant_col_end(self) -> str:

        return self.RELEVANT_COLS.split(":")[1]

################################################################################
    @abstractmethod
    def _parse_record(self, row: List[Dict[str, Any]], row_index: int) -> Optional[SheetRecord]:

        pass

################################################################################
    @abstractmethod
    def _raw_data_from_qb(self, qb: QBServiceRecord) -> List[str]:

        pass

################################################################################
    @abstractmethod
    def to_row_data(self, record: SheetRecord) -> Dict[str, List[Dict[str, Any]]]:

        pass

################################################################################
    def base_title(self) -> str:

        return _DATE_SUFFIX_RE.sub("", self.title).strip()

################################################################################
    def create_new_sheet_request(self, date_str: str) -> Dict[str, Any]:

        return {
            "addSheet": {
                "properties": {
                    "title": f"{self.base_title()} - {date_str}",
                }
            }
        }

################################################################################
    def append_cells_payload(self, sheet_id: int):

        sorted_records = sorted(self._records, key=lambda r: (
            r._expiry_date is not None,
            r._expiry_date or datetime.min,
            r._row
        ))

        ret = {
            "appendCells": {
                "sheetId": sheet_id,
                "fields": "*",
                "rows": [r.to_row_data() for r in sorted_records]
            }
        }

        return ret

################################################################################
    def new_id(self) -> int:

        return self._parent.new_id()

################################################################################
    def _parse_row_data(self) -> None:

        for i, row in enumerate(self.row_data, start=1):
            values = row.get("values", [])
            if not values:
                continue  # Skip empty rows
            if values[1].get("formattedValue") == "Membership Type":
                continue  # Skip header row

            values = self._pad_row(values, 12)
            result = self._parse_record(values, i)
            if result is None:
                continue

            assert isinstance(result, SheetRecord), "Parsed record must be a SheetRecord"
            self._records.append(result)

################################################################################
    def get_account_id_and_names_from_text(
        self,
        raw_name: str,
        row_index: int
    ) -> Optional[Tuple[Optional[int], List[MemberName]]]:

        # First cell is account name and ID
        raw_name = raw_name.strip() if len(raw_name) > 0 else None
        # If missing, log error and skip
        if not raw_name:
            self._errors.append(NameMissingError(self.title, row_index))
            return

        # Extract name and ID from cell data
        split_result = U.split_name_and_account(raw_name)
        if split_result is None:
            self._errors.append(NameParseError(self.title, raw_name, row_index))
            return

        account_id, name_without_id = split_result

        U.split_multi_names(name_without_id)
        names = [
            MemberName(first=n[0], last=n[1], raw=n[2])
            for n in U.split_multi_names(name_without_id)
        ]

        return account_id, names

################################################################################
    def reconcile_record(self, qb: QBServiceRecord) -> bool:

        # For most sheets, positive values should simply be added as new records
        # to the end. Done and done.
        if qb.amount > 0:
            self.add_row(qb)
            return True

        # Negative records need to find a matching positive record to reconcile against.
        acct_records = self.get_records_by_account_id(qb.account_id)
        # If there are no records for this account, log an error.
        if not acct_records:
            monthly_worksheet = self._parent["Monthly"]
            assert monthly_worksheet is not None
            success = monthly_worksheet.reconcile_record(qb)
            if not success:
                print(f"    No records found for account ID {qb.account_id} in sheet '{self.title}'")
                self._errors.append(
                    NoRecordsToReconcileException(
                        sheet_name=self.title,
                        account_id=qb.account_id,
                        qb_record=qb
                    )
                )
            return success

        # Search through records for a matching amount to reconcile.
        for record in acct_records:
            if not record._amount:
                continue

            if 0 < record._amount == abs(qb.amount):
                print(f"    Reconciling QB record {qb} with sheet record {record} in sheet '{self.title}'")
                record.delete()
                return True

        print(f"    No matching record found for account ID {qb.account_id} and amount ${abs(qb.amount)} in sheet '{self.title}'")
        # If we get here, no matching record was found. Log an error.
        self._errors.append(
            NoMatchingRecordException(
                sheet_name=self.title,
                account_id=qb.account_id,
                qb_record=qb
            )
        )
        return False

################################################################################
    def _add_reconciled(self, record: SheetRecord) -> None:

        self._reconciled.append(record)

################################################################################
    def add_row(self, qb: QBServiceRecord) -> None:

        record = SheetRecord(
            parent=self,
            index=self.next_row(),
            raw=self._raw_data_from_qb(qb),
            account_id=qb.account_id,
            # Copy names so we don't have references to the same objects
            names=[MemberName(first=n.first, last=n.last, raw=n.raw) for n in qb.names],
            memos=[qb.memo],
            amount=qb.amount,
            expiry_date=qb.date + timedelta(days=365)
        )
        self._records.append(record)

################################################################################
    def get_records_by_account_id(self, account_id: Optional[int]) -> List[SheetRecord]:

        if not account_id:
            return []

        temp = [r for r in self._records if r._account_id == account_id]
        return sorted(
            temp,
            key=lambda r: r._row
        )

################################################################################
    @staticmethod
    def value_with_highlight(
        value: str,
        color: Optional[Dict[str, float]],
        number_fmt: Optional[str] = None
    ) -> Dict[str, Any]:

        user_entered_format: Dict[str, Any] = {
            "backgroundColorStyle": {
                "rgbColor": color or {
                    "red": 1.0,
                    "green": 1.0,
                    "blue": 1.0,
                }
            }
        }

        if number_fmt is not None:
            user_entered_format["numberFormat"] = {
                "type": "NUMBER",
                "pattern": number_fmt,
            }

        user_entered_value: Dict[str, Any] = {}
        if number_fmt is not None:
            user_entered_value["number_value"] = value
        else:
            user_entered_value["stringValue"] = value

        return {
            "userEnteredValue": user_entered_value,
            "userEnteredFormat": user_entered_format,
        }

################################################################################
    @staticmethod
    def empty_value() -> Dict[str, Any]:

        return {
            "userEnteredValue": {}
        }

################################################################################
    def column_sizing_requests(self, new_sheet_id: int) -> List[Dict[str, Any]]:
        """
        Turns per-column pixel sizes into minimal updateDimensionProperties requests
        by grouping contiguous columns of the same size.
        """
        if not self.column_sizes():
            return []

        cols = sorted(self.column_sizes().keys())
        requests: List[Dict[str, Any]] = []

        run_start = cols[0]
        run_size = self.column_sizes()[run_start]
        prev = run_start

        def flush(end_exclusive) -> None:
            requests.append({
                "updateDimensionProperties": {
                    "range": {
                        "sheetId": new_sheet_id,
                        "dimension": "COLUMNS",
                        "startIndex": run_start,
                        "endIndex": end_exclusive,
                    },
                    "properties": {"pixelSize": run_size},
                    "fields": "pixelSize",
                }
            })

        for c in cols[1:]:
            size = self.column_sizes()[c]
            if c == prev + 1 and size == run_size:
                prev = c
                continue

            flush(prev + 1)
            run_start = c
            run_size = size
            prev = c

        flush(prev + 1)
        return requests

################################################################################
    # noinspection PyListCreation
    def justification_requests(self, sheet_id: int) -> List[Dict[str, Any]]:

        ret: List[Dict[str, Any]] = []

        # A:B left (exists for all sheets)
        ret.append(self._repeat_alignment(
            sheet_id=sheet_id,
            start_row=0,
            end_row=self.max_row,
            start_col=0,  # A
            end_col=2,  # C (exclusive) -> A,B
            alignment="LEFT",
        ))

        # C right (exists for Annual + Monthly; Generator stops at C but C still exists)
        ret.append(self._repeat_alignment(
            sheet_id=sheet_id,
            start_row=0,
            end_row=self.max_row,
            start_col=2,  # C
            end_col=3,  # D (exclusive) -> C
            alignment="RIGHT",
        ))

        sheet_name = self.title.strip().lower()

        # D left (Annual only; Monthly doesn't have D; Generator doesn't have D)
        if sheet_name.startswith("annual") or sheet_name.startswith("plumbing"):
            ret.append(self._repeat_alignment(
                sheet_id=sheet_id,
                start_row=0,
                end_row=self.max_row,
                start_col=3,  # D
                end_col=4,  # E (exclusive) -> D
                alignment="LEFT",
            ))

            # E:K centered (Annual only)
            ret.append(self._repeat_alignment(
                sheet_id=sheet_id,
                start_row=0,
                end_row=self.max_row,
                start_col=4,  # E
                end_col=11,  # K (exclusive)
                alignment="CENTER",
            ))

        if sheet_name.startswith("monthly"):
            ret.append(self._repeat_alignment(
                sheet_id=sheet_id,
                start_row=0,
                end_row=self.max_row,
                start_col=4,
                end_col=11,
                alignment="CENTER"
            ))

        return ret

################################################################################
    @staticmethod
    def _repeat_alignment(
        *,
        sheet_id: int,
        start_row: int,
        end_row: int,
        start_col: int,
        end_col: int,
        alignment: str,
    ) -> Dict[str, Any]:
        return {
            "repeatCell": {
                "range": {
                    "sheetId": sheet_id,
                    "startRowIndex": start_row,
                    "endRowIndex": end_row,
                    "startColumnIndex": start_col,
                    "endColumnIndex": end_col,
                },
                "cell": {"userEnteredFormat": {"horizontalAlignment": alignment}},
                "fields": "userEnteredFormat.horizontalAlignment",
            }
        }

################################################################################
    def trim_requests(
        self,
        sheet_id: int,
        trim_rows: bool,
        *,
        row_count: int,
        record_count: int,
        column_count: int
    ) -> List[Dict[str, Any]]:

        ret = [
            {
                "deleteDimension": {
                    "range": {
                        "sheetId": sheet_id,
                        "dimension": "COLUMNS",
                        "startIndex": U.column_to_index(self.relevant_col_end),
                        "endIndex": column_count - 1,
                    }
                }
            }
        ]
        if trim_rows:
            ret.append({
                "deleteDimension": {
                    "range": {
                        "sheetId": sheet_id,
                        "dimension": "ROWS",
                        "startIndex": record_count + 1,
                        "endIndex": row_count - 1,
                    }
                }
            })

        return ret

################################################################################
    @staticmethod
    def _pad_row(row: List[Mapping[str, Any]], pad_to: int) -> List[Mapping[str, Any]]:

        if len(row) < pad_to:
            num_addl = pad_to - len(row)
            row.extend([{
                "horizontalAlignment": "LEFT",
                "wrapStrategy": "WRAP",
                "effectiveFormat": {
                    "backgroundColorStyle": {
                        "rgbColor": {
                            "red": 1.0,
                            "green": 1.0,
                            "blue": 1.0,
                        }
                    }
                }
            }] * num_addl)

        return row

################################################################################
