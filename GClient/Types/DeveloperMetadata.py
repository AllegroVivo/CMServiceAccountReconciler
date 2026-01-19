from __future__ import annotations

from typing import TYPE_CHECKING, TypedDict, Union, NotRequired

from .Enums import *

if TYPE_CHECKING:
    from .Misc import DimensionRange
################################################################################
class DeveloperMetadata(TypedDict):
    """Developer metadata associated with a location or object in a spreadsheet.

    Developer metadata may be used to associate arbitrary data with various
    parts of a spreadsheet and will remain associated at those locations as
    they move around and the spreadsheet is edited. For example, if developer
    metadata is associated with row 5 and another row is then subsequently
    inserted above row 5, that original metadata will still be associated with
    the row it was first associated with (what is now row 6). If the associated
    object is deleted its metadata is deleted too.

    Members:
        - **metadataId** (int): The spreadsheet-scoped unique ID that identifies the metadata. Must be positive.
        - **metadataKey** (str): The metadata key. There may be multiple metadata in a spreadsheet with the same key. Developer metadata must always have a key specified.
        - **metadataValue** (str): Data associated with the metadata's key.
        - **location** (DeveloperMetadataLocation): The location where the metadata is associated.
        - **visibility** (DeveloperMetadataVisibility): The metadata visibility. Developer metadata must always have a visibility specified.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets.developerMetadata>`_
    """
    metadataId: int
    metadataKey: str
    metadataValue: str
    location: DeveloperMetadataLocation
    visibility: DeveloperMetadataVisibility

################################################################################
class _DeveloperMetadataLocationBase(TypedDict):
    locationType: DeveloperMetadataLocationType

class _DeveloperMetadataLocationSpreadsheet(_DeveloperMetadataLocationBase):
    spreadsheet: bool
    sheetId: NotRequired[None]
    dimensionRange: NotRequired[None]

class _DeveloperMetadataLocationSheet(_DeveloperMetadataLocationBase):
    spreadsheet: NotRequired[None]
    sheetId: int
    dimensionRange: NotRequired[None]

class _DeveloperMetadataLocationDimensionRange(_DeveloperMetadataLocationBase):
    spreadsheet: NotRequired[None]
    sheetId: NotRequired[None]
    dimensionRange: DimensionRange

DeveloperMetadataLocation = Union[
    _DeveloperMetadataLocationSpreadsheet,
    _DeveloperMetadataLocationSheet,
    _DeveloperMetadataLocationDimensionRange
]
"""A location where metadata may be associated in a spreadsheet.

Members:
    - **locationType** (DeveloperMetadataLocationType): The type of location this metadata is associated with. This field is read-only.
    - **spreadsheet** (bool): True when metadata is associated with an entire spreadsheet.
    - **sheetId** (int): The ID of the sheet when metadata is associated with an entire sheet.
    - **dimensionRange** (DimensionRange): Represents the row or column when metadata is associated with a dimension. The specified ``DimensionRange`` must represent a single row or column; it cannot be unbounded or span multiple rows or columns.

`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets.developerMetadata#developermetadatalocation>`_
"""

################################################################################
