from __future__ import annotations
# Don't clean up imports! They're marked as unused but we need them.
import csv
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import TYPE_CHECKING, Optional

from .Classes import *
from GClient.Client import GSheetsClient
from Utilities import Utilities as U
from .Exceptions import *
from .RuleManager import RoutingRuleManager
from .Spreadsheet import Spreadsheet

if TYPE_CHECKING:
    from .Worksheets.WorksheetBase import _WorksheetBase
    from PySide6.QtCore import SignalInstance
################################################################################

__all__ = ("ServiceReconciler", )

################################################################################
class ServiceReconciler:

    __slots__ = (
        "_client",
        "_spreadsheet",
        "_qb",
        "_errors",
        "_rule_mgr",
    )

################################################################################
    def __init__(self, rule_mgr: RoutingRuleManager) -> None:

        self._client: GSheetsClient = GSheetsClient()
        self._spreadsheet: Optional[Spreadsheet] = None
        self._errors: List[ReconcilerException] = []

        self._qb: Dict[date, List[QBServiceRecord]] = defaultdict(list)
        self._rule_mgr: RoutingRuleManager = rule_mgr

################################################################################
    def load_data(self, spreadsheet_id: str, last_run_date: Optional[date]) -> None:

        try:
            meta_payload = self._client.spreadsheet_get(spreadsheet_id)
        except Exception as ex:
            print(f"Error loading spreadsheet metadata: {ex}")
            return

        sheets = meta_payload.get("sheets", [])
        ranges: list[str] = []
        row_counts: Dict[str, int] = {}

        for sheet in sheets:
            props = sheet.get("properties", {})
            title: str | None = props.get("title")
            grid = props.get("gridProperties", {}) or {}
            row_count: int = grid.get("rowCount", 0) or 0
            col_count: int = grid.get("columnCount", 0) or 0

            suffix = last_run_date.strftime("%m-%d-%Y") if last_run_date is not None else ""
            if title not in {
                f"Annual{suffix}",
                f"Monthly{suffix}",
                f"Plumbing - Annual{suffix}",
                f"Generator{suffix}",
                f"Duct Cleaning{suffix}"
            }:
                continue

            row_counts[title] = row_count

            # If we know rows & columns, build a tight range; otherwise fall back to whole sheet
            if row_count > 0 and col_count > 0:
                end_col = U.index_to_column(col_count)
                ranges.append(f"{title}!A1:{end_col}{row_count}")
            else:
                # Just ask for the whole sheet if grid properties are missing
                ranges.append(title)

        # 3) Second request: rich grid data for the computed ranges
        try:
            rich_payload = self._client.spreadsheet_get(
                spreadsheet_id=spreadsheet_id,
                ranges=ranges,
                include_grid_data=True,
            )
        except Exception as ex:
            print(f"Error loading spreadsheet grid data: {ex}")
            # fall back to metadata-only payload if something goes wrong
            rich_payload = meta_payload

        # 4) Build Spreadsheet object from the rich payload
        self._spreadsheet = Spreadsheet(
            client=self._client,
            payload=rich_payload,
            last_run_date=last_run_date
        )
        print(f"Loaded spreadsheet with {len(self._spreadsheet._sheets)} relevant sheets.")

################################################################################
    def load_qb_export(self, csv_addr: Path) -> None:

        assert csv_addr.exists(), f"CSV file not found: {csv_addr}"

        with open(csv_addr, "r", encoding="cp1252") as csv_file:
            reader = csv.DictReader(csv_file)
            for i, row in enumerate(reader):
                parsed = self._parse_qb_record(row, i)
                if parsed is None:
                    continue

                self._qb[parsed.date].append(parsed)

        print(f"Loaded {sum(len(v) for v in self._qb.values())} QB records.")

################################################################################
    def _parse_qb_record(
        self,
        row: Dict[str, str],
        idx: int
    ) -> Optional[QBServiceRecord]:

        name_str = row["Name"]
        split_result = U.split_name_and_account(name_str)
        if split_result is None:
            if self.is_mostly_empty(row):
                return None
            self._errors.append(QBParsingError(
                row,
                idx,
                f"Failed to split name and account ID: '{name_str}'"
            ))
            return None

        account_id, name_without_id = split_result
        member_names = U.split_multi_names(name_without_id)
        _, amount = U.make_numeric(row["Amount"], default=0.0)

        return QBServiceRecord(
            raw=row,
            index=idx,
            account_id=account_id,
            names=[
                MemberName(first=n[0], last=n[1], raw=n[2])
                for n in member_names
            ],
            memo=row["Memo"],
            amount=amount,
            date=U.iso_date_from_str(row["Date"])
        )

################################################################################
    def thresholds_menu(self) -> None:

        while True:
            print(
                "\nInterpretation Thresholds Menu:\n"
                "1. Add Rule\n"
                "2. View/Edit Rule List\n"
                "3. Remove Rule\n"
                "4. Back to Main Menu\n"
            )
            choice = input("Enter your choice: ")

            if choice == "1":
                self._rule_mgr.add_rule()
            elif choice == "2":
                self._rule_mgr.list_edit_rules()
            elif choice == "3":
                self._rule_mgr.remove_rule()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

################################################################################
    def reconcile_all(self, phase_signal: SignalInstance, log_signal: SignalInstance) -> None:

        total_records = sum(len(v) for v in self._qb.values())
        if total_records == 0:
            log_signal.emit("No QB records to reconcile.")
            phase_signal.emit("Reconciling...", 25)
            return

        processed = 0
        last_emitted_bucket = -1

        phase_signal.emit("Reconciling...", 25)
        log_signal.emit(f"Reconciling {total_records} QuickBooks record(s)...")

        def emit_bucket(bucket: int) -> None:
            nonlocal last_emitted_bucket

            if bucket == last_emitted_bucket:
                return
            last_emitted_bucket = bucket

            # Clamp progress of 0...100 to 25...90 for this phase
            mapped = 25 + int(round(bucket * 65 / 100))

            # Now clamp
            if mapped < 25:
                mapped = 25
            elif mapped > 90:
                mapped = 90

            phase_signal.emit("Reconciling...", mapped)
            log_signal.emit(f"Reconciliation progress: {bucket}% ({processed}/{total_records} records processed)")

        for invoice_date in self._qb.keys():
            qb_records = sorted(self._qb[invoice_date], key=lambda r: r.amount)

            for qb in qb_records:
                if qb.account_id == 177860658:
                    # Debug breakpoint
                    pass

                if qb.amount == 0:
                    continue

                target_sheet_name = self._rule_mgr.get_target_sheet(qb)
                assert target_sheet_name is not None

                assert self._spreadsheet is not None
                target_sheet: _WorksheetBase = self._spreadsheet[target_sheet_name]  # type: ignore
                assert target_sheet is not None
                target_sheet.reconcile_record(qb)

                # Calculate progress
                processed += 1
                raw_pct = int((processed / total_records) * 100)
                bucket = (raw_pct // 10) * 10

                emit_bucket(bucket)

        emit_bucket(100)

################################################################################
    def write_to_destination(self, date_str: str) -> None:

        self._spreadsheet.final_batch_update(self, date_str)

################################################################################
    def format_all_errors(self, sheet_id: Optional[int]) -> Dict[str, Any]:

        for sheet in self._spreadsheet._sheets:
            self._errors.extend(sheet._errors)
            sheet._errors.clear()

        self._deduplicate_errors()
        print(len(self._errors), "unique errors found during reconciliation. Writing...")

        if sheet_id:
            request = {
                "appendCells": {
                    "sheetId": sheet_id,
                    "fields": "*",
                    "rows": [e.to_row_data() for e in sorted(self._errors, key=lambda e: e.sort_key())]
                }
            }
            request["appendCells"]["rows"].append({
                "values": [
                    blank_cell(),
                    blank_cell(),
                    fmt_value(
                        value="TOTAL:",
                        align="RIGHT"
                    ),
                    fmt_value(
                        value=f"=SUM(D1:D{len(self._errors)})",
                        align="RIGHT",
                        value_type="Formula",
                        number_fmt_str="$#,##0.00",
                        number_fmt_type="CURRENCY"
                    )
                ]
            })
            return request
        return {}

################################################################################
    def _deduplicate_errors(self) -> None:

        unique_errors: List[ReconcilerException] = []
        for error in self._errors:
            if hasattr(error, "index"):
                qb_row_str = f"QB Row {error.index}"
                for ue in unique_errors:
                    if hasattr(ue, "index"):
                        existing_qb_row_str = f"QB Row {ue.index}"
                        if qb_row_str == existing_qb_row_str:
                            break
                else:
                    unique_errors.append(error)
            else:
                unique_errors.append(error)

        self._errors = list(unique_errors)

################################################################################
    def format_error_for_export(self, error: ReconcilerException) -> List[str]:

        # Location
        # Index
        # Message
        # Raw Data(?)

        if isinstance(error, NameMissingError):
            return [
                f"SOURCE WORKSHEET - {error.source}",
                f"Row: {error.row}",
                error.msg,
                ""
            ]
        if isinstance(error, NameParseError):
            return [
                f"SOURCE WORKSHEET - {error.source}",
                f"Row: {error.row}",
                error.msg,
                error.raw_name
            ]
        if isinstance(error, QBParsingError):
            return [
                "QB EXPORT",
                f"Row: {error.index}",
                error.msg,
                str(error.value)
            ]
        if isinstance(error, UnableToRouteException):
            return [
                "QB EXPORT",
                f"Row: {error.qb.index}",
                error.msg,
                str(error.qb.raw)
            ]
        if isinstance(error, (NoRecordsToReconcileException, NoMatchingRecordException)):
            return [
                f"SOURCE WORKSHEET - {error.sheet_name}",
                f"QB Row: {error.qb_record.index}",
                error.msg,
                str(error.qb_record.raw)
            ]
        if isinstance(error, NumericParseError):
            return [
                f"SOURCE WORKSHEET - {error.sheet_name}",
                f"QB Row: {error.index}",
                error.msg,
                str(error.value)
            ]

        raise NotImplementedError(f"Error formatting not implemented for {type(error)}")

################################################################################
    @staticmethod
    def is_mostly_empty(row: Dict[str, str]) -> bool:

        values = [v for v in row.values() if v.strip() != '']
        return len(values) < 4

################################################################################
def fmt_value(
    value: str,
    align: Literal["LEFT", "CENTER", "RIGHT"] = "CENTER",
    number_fmt_str: Optional[str] = None,
    number_fmt_type: Literal["CURRENCY", "DATE"] = "Currency",
    value_type: Literal["String", "Formula"] = "String",
) -> Dict[str, Any]:

    user_entered_format: Dict[str, Any] = {
        "horizontalAlignment": align,
    }
    if number_fmt_str and number_fmt_type:
        user_entered_format["numberFormat"] = {
            "type": number_fmt_type,
            "pattern": number_fmt_str,
        }

    return {
        "userEnteredValue": {
            f"{value_type.lower()}Value": value
        },
        "userEnteredFormat": user_entered_format
    }

################################################################################
def blank_cell() -> Dict[str, List[Dict[str, Any]]]:

    return fmt_value("")

################################################################################
