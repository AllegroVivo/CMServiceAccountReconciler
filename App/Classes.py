from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional, Dict, Type
################################################################################

__all__ = (
    "MemberName",
    "ServiceAccountRecord",
    "_CSRDataBase",
    "AnnualCSRData",
    "MonthlyCSRData",
    "DuctCleaningCSRData",
    "Coordinate",
    "QBServiceRecord",
    "SheetRoutingRuleWrite",
    "SheetRoutingRuleRead",
    "ApplicationState",
)

################################################################################
@dataclass
class Identifiable:

    id: int

################################################################################
@dataclass
class MemberName:

    first: str
    last: Optional[str]
    raw: str

    def __eq__(self, other) -> bool:
        return self.first == other.first and self.last == other.last

    def __str__(self) -> str:
        if self.last:
            return f"{self.first} {self.last}"
        return self.first

################################################################################
@dataclass
class ServiceAccountRecord:

    memo: str
    amount_paid: float
    exp_date: Optional[date]
    csr_data: _CSRDataBase
    location: Coordinate
    highlight: Dict[str, float] = field(default_factory=dict)
    _remove_flag: bool = False

    @classmethod
    def from_qb[SAR](cls: Type[SAR], qb: QBServiceRecord, sheet: str, row: int) -> SAR:
        return cls(
            memo=qb.memo,
            amount_paid=qb.amount,
            exp_date=qb.date,
            csr_data=(
                MonthlyCSRData()
                if sheet == "Monthly"
                else AnnualCSRData()
            ),
            location=Coordinate(
                sheet=sheet,
                row=row,
                column=0
            )
        )

################################################################################
@dataclass
class _CSRDataBase:

    raw: List[str] = field(default_factory=list)
    highlight: Dict[str, float] = field(default_factory=dict)

    def to_values_array(self) -> List[str]:
        return []

################################################################################
@dataclass
class _CSRBaseWithAttrs(_CSRDataBase):

    csr_name: Optional[str] = None
    last_contact: Optional[str] = None

    def to_values_array(self) -> List[str]:
        return [
            # CSR Name
            self.csr_name or "",
            # Last Contact
            self.last_contact or "",
        ]

################################################################################
@dataclass
class AnnualCSRData(_CSRBaseWithAttrs):

    notes: Optional[str] = None
    date_booked: Optional[str] = None
    install_date: Optional[str] = None
    equipment: Optional[str] = None

    def to_values_array(self) -> List[str]:
        return [
            *(super().to_values_array()),
            # Notes
            self.notes or "",
            # Date Booked
            self.date_booked or "",
            # Install Date
            self.install_date or "",
            # Equipment
            self.equipment or "",
        ]

################################################################################
@dataclass
class MonthlyCSRData(_CSRBaseWithAttrs):

    contact_meths: Optional[str] = None
    scheduled_date: Optional[str] = None
    recognize_as: Optional[str] = None
    last_service: Optional[str] = None

    def to_values_array(self) -> List[str]:
        return [
            *(super().to_values_array()),
            # Contact Methods
            self.contact_meths or "",
            # Date Scheduled
            self.scheduled_date or "",
            # Recognize As
            self.recognize_as or "",
            # Last Service
            self.last_service or "",
        ]

################################################################################
@dataclass
class DuctCleaningCSRData(_CSRDataBase):

    def to_values_array(self) -> List[str]:
        return [self.raw[0]]

################################################################################
@dataclass
class Coordinate:

    sheet: str
    row: int
    column: int

    def __eq__(self, other: Coordinate) -> bool:
        return (
            self.sheet == other.sheet and
            self.row == other.row and
            self.column == other.column
        )

    def __str__(self) -> str:
        return f"{self.sheet}(Row: {self.row}, Col: {self.column})"

################################################################################
@dataclass
class QBServiceRecord:

    raw: Dict[str, str]
    index: int
    account_id: int
    names: List[MemberName]
    memo: str
    amount: float
    date: date

    def __str__(self) -> str:
        names_str = ", ".join(str(name) for name in self.names)
        return f"QBServiceRecord(Index: {self.index}, Account ID: {self.account_id}, Names: [{names_str}], Memo: {self.memo}, Amount: {self.amount}, Date: {self.date})"

################################################################################
@dataclass
class SheetRoutingRuleWrite:

    name: str
    sheet: str
    min_amount: Optional[float]
    max_amount: Optional[float]
    priority: int = 100

################################################################################
@dataclass
class SheetRoutingRuleRead(SheetRoutingRuleWrite, Identifiable):

    dirty: bool = False

    def matches(self, record: QBServiceRecord) -> bool:
        _min = self.min_amount or float("-inf")
        _max = self.max_amount or float("inf")
        return _min <= abs(record.amount) <= _max

################################################################################
@dataclass
class ApplicationState:

    spreadsheet_id: str
    last_run_date: Optional[date] = None
    id: int = -1

################################################################################
