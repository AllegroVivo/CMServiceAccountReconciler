from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Any

if TYPE_CHECKING:
    from .Classes import *
    from .SheetRecord import SheetRecord
################################################################################
class ReconcilerException(Exception):
    # In case we want to add common functionality later
    def __init__(self, msg: str):
        self.msg = msg
        super().__init__(msg)

################################################################################
class NameMissingError(ReconcilerException):

    def __init__(self, source: str, row: int) -> None:

        self.source: str = source
        self.row: int = row
        super().__init__(f"NameMissingError in '{source}' at row {row}: Name field is missing or empty.")

################################################################################
class NameParseError(ReconcilerException):

    def __init__(self, source: str, raw_name: str, row: int) -> None:

        self.source: str = source
        self.raw_name: str = raw_name
        self.row: int = row

        super().__init__(f"NameParseError in '{source}' at row {row}: Failed to parse name from '{raw_name}'.")

################################################################################
class QBParsingError(ReconcilerException):

    def __init__(self, value: Dict[str, str], index: int, msg: str) -> None:

        self.value: Dict[str, str] = value
        self.index: int = index
        super().__init__(f"QBParsingError -- invalid record '{value}'. {msg}")

################################################################################
class UnableToRouteException(ReconcilerException):

    def __init__(self, qb: QBServiceRecord) -> None:

        self.qb: QBServiceRecord = qb

        super().__init__(
            f"UnableToRouteException: Unable to route QB Record '{qb.raw['Name']}' "
            f"with account ID {qb.account_id} to a sheet. Check to see if a Routing "
            f"Rule exists for the applicable amount range."
        )

################################################################################
class NoRecordsToReconcileException(ReconcilerException):

    def __init__(self, sheet_name: str, account_id: int, qb_record: QBServiceRecord) -> None:

        self.sheet_name: str = sheet_name
        self.account_id: int = account_id
        self.qb_record: QBServiceRecord = qb_record

        super().__init__(
            f"NoRecordsToReconcileException in sheet '{sheet_name}': "
            f"No existing records found for account ID {account_id} "
            f"to reconcile QB Record '{qb_record.raw['Name']}' from row "
            f"{qb_record.index}."
        )

################################################################################
class NoMatchingRecordException(ReconcilerException):

    def __init__(self, sheet_name: str, account_id: int, qb_record: QBServiceRecord) -> None:

        self.sheet_name: str = sheet_name
        self.account_id: int = account_id
        self.qb_record: QBServiceRecord = qb_record

        super().__init__(
            f"NoMatchingRecordException in sheet '{sheet_name}': "
            f"No matching record found for account ID {account_id} "
            f"to reconcile QB Record '{qb_record.raw['Name']}' from row "
            f"{qb_record.index}."
        )

################################################################################
class NumericParseError(ReconcilerException):

    def __init__(self, sheet_name: str, value: str, index: int) -> None:

        self.sheet_name: str = sheet_name
        self.value: str = value
        self.index: int = index
        super().__init__(
            f"NumericParseError -- invalid numeric value '{value}' at row "
            f"{index} in sheet {sheet_name}."
        )

################################################################################
