from __future__ import annotations

from datetime import timedelta
from typing import List, Union, Optional, Any, Dict

from Utilities import Utilities as U
from .WorksheetBase import _WorksheetBase
from ..Exceptions import *
from ..Classes import *
from ..SheetRecord import SheetRecord
################################################################################

__all__ = ("PlumbingWorksheet",)

################################################################################
class PlumbingWorksheet(_WorksheetBase):

    RELEVANT_COLS = "A:K"

    def _parse_record(self, row: List[Dict[str, Any]], row_index: int) -> Optional[SheetRecord]:

        row = row[:11]
        assert len(row) == 11

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

        csr_highlight = row[5].get("effectiveFormat", {}).get("backgroundColorStyle", {}).get("rgbColor")
        if csr_highlight is None:
            csr_highlight = self._parent.theme_colors[row[5]["effectiveFormat"]["backgroundColorStyle"]["themeColor"]]

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
                csr_name=row[5].get("formattedValue", ""),
                last_contact=row[6].get("formattedValue", ""),
                notes=row[7].get("formattedValue", ""),
                date_booked=row[8].get("formattedValue", ""),
                install_date=row[9].get("formattedValue", ""),
                equipment=row[10].get("formattedValue", ""),
                highlight=csr_highlight,
                raw=[x.get("formattedValue", "") for x in row[5:]]
            ),
            highlight=accounting_highlight
        )

################################################################################
    def _raw_data_from_qb(self, qb: QBServiceRecord) -> List[str]:

        return [
            U.account_name_str(qb.account_id, qb.names),
            qb.memo,
            f"${qb.amount:.2f}",
            (qb.date + timedelta(days=365)).strftime("%m/%d/%Y"),
            "", "", "", "", "", "", ""
        ]

################################################################################
    def to_row_data(self, record: SheetRecord) -> Dict[str, List[Dict[str, Any]]]:

        csr_data = [self.empty_value()] * 6
        csr: AnnualCSRData = record._csr_data  # type: ignore

        if record._csr_data is not None:
            csr_data = [
                self.value_with_highlight(
                    value=csr.csr_name,
                    color=csr.highlight
                ),
                self.value_with_highlight(
                    value=csr.last_contact,
                    color=csr.highlight
                ),
                self.value_with_highlight(
                    value=csr.notes,
                    color=csr.highlight
                ),
                self.value_with_highlight(
                    value=csr.date_booked,
                    color=csr.highlight
                ),
                self.value_with_highlight(
                    value=csr.install_date,
                    color=csr.highlight
                ),
                self.value_with_highlight(
                    value=csr.equipment,
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
                # Expiry Date
                self.value_with_highlight(
                    value=record._expiry_date.strftime("%m/%d/%Y") if record._expiry_date else "N/A",
                    color=record._highlight,
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
