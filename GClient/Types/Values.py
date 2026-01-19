from __future__ import annotations

from typing import TypedDict, List, Union

from .Enums import *
################################################################################
class ValueRange(TypedDict):
    """Data within a range of a spreadsheet.

    Members:
        - **range** (str): The A1 notation of the values' range.
        - **majorDimension** (Dimension): The major dimension of the values.
        - **values** (List[List[Union[str, int]]): The data that was read or to be written. This is an array of arrays, the outer array representing all the data and each inner array representing a major dimension. Each item in the inner array corresponds with one cell.
    """
    range: str
    majorDimension: Dimension
    values: List[List[Union[str, int, float, bool, None]]]

################################################################################
