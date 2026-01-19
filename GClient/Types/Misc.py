from __future__ import annotations

from typing import TYPE_CHECKING, TypedDict, Union, NotRequired

from .Enums import *

if TYPE_CHECKING:
    from .Other import GridRange
    from .DeveloperMetadata import DeveloperMetadataLocation
    from .Values import ValueRange
################################################################################
class _DataFilterWithDevMetadata(TypedDict):
    developerMetadataLookup: DeveloperMetadataLookup
    a1Range: NotRequired[None]
    gridRange: NotRequired[None]

class _DataFilterWithA1Range(TypedDict):
    developerMetadataLookup: NotRequired[None]
    a1Range: str
    gridRange: NotRequired[None]

class _DataFilterWithGridRange(TypedDict):
    developerMetadataLookup: NotRequired[None]
    a1Range: NotRequired[None]
    gridRange: GridRange

DataFilter = Union[
    _DataFilterWithDevMetadata,
    _DataFilterWithA1Range,
    _DataFilterWithGridRange
]
"""Filter that describes what data should be selected or returned from a request.

Members:
    - **developerMetadataLookup** (DeveloperMetadataLookup): Selects data associated with the developer metadata matching the criteria described by this ``DeveloperMetadataLookup``.
    - **a1Range** (str): Selects data that matches the specified A1 range.
    - **gridRange** (GridRange): Selects data that matches the range described by the ``GridRange``.

`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/DataFilter>``_
"""

################################################################################
class DeveloperMetadataLookup(TypedDict):
    """Selects DeveloperMetadata that matches all the specified fields.

    Members:
        - **locationType** (DeveloperMetadataLocationType): Limits the selected developer metadata to those entries which are associated with locations of the specified type.
        - **metadataLocation** (DeveloperMetadataLocation): Limits the selected developer metadata to those entries associated with the specified location.
        - **locationMatchingStrategy** (DeveloperMetadataLocationMatchingStrategy): Determines how this lookup matches the location.
        - **metadataId** (int): Limits the selected developer metadata to that which has a matching ``DeveloperMetadata.metadata_id``.
        - **metadataKey** (str): Limits the selected developer metadata to that which has a matching ``DeveloperMetadata.metadata_key``.
        - **metadataValue** (str): Limits the selected developer metadata to that which has a matching ``DeveloperMetadata.metadata_value``.
        - **visibility** (DeveloperMetadataVisibility): Limits the selected developer metadata to that which has a matching ``DeveloperMetadata.visibility``.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/DataFilter#developermetadatalookup>`_
    """
    locationType: DeveloperMetadataLocationType
    metadataLocation: DeveloperMetadataLocation
    locationMatchingStrategy: DeveloperMetadataLocationMatchingStrategy
    metadataId: int
    metadataKey: str
    metadataValue: str
    visibility: DeveloperMetadataVisibility

################################################################################
class DimensionRange(TypedDict):
    """A range along a single dimension on a sheet.

    Members:
        - **sheetId** (int): The sheet this span is on.
        - **dimension** (Dimension): The dimension of the span.
        - **startIndex** (int): The start (inclusive) of the span, or not set if unbounded.
        - **endIndex** (int): The end (exclusive) of the span, or not set if unbounded.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/DimensionRange>`_
    """
    sheetId: int
    dimension: Dimension
    startIndex: int
    endIndex: int

################################################################################
class ErrorDetails(TypedDict):
    """Details about an error that occurred.

    Members:
        - **errorCode** (ErrorCode): Specific error code indicating what went wrong.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/ErrorDetails>`_
    """
    errorCode: ErrorCode

################################################################################
class UpdateValuesResponse(TypedDict):
    """The response when updating a range of values in a spreadsheet.

    Members:
        - **spreadsheetId** (str): The spreadsheet the updates were applied to.
        - **updatedRange** (str): The range (in A1 notation) that was updated.
        - **updatedRows** (int): The number of rows where at least one cell in the row was updated.
        - **updatedColumns** (int): The number of columns where at least one cell in the column was updated.
        - **updatedCells** (int): The number of cells that were updated.
        - **updatedData** (ValueRange): The values of the cells after updates were applied. This is only included if the request's ``includeValuesInResponse`` field was true.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/UpdateValuesResponse>`_
    """
    spreadsheetId: str
    updatedRange: str
    updatedRows: int
    updatedColumns: int
    updatedCells: int
    updatedData: ValueRange

################################################################################
