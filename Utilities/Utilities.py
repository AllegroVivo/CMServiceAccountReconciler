from __future__ import annotations

import re

from datetime import date
from typing import TYPE_CHECKING, Any, List, Optional, Sequence, Union, Tuple, Dict
from urllib.parse import quote

if TYPE_CHECKING:
    from App.Classes import MemberName
################################################################################

__all__ = ("Utilities",)

_IRREGULAR_PLURALS = {
    "person": "people",
    # Add here as needed eg: "child": "children", etc.
}

################################################################################
class Utilities:

    @staticmethod
    def safe_quote(value: str, safe: str = "", encoding: str = "utf-8") -> str:

        return quote(value.encode(encoding), safe)

################################################################################
    @staticmethod
    def absolute_range(sheet_name: str, cell_range: str) -> str:

        name = f"{sheet_name.replace("'", "''")}"
        if cell_range:
            return f"'{name}'!{cell_range}"
        return name

################################################################################
    @staticmethod
    def fill_gaps[T](
        _list: Sequence[Sequence[T]],
        rows: Optional[int] = None,
        cols: Optional[int] = None,
        value: T = ""
    ) -> List[Any]:

        if not _list:
            if rows is None or cols is None:
                return []
            return [[value for _ in range(cols)] for _ in range(rows)]

        inferred_max = max(len(r) for r in _list)
        max_cols = cols if cols is not None else inferred_max
        max_rows = rows if rows is not None else len(_list)

        def _rightpad(_row: Sequence[T]) -> List[T]:
            current = list(_row)
            if len(current) >= max_cols:
                return current[:max_cols]
            return current + [value] * (max_cols - len(current))

        padded_rows: List[List[T]] = []
        for row in _list[:max_rows]:
            padded_rows.append(_rightpad(row))

        additional_rows = max_rows - len(padded_rows)
        for _ in range(additional_rows):
            padded_rows.append([value] * max_cols)

        return padded_rows

################################################################################
    @staticmethod
    def make_numeric(value: str, *, default: Any = None) -> Optional[Tuple[bool, Optional[Union[int, float]]]]:

        if isinstance(value, (int, float)):
            return True, value

        assert isinstance(value, str), "Value must be a string"
        v = value.strip()
        cleaned = v.replace(",", "").replace("$", "")

        if cleaned == "":
            return True, default

        try:
            return True, float(cleaned)
        except ValueError:
            pass

        return False, default

################################################################################
    @staticmethod
    def split_name_and_account(raw: str) -> Optional[Tuple[int, str]]:
        """
        Returns:
            A tuple of (account_id, name_str) if parsing is successful,
            None if parsing fails.
        """

        parts = raw.strip().split()
        if not parts:
            return None

        trailing_nums: List[str] = []

        # Strip pure-digit tokens from the end
        while parts and parts[-1].isdigit():
            trailing_nums.insert(0, parts.pop())

        # No account number found - invalid
        if not trailing_nums:
            return None

        account_id_str = trailing_nums[-1]  # Last token is the account ID
        name_tokens = parts + trailing_nums[:-1]  # Combine any earlier numbers into the name
        name_str = " ".join(name_tokens).strip()

        try:
            account_id = int(account_id_str)
            return account_id, name_str
        except ValueError:
            return None

################################################################################
    @staticmethod
    def split_multi_names(raw: str) -> List[Tuple[str, Optional[str], str]]:
        """
         Returns a list of tuples containing (first_name, last_name, raw)
        """

        parts = raw.strip().split()
        if not parts:
            return []

        member_names: List[Tuple[str, Optional[str], str]] = []
        current_name_parts: List[str] = []
        last_name = parts[-1]

        for part in parts[:-1]:
            if part.lower() in ("and", "&"):
                if current_name_parts:
                    if len(current_name_parts) == 2:
                        first_name = current_name_parts[0]
                        last_name = current_name_parts[1]
                    else:
                        first_name = " ".join(current_name_parts).strip()
                    member_names.append((first_name, last_name, raw))
                    current_name_parts = []
            else:
                current_name_parts.append(part)

        if current_name_parts:
            first_name = " ".join(current_name_parts).strip()
            member_names.append((first_name, last_name, raw))

        return member_names

################################################################################
    @staticmethod
    def columns_in_range(range_str: str) -> int:
        """
        Calculate the number of columns in a given range string (e.g., 'A:C' -> 3).
        """
        if ":" not in range_str:
            return 1

        start_col, end_col = range_str.split(":")
        start_idx = Utilities.column_to_index(start_col)
        end_idx = Utilities.column_to_index(end_col)
        return end_idx - start_idx + 1

################################################################################
    @staticmethod
    def column_to_index(col: str) -> int:
        """
        Convert a column letter (e.g., 'A', 'B', ..., 'Z', 'AA', etc.) to a 1-based index.
        """
        idx = 0
        for i, char in enumerate(reversed(col.upper())):
            idx += (ord(char) - ord("A") + 1) * (26 ** i)
        return idx

################################################################################
    @staticmethod
    def index_to_column(idx: int) -> str:
        """
        Convert a 1-based column index to a column letter
        (e.g., 1 -> 'A', 2 -> 'B', ..., 27 -> 'AA', etc.).
        """
        result = []
        while idx > 0:
            idx, remainder = divmod(idx - 1, 26)
            result.append(chr(remainder + ord("A")))
        return "".join(reversed(result))

################################################################################
    @staticmethod
    def iso_date_from_str(date_val: Optional[str]) -> Optional[date]:

        try:
            date_parts = date_val.split("/") if date_val else []
            iso_date = None
            if len(date_parts) == 3:
                if len(date_parts[2]) != 4:
                    date_parts[2] = f"20{date_parts[2]}"
                iso_date = f"{date_parts[2]}-{int(date_parts[0]):02}-{int(date_parts[1]):02}"
            elif len(date_parts) == 2:
                if len(date_parts[1]) != 4:
                    date_parts[1] = f"20{date_parts[1]}"
                iso_date = f"{date_parts[1]}-{int(date_parts[0]):02}-01"

            return date.fromisoformat(iso_date)
        except (TypeError, ValueError):
            # Probably text or empty value.
            return None

################################################################################
    @staticmethod
    def camel_to_snake(name: str) -> str:
        # Handles acronyms like URLThing -> url_thing
        s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
        s2 = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1)
        return s2.lower()

################################################################################
    @staticmethod
    def pluralize(s: str) -> str:

        if s in _IRREGULAR_PLURALS:
            return _IRREGULAR_PLURALS[s]
        if s.endswith(("s", "x", "z", "ch", "sh")):
            return s + "es"
        if len(s) >= 2 and s.endswith("y") and s[-2] not in "aeiou":
            return s[:-1] + "ies"
        return s + "s"

################################################################################
    @staticmethod
    def get_sheet_map() -> Dict[int, str]:
        """A dictionary mapping numbers in a series to sheet names.

        1. Annual
        2. Monthly
        3. Plumbing - Annual
        4. Generator
        5. Duct Cleaning
        """
        # Unused in current implementation.
        return {
            1: "Annual",
            2: "Monthly",
            3: "Plumbing - Annual",
            4: "Generator",
            5: "Duct Cleaning"
        }

################################################################################
    @staticmethod
    def account_name_str(account_id: Optional[int], names: List[MemberName]) -> str:

        if len(names) == 1:
            n = names[0]
            return f"{n.first} {n.last} {account_id if account_id else ''}"

        name_str = ""
        for i, n in enumerate(names):
            if i != len(names) - 1:
                name_str += f"{n.first} and "
            else:
                name_str += f"{n.first} {n.last} "

        if account_id:
            name_str += f"{account_id}"

        return name_str.strip()

################################################################################
    @staticmethod
    def distance_between(col1: str, col2: str) -> int:
        """Calculate the number of columns between two column letters."""
        idx1 = Utilities.column_to_index(col1)
        idx2 = Utilities.column_to_index(col2)
        return abs(idx2 - idx1)

################################################################################
