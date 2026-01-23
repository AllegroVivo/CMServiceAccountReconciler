from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Any, Literal, Optional

if TYPE_CHECKING:
    from .Classes import *
################################################################################
class ReconcilerException(Exception):
    # In case we want to add common functionality later
    def __init__(self, msg: str):
        self.msg = msg
        super().__init__(msg)

    def __eq__(self, other: ReconcilerException) -> bool:
        return self.msg == other.msg

    def to_row_data(self) -> Dict[str, List[Dict[str, Any]]]:
        raise NotImplementedError("Subclasses must implement to_row_data method.")

    def sort_key(self) -> Any:
        raise NotImplementedError("Subclasses must implement sort_key method.")

################################################################################
class NameMissingError(ReconcilerException):

    def __init__(self, source: str, row: int) -> None:

        self.source: str = source
        self.row: int = row
        super().__init__(f"NameMissingError in '{source}' at row {row}: Name field is missing or empty.")

    def to_row_data(self) -> Dict[str, List[Dict[str, Any]]]:
        return {
            "values": [
                fmt_value(
                    value=f"Row {self.row} in {self.source}",
                ),
                blank_cell(),
                fmt_value(
                    value="Name Missing - There was no name in the 'Name' column for this row. Unable to identify.",
                ),
            ]
        }

    def sort_key(self) -> Any:
        return 0, self.source, self.row

################################################################################
class NameParseError(ReconcilerException):

    def __init__(self, source: str, raw_name: str, row: int) -> None:

        self.source: str = source
        self.raw_name: str = raw_name
        self.row: int = row

        super().__init__(f"NameParseError in '{source}' at row {row}: Failed to parse name from '{raw_name}'.")

    def to_row_data(self) -> Dict[str, List[Dict[str, Any]]]:
        return {
            "values": [
                fmt_value(
                    value=f"Row {self.row} in {self.source}: '{self.raw_name}'",
                ),
                blank_cell(),
                fmt_value(
                    value=(
                        "Name Parse Error - Unable to parse a valid <name> "
                        "<account number> combination from the 'Name' column. "
                        "Unable to identify."
                    ),
                    align="LEFT"
                ),
            ]
        }

    def sort_key(self) -> Any:
        return 1, self.source, self.row

################################################################################
class QBParsingError(ReconcilerException):

    def __init__(self, value: Dict[str, str], index: int, msg: str) -> None:

        self.value: Dict[str, str] = value
        self.index: int = index
        self.date: str = value["Date"]
        super().__init__(f"QBParsingError -- invalid record '{value}'. {msg}")

    def to_row_data(self) -> Dict[str, List[Dict[str, Any]]]:
        return {
            "values": [
                fmt_value(
                    value=f"QB Row {self.index}",
                ),
                fmt_value(
                    value=f"{self.value.get('Name', '???')}",
                    align="LEFT"
                ),
                fmt_value(
                    value=(
                        "QB Name Parse Error - Unable to parse a valid <name> "
                        "<account number> combination from the QuickBooks record "
                        "'Name' field. Unable to identify."
                    ),
                    align="LEFT"
                ),
                fmt_value(
                    value=f"{self.value.get('Amount', '???')}",
                    number_fmt_str="$#,##0.00",
                    number_fmt_type="CURRENCY",
                    align="RIGHT",
                    value_type="Number"
                ),
                fmt_value(
                    value=f"{self.date}",
                    number_fmt_str="MM-DD-YYYY",
                    number_fmt_type="DATE",
                    align="LEFT"
                )
            ]
        }

    def sort_key(self) -> Any:
        return 2, self.index

################################################################################
class UnableToRouteException(ReconcilerException):

    def __init__(self, qb: QBServiceRecord) -> None:

        self.qb: QBServiceRecord = qb
        self.index: int = qb.index
        self.date: str = qb.date.strftime("%m-%d-%Y")

        super().__init__(
            f"UnableToRouteException: Unable to route QB Record '{qb.raw['Name']}' "
            f"with account ID {qb.account_id} to a sheet. Check to see if a Routing "
            f"Rule exists for the applicable amount range."
        )

    def to_row_data(self) -> Dict[str, List[Dict[str, Any]]]:
        return {
            "values": [
                fmt_value(
                    value=f"QB Row {self.index}",
                ),
                fmt_value(
                    value=f"{self.qb.raw.get('Name', '???')}",
                    align="LEFT"
                ),
                fmt_value(
                    value="Unable to Route Transaction - This is unused?",
                    align="LEFT"
                ),
                fmt_value(
                    value=f"{self.qb.raw.get('Amount', '???')}",
                    number_fmt_str="$#,##0.00",
                    number_fmt_type="CURRENCY",
                    align="RIGHT",
                    value_type="Number"
                ),
                fmt_value(
                    value=f"{self.date}",
                    number_fmt_str="MM-DD-YYYY",
                    number_fmt_type="DATE",
                    align="LEFT",
                )
            ]
        }

    def sort_key(self) -> Any:
        return 3, self.qb.index

################################################################################
class NoRecordsToReconcileException(ReconcilerException):

    def __init__(self, sheet_name: str, account_id: int, qb_record: QBServiceRecord) -> None:

        self.sheet_name: str = sheet_name
        self.account_id: int = account_id
        self.qb_record: QBServiceRecord = qb_record
        self.index: int = qb_record.index
        self.date: str = qb_record.date.strftime("%m-%d-%Y")

        super().__init__(
            f"NoRecordsToReconcileException in sheet '{sheet_name}': "
            f"No existing records found for account ID {account_id} "
            f"to reconcile QB Record '{qb_record.raw['Name']}' from row "
            f"{qb_record.index}."
        )

    def to_row_data(self) -> Dict[str, List[Dict[str, Any]]]:
        return {
            "values": [
                fmt_value(
                    value=f"QB Row {self.index}",
                ),
                fmt_value(
                    value=f"{self.qb_record.raw.get('Name', '???')}",
                    align="LEFT"
                ),
                fmt_value(
                    value=(
                        "No Positive Records - There are no existing positive "
                        "balance records for the specified account ID. (On any sheet)"
                    ),
                    align="LEFT"
                ),
                fmt_value(
                    value=f"{self.qb_record.raw.get('Amount', '???')}",
                    number_fmt_str="$#,##0.00",
                    number_fmt_type="CURRENCY",
                    align="RIGHT",
                    value_type="Number"
                ),
                fmt_value(
                    value=f"{self.date}",
                    number_fmt_str="MM-DD-YYYY",
                    number_fmt_type="DATE",
                    align="LEFT",
                )
            ]
        }

    def sort_key(self) -> Any:
        return 4, self.sheet_name, self.qb_record.index

################################################################################
class NoMatchingRecordException(ReconcilerException):

    def __init__(self, sheet_name: str, account_id: int, qb_record: QBServiceRecord) -> None:

        self.sheet_name: str = sheet_name
        self.account_id: int = account_id
        self.qb_record: QBServiceRecord = qb_record
        self.index: int = qb_record.index
        self.date: str = qb_record.date.strftime("%m-%d-%Y")

        super().__init__(
            f"NoMatchingRecordException in sheet '{sheet_name}': "
            f"No matching record found for account ID {account_id} "
            f"to reconcile QB Record '{qb_record.raw['Name']}' from row "
            f"{qb_record.index}."
        )

    def to_row_data(self) -> Dict[str, List[Dict[str, Any]]]:
        return {
            "values": [
                fmt_value(
                    value=f"QB Row {self.index}",
                ),
                fmt_value(
                    value=f"{self.qb_record.raw.get('Name', '???')}",
                    align="LEFT"
                ),
                fmt_value(
                    value=(
                        "No Matching Record Found - Existing records were found, "
                        "but none of the existing records amounts' "
                        "matched the QuickBooks transaction amount for this "
                        "account ID."
                    ),
                    align="LEFT"
                ),
                fmt_value(
                    value=f"{self.qb_record.raw.get('Amount', '???')}",
                    number_fmt_str="$#,##0.00",
                    number_fmt_type="CURRENCY",
                    align="RIGHT",
                    value_type="Number"
                ),
                fmt_value(
                    value=f"{self.date}",
                    number_fmt_str="MM-DD-YYYY",
                    number_fmt_type="DATE",
                    align="LEFT",
                )
            ]
        }

    def sort_key(self) -> Any:
        return 5, self.sheet_name, self.qb_record.index

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

    def to_row_data(self) -> Dict[str, List[Dict[str, Any]]]:
        return {
            "values": [
                fmt_value(
                    value=f"Row {self.index} in {self.sheet_name}",
                ),
                blank_cell(),
                fmt_value(
                    value=(
                        "Numeric Parse Error - Unable to parse a valid numeric "
                        "value from the 'Amount' column."
                    ),
                    align="LEFT"
                ),
                fmt_value(
                    value=f"{self.value}",
                    align="RIGHT"
                )
            ]
        }

    def sort_key(self) -> Any:
        return 6, self.sheet_name, self.index

################################################################################
def fmt_value(
    value: str,
    align: Literal["LEFT", "CENTER", "RIGHT"] = "CENTER",
    number_fmt_str: Optional[str] = None,
    number_fmt_type: Literal["CURRENCY", "DATE"] = "Currency",
    value_type: Literal["String", "Formula", "Number"] = "String",
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

    return {
        "values": [
            fmt_value(value="")
        ]
    }

################################################################################
