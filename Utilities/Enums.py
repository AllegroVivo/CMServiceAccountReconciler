from __future__ import annotations

from enum import StrEnum
################################################################################
class _EnumBase(StrEnum):
    # In case we want to add common functionality later
    pass

################################################################################
class ServiceAccountSheet(_EnumBase):

    Annual = "Annual"
    Monthly = "Monthly"
    Plumbing = "Plumbing - Annual"
    Generator = "Generator"
    DuctCleaning = "Duct Cleaning"
    Other = "Other"

################################################################################
class HighlightColor(_EnumBase):

    Yellow = "#FFFF00"
    Green = "#34A853"
    Red = "#FF0000"
    Pink = "#EAD1DC"
    Orange = "#FBBC04"

################################################################################
class Dimension(_EnumBase):

    Rows = "ROWS"
    Columns = "COLUMNS"

################################################################################
class ValueRenderOption(_EnumBase):

    Formatted = "FORMATTED_VALUE"
    Unformatted = "UNFORMATTED_VALUE"
    Formula = "FORMULA"

################################################################################
class DateTimeRenderOption(_EnumBase):

    FmtString = "FORMATTED_STRING"
    SerialNumber = "SERIAL_NUMBER"

################################################################################
class GridRangeType(_EnumBase):

    ValueRange = "ValueRange"
    ListOfLists = "ListOfLists"

################################################################################
