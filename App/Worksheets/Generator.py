from __future__ import annotations

from typing import List, Union, Optional, Any, Dict

from Utilities import Utilities as U
from .WorksheetBase import _WorksheetBase
from ..Classes import *
from ..Exceptions import *
from ..SheetRecord import SheetRecord
################################################################################

__all__ = ("GeneratorWorksheet",)

################################################################################
class GeneratorWorksheet(_WorksheetBase):

    RELEVANT_COLS = "A:C"

    def _parse_record(self, row: List[Dict[str, Any]], row_index: int) -> Optional[SheetRecord]:

        row = row[:3]
        assert len(row) == 3

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

        return SheetRecord(
            self,
            row_index,
            raw=[x.get("formattedValue", "") for x in row],
            account_id=account_id,
            names=names,
            memos=[row[1].get("formattedValue", "")],
            amount=amount,
            expiry_date=None,
            csr_data=_CSRDataBase(
                raw=[x.get("formattedValue", "") for x in row[5:]],
                highlight={
                    "red": 1.0,
                    "green": 1.0,
                    "blue": 1.0
                },
            ),
            highlight=accounting_highlight
        )

################################################################################
    def _raw_data_from_qb(self, qb: QBServiceRecord) -> List[str]:

        return [
            U.account_name_str(qb.account_id, qb.names),
            qb.memo,
            f"${qb.amount:.2f}"
        ]

################################################################################
    def to_row_data(self, record: SheetRecord) -> Dict[str, List[Dict[str, Any]]]:

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
            ]
        }

################################################################################

