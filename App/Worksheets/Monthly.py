from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING, List, Tuple, Union, Optional, Any, Dict

from .WorksheetBase import _WorksheetBase
from ..Classes import *
from ..Exceptions import *
from Utilities import Utilities as U
from ..SheetRecord import SheetRecord

if TYPE_CHECKING:
    pass
################################################################################

__all__ = ("MonthlyWorksheet",)

################################################################################
class MonthlyWorksheet(_WorksheetBase):

    RELEVANT_COLS = "A:J"

    def _parse_record(self, row: List[Dict[str, Any]], row_index: int) -> Optional[SheetRecord]:

        row = row[:10]
        assert len(row) == 10

        if row[0].get("formattedValue") is None:
            self._errors.append(NameMissingError(self.title, row_index))
            return

        result = self.get_account_id_and_names_from_text(row[0]["formattedValue"], row_index)
        if result is None:
            # Error is handled in get_account_id_and_names_from_text
            return

        account_id, names = result

        if row[2].get("formattedValue") is None:
            self._errors.append(NumericParseError(self.title, "{Empty/None}", row_index))
            return

        success, amount = U.make_numeric(row[2]["formattedValue"], default="")
        if not success:
            self._errors.append(NumericParseError(self.title, row[2]["formattedValue"], row_index))
            return

        accounting_highlight = row[0]["effectiveFormat"]["backgroundColorStyle"].get("rgbColor")
        if accounting_highlight is None:
            accounting_highlight = self._parent.theme_colors[row[0]["effectiveFormat"]["backgroundColorStyle"]["themeColor"]]

        csr_highlight = row[4]["effectiveFormat"]["backgroundColorStyle"].get("rgbColor")
        if csr_highlight is None:
            csr_highlight = self._parent.theme_colors[row[4]["effectiveFormat"]["backgroundColorStyle"]["themeColor"]]

        return SheetRecord(
            self,
            row_index,
            raw=[x.get("formattedValue", "") for x in row],
            account_id=account_id,
            names=names,
            memos=[row[1].get("formattedValue", "")],
            amount=amount,
            expiry_date=U.iso_date_from_str(row[3].get("formattedValue", "")),
            csr_data=AnnualCSRData(
                csr_name=row[4].get("formattedValue", ""),
                last_contact=row[5].get("formattedValue", ""),
                notes=row[6].get("formattedValue", ""),
                date_booked=row[7].get("formattedValue", ""),
                install_date=row[8].get("formattedValue", ""),
                equipment=row[9].get("formattedValue", ""),
                highlight=csr_highlight,
                raw=[x.get("formattedValue", "") for x in row[4:]]
            ),
            highlight=accounting_highlight
        )

################################################################################
    def _raw_data_from_qb(self, qb: QBServiceRecord) -> List[str]:

        return [
            U.account_name_str(qb.account_id, qb.names),
            qb.memo,
            f"${qb.amount:.2f}",
            "", "", "", "", "", "", ""
        ]

################################################################################
    def reconcile_record(self, qb: QBServiceRecord, error: bool = True) -> bool:

        if qb.account_id == 177860658:
            # Debug breakpoint
            pass

        print(f"Reconciling QB record {qb} in sheet '{self.title}'")
        # Positive values should simply be added as new records to the end.
        # if qb.amount > 0:
        #     print(f"  Adding new record for positive amount ${qb.amount} from QB.")
        #     self.add_row(qb)
        #     return True

        print(f"  Searching for matching record to reconcile negative amount ${qb.amount} from QB. Account ID: {qb.account_id}")
        # Negative records need to find a matching positive record to reconcile against.
        acct_records = self.get_records_by_account_id(qb.account_id)
        # If there are no records for this account, log an error.
        if not acct_records:
            print(f"    No records found for account ID {qb.account_id} in sheet '{self.title}'")
            if qb.amount > 0:
                print(f"    Adding new record for positive amount ${qb.amount} from QB.")
                self.add_row(qb)
                return True
            else:
                print(f"    Error: No records to reconcile against for negative amount ${qb.amount} from QB.")
                self._errors.append(
                    NoRecordsToReconcileException(
                        sheet_name=self.title,
                        account_id=qb.account_id,
                        qb_record=qb
                    )
                )
                return False

        # If more than one account record exists, we need to combine into a single item.
        if len(acct_records) > 1:
            print(f"    Multiple records found for account ID {qb.account_id} in sheet '{self.title}'. Combining into single record for reconciliation.")

            master_record = acct_records[0]
            for record in acct_records[1:]:
                print(f"      Merging Monthly Record: {record} with Master Record: {master_record}")
                master_record.merge(record)

            acct_records = [master_record]

        assert len(acct_records) == 1, "There should be exactly one record to reconcile against."

        record = acct_records[0]
        record._amount += qb.amount

        print(f"    Updated record after reconciliation: {record}")
        return True

################################################################################
    def to_row_data(self, record: SheetRecord) -> Dict[str, List[Dict[str, Any]]]:

        csr_data = [self.empty_value()] * 6
        csr = record._csr_data

        def get_csr_data_at(c, position: int) -> str:
            match position:
                case 0:
                    if isinstance(c, AnnualCSRData):
                        return c.csr_name
                    elif isinstance(c, MonthlyCSRData):
                        return c.csr_name
                    elif isinstance(c, DuctCleaningCSRData):
                        return c.raw[0]
                case 1:
                    if isinstance(c, AnnualCSRData):
                        return c.last_contact
                    elif isinstance(c, MonthlyCSRData):
                        return c.csr_name
                case 2:
                    if isinstance(c, AnnualCSRData):
                        return c.notes
                    elif isinstance(c, MonthlyCSRData):
                        return c.contact_meths
                case 3:
                    if isinstance(c, AnnualCSRData):
                        return c.date_booked
                    elif isinstance(c, MonthlyCSRData):
                        return c.scheduled_date
                case 4:
                    if isinstance(c, AnnualCSRData):
                        return c.install_date
                    elif isinstance(c, MonthlyCSRData):
                        return c.recognize_as
                case 5:
                    if isinstance(c, AnnualCSRData):
                        return c.equipment
                    elif isinstance(c, MonthlyCSRData):
                        return c.last_service

            return ""

        if record._csr_data is not None:
            csr_data = [
                self.value_with_highlight(
                    value=get_csr_data_at(record._csr_data, 0),
                    color=csr.highlight
                ),
                self.value_with_highlight(
                    value=get_csr_data_at(record._csr_data, 1),
                    color=csr.highlight
                ),
                self.value_with_highlight(
                    value=get_csr_data_at(record._csr_data, 2),
                    color=csr.highlight
                ),
                self.value_with_highlight(
                    value=get_csr_data_at(record._csr_data, 3),
                    color=csr.highlight
                ),
                self.value_with_highlight(
                    value=get_csr_data_at(record._csr_data, 4),
                    color=csr.highlight
                ),
                self.value_with_highlight(
                    value=get_csr_data_at(record._csr_data, 5),
                    color=csr.highlight
                )
            ]

        return {
            "values": [
                # Name
                self.value_with_highlight(
                    value=U.account_name_str(record._account_id, record._names),
                    color=record._highlight
                ),
                # Memo(s)
                self.value_with_highlight(
                    value=";\n".join(record._memos) if record._memos else "",
                    color=record._highlight
                ),
                # Amount
                self.value_with_highlight(
                    value=str(record._amount) if record._amount is not None else "",
                    color=record._highlight,
                    number_fmt="$#,##0.00"
                ),
                # Empty - Purple Highlight
                self.value_with_highlight(
                    value="",
                    color={
                        "red": 0.40392157,
                        "green": 0.30588236,
                        "blue": 0.654902
                    }
                ),
                # CSR Data (if applicable)
                *csr_data
            ]
        }

################################################################################
    def replace_record(self, record: SheetRecord) -> None:

        for i, r in enumerate(self._records):
            if r._id == record._id:
                self._records[i] = record

################################################################################
