from __future__ import annotations

from abc import abstractmethod
from datetime import date
from typing import TYPE_CHECKING, List, Optional, Any, Literal

from Utilities.Enums import HighlightColor
from .Classes import *
from Utilities import Utilities as U
from .Exceptions import *

if TYPE_CHECKING:
    from .Worksheets.WorksheetBase import _WorksheetBase
################################################################################

__all__ = ("SheetRecord", )

LINE_SEP = ";\n"

################################################################################
class SheetRecord:

    __slots__ = (
        "_id",
        "_sheet",
        "_row",
        "_raw",
        "_account_id",
        "_names",
        "_memos",
        "_amount",
        "_expiry_date",
        "_csr_data",
        "_highlight",
        "_reconciled_record",
    )

################################################################################
    def __init__(self, parent: _WorksheetBase, index: int, raw: List[str], **kwargs) -> None:

        self._id: int = parent.new_id()
        self._sheet: _WorksheetBase = parent
        self._raw: List[str] = raw.copy()
        self._row: int = index

        self._account_id: int = kwargs.get("account_id")
        self._names: List[MemberName] = kwargs.get("names", [])
        self._memos: List[str] = kwargs.get("memos", [])
        self._amount: float = kwargs.get("amount")
        self._expiry_date: Optional[date] = kwargs.get("expiry_date")
        self._csr_data: Optional[_CSRDataBase] = kwargs.get("csr_data")
        self._highlight: Optional[HighlightColor] = kwargs.get("highlight")

        self._reconciled_record: Optional[QBServiceRecord] = None

################################################################################
    def __eq__(self, other: SheetRecord) -> bool:

        return self._id == other._id

################################################################################
    def is_empty(self) -> bool:

        return all(value is None or value == "" for value in self._raw)

################################################################################
    def delete(self) -> None:

        for i, record in enumerate(self._sheet._records):
            if record == self:
                self._sheet._records.pop(i)
                break

        # TODO: Shift indexes of remaining records up by 1

################################################################################
    def to_values_array(self, sheet: str) -> List[str]:

        if sheet == "Annual":
            return self._values_array_annual()
        elif sheet == "Monthly":
            return self._values_array_monthly()
        elif sheet == "Plumbing - Annual":
            return self._values_array_plumbing()
        elif sheet == "Generator":
            return self._values_array_generator()
        elif sheet == "Duct Cleaning":
            return self._values_array_duct_cleaning()
        else:
            raise ValueError(f"Unsupported sheet type: {sheet}")

################################################################################
    def _values_array_annual(self) -> List[str]:
        return [
            # Column A - Names and Account Number
            U.account_name_str(self._account_id, self._names),
            # Column B - Memo
            ";\n".join(self._memos) if self._memos else "",
            # Column C - Amount
            str(self._amount) if self._amount is not None else "",
            # Column D - Expiry Date
            self._expiry_date.strftime("%m/%d/%Y") if self._expiry_date else "N/A",
            # Column E - Empty
            "",
            # Columns F through K - CSR Data (if applicable)
            *(
                self._csr_data.to_values_array()
                if self._csr_data is not None
                else ""
            )
        ]

################################################################################
    def _values_array_monthly(self) -> List[str]:
        return [
            # Column A - Names and Account Number
            U.account_name_str(self._account_id, self._names),
            # Column B - Memo
            ";\n".join(self._memos) if self._memos else "",
            # Column C - Amount
            str(self._amount) if self._amount is not None else "",
            # Column D - Empty
            "",
            # Columns E through J - CSR Data (if applicable)
            *(
                self._csr_data.to_values_array()
                if self._csr_data is not None
                else ""
            )
        ]

################################################################################
    def _values_array_plumbing(self) -> List[str]:
        return [
            # Column A - Names and Account Number
            U.account_name_str(self._account_id, self._names),
            # Column B - Memo
            ";\n".join(self._memos) if self._memos else "",
            # Column C - Amount
            str(self._amount) if self._amount is not None else "",
            # Column D - Expiry Date
            self._expiry_date.strftime("%m/%d/%Y") if self._expiry_date else "N/A",
            # Columns E through K - Empty CSR Data
            "", "", "", "", "", "", ""
        ]

################################################################################
    def _values_array_generator(self) -> List[str]:
        return [
            # Column A - Names and Account Number
            U.account_name_str(self._account_id, self._names),
            # Column B - Memo
            ";\n".join(self._memos) if self._memos else "",
            # Column C - Amount
            str(self._amount) if self._amount is not None else "",
            # Columns D through K - Empty CSR Data
            "", "", "", "", "", "", "", ""
        ]

################################################################################
    def _values_array_duct_cleaning(self) -> List[str]:
        return [
            # Column A - Names and Account Number
            U.account_name_str(self._account_id, self._names),
            # Column B - Memo
            ";\n".join(self._memos) if self._memos else "",
            # Column C - Amount
            str(self._amount) if self._amount is not None else "",
            # Column D - CSR Data Shitshow
            self._csr_data.raw[0] if self._csr_data is not None else ""
        ]

################################################################################
    def merge(self, other: SheetRecord) -> SheetRecord:

        assert self._account_id == other._account_id

        for name in other._names:
            if name not in self._names:
                self._names.append(name)

        for memo in other._memos:
            if memo not in self._memos:
                self._memos.append(memo)

        if self._amount is None:
            self._amount = 0
        if other._amount is not None:
            self._amount += other._amount

        def merge_csr_text(left: str, right: str, sep: str = LINE_SEP) -> str:
            left = (left or "").strip()
            right = (right or "").strip()

            if not right:
                return left
            if not left:
                return right
            return f"{left}{sep}{right}"

        if isinstance(self._csr_data, MonthlyCSRData):
            field_set = {
                "csr_name",
                "last_contact",
                "contact_meths",
                "scheduled_date",
                "recognize_as",
                "last_service"
            }
            csr_data_type = MonthlyCSRData
        elif isinstance(self._csr_data, DuctCleaningCSRData):
            field_set = {
                "raw",
            }
            csr_data_type = DuctCleaningCSRData
        else:
            field_set = {
                "csr_name",
                "last_contact",
                "contact_meths",
                "scheduled_date",
                "recognize_as",
                "last_service",
            }
            csr_data_type = AnnualCSRData

        # Create a copy (replace is nice with dataclasses; or just assign attrs)
        merged = self._csr_data or csr_data_type()
        for field_name in field_set:
            merged_val = merge_csr_text(
                getattr(merged, field_name, ""),
                getattr(other._csr_data, field_name, ""),
            )
            setattr(merged, field_name, merged_val)

        self._csr_data = merged

        # Remove the other record from the document
        other.delete()

        return self

################################################################################
    def to_row_data(self) -> Dict[str, Any]:

        return self._sheet.to_row_data(self)

################################################################################
