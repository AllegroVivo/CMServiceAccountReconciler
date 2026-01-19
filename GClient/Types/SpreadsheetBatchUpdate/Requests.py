from __future__ import annotations

from typing import TYPE_CHECKING, TypedDict, Union, NotRequired, List

from ..Enums import *

if TYPE_CHECKING:
    from ..Cells import CellData, Border, DataValidationRule
    from ..Charts import EmbeddedChart, ChartSpec
    from ..DeveloperMetadata import DeveloperMetadata
    from ..Misc import DimensionRange, DataFilter
    from ..Other import (
        DataSourceColumnReference, GridRange, GridCoordinate,
        EmbeddedObjectPosition, SortSpec,
    )
    from ..Sheets import (
        SheetProperties, DimensionProperties, RowData, FilterView,
        ConditionalFormatRule, BasicFilter, ProtectedRange, BandedRange,
        DimensionGroup, Slicer, SlicerSpec, Table,
    )
    from ..Spreadsheets import SpreadsheetProperties, NamedRange, DataSource
################################################################################
class _RequestUpdateSpreadsheetProperties(TypedDict):
    updateSpreadsheetProperties: UpdateSpreadsheetPropertiesRequest

class _RequestUpdateSheetProperties(TypedDict):
    updateSheetProperties: UpdateSheetPropertiesRequest

class _RequestUpdateDimensionProperties(TypedDict):
    updateDimensionProperties: UpdateDimensionPropertiesRequest

class _RequestUpdateNamedRange(TypedDict):
    updateNamedRange: UpdateNamedRangeRequest

class _RequestRepeatCell(TypedDict):
    repeatCell: RepeatCellRequest

class _RequestAddNamedRange(TypedDict):
    addNamedRange: AddNamedRangeRequest

class _RequestDeleteNamedRange(TypedDict):
    deleteNamedRange: DeleteNamedRangeRequest

class _RequestAddSheet(TypedDict):
    addSheet: AddSheetRequest

class _RequestDeleteSheet(TypedDict):
    deleteSheet: DeleteSheetRequest

class _RequestAutoFill(TypedDict):
    autoFill: AutoFillRequest

class _RequestCutPaste(TypedDict):
    cutPaste: CutPasteRequest

class _RequestCopyPaste(TypedDict):
    copyPaste: CopyPasteRequest

class _RequestMergeCells(TypedDict):
    mergeCells: MergeCellsRequest

class _RequestUnmergeCells(TypedDict):
    unmergeCells: UnmergeCellsRequest

class _RequestUpdateBorders(TypedDict):
    updateBorders: UpdateBordersRequest

class _RequestUpdateCells(TypedDict):
    updateCells: UpdateCellsRequest

class _RequestAddFilterView(TypedDict):
    addFilterView: AddFilterViewRequest

class _RequestAppendCells(TypedDict):
    appendCells: AppendCellsRequest

class _RequestClearBasicFilter(TypedDict):
    clearBasicFilter: ClearBasicFilterRequest

class _RequestDeleteDimension(TypedDict):
    deleteDimension: DeleteDimensionRequest

class _RequestDeleteEmbeddedObject(TypedDict):
    deleteEmbeddedObject: DeleteEmbeddedObjectRequest

class _RequestDeleteFilterView(TypedDict):
    deleteFilterView: DeleteFilterViewRequest

class _RequestDuplicateFilterView(TypedDict):
    duplicateFilterView: DuplicateFilterViewRequest

class _RequestDuplicateSheet(TypedDict):
    duplicateSheet: DuplicateSheetRequest

class _RequestFindReplace(TypedDict):
    findReplace: FindReplaceRequest

class _RequestInsertDimension(TypedDict):
    insertDimension: InsertDimensionRequest

class _RequestInsertRange(TypedDict):
    insertRange: InsertRangeRequest

class _RequestMoveDimension(TypedDict):
    moveDimension: MoveDimensionRequest

class _RequestUpdateEmbeddedObjectPosition(TypedDict):
    updateEmbeddedObjectPosition: UpdateEmbeddedObjectPositionRequest

class _RequestPasteData(TypedDict):
    pasteData: PasteDataRequest

class _RequestTextToColumns(TypedDict):
    textToColumns: TextToColumnsRequest

class _RequestUpdateFilterView(TypedDict):
    updateFilterView: UpdateFilterViewRequest

class _RequestDeleteRange(TypedDict):
    deleteRange: DeleteRangeRequest

class _RequestAppendDimension(TypedDict):
    appendDimension: AppendDimensionRequest

class _RequestAddConditionalFormatRule(TypedDict):
    addConditionalFormatRule: AddConditionalFormatRuleRequest

class _RequestUpdateConditionalFormatRule(TypedDict):
    updateConditionalFormatRule: UpdateConditionalFormatRuleRequest

class _RequestDeleteConditionalFormatRule(TypedDict):
    deleteConditionalFormatRule: DeleteConditionalFormatRuleRequest

class _RequestSortRange(TypedDict):
    sortRange: SortRangeRequest

class _RequestSetDataValidation(TypedDict):
    setDataValidation: SetDataValidationRequest

class _RequestSetBasicFilter(TypedDict):
    setBasicFilter: SetBasicFilterRequest

class _RequestAddProtectedRange(TypedDict):
    addProtectedRange: AddProtectedRangeRequest

class _RequestUpdateProtectedRange(TypedDict):
    updateProtectedRange: UpdateProtectedRangeRequest

class _RequestDeleteProtectedRange(TypedDict):
    deleteProtectedRange: DeleteProtectedRangeRequest

class _RequestAutoResizeDimensions(TypedDict):
    autoResizeDimensions: AutoResizeDimensionsRequest

class _RequestAddChart(TypedDict):
    addChart: AddChartRequest

class _RequestUpdateChartSpec(TypedDict):
    updateChartSpec: UpdateChartSpecRequest

class _RequestUpdateBanding(TypedDict):
    updateBanding: UpdateBandingRequest

class _RequestAddBanding(TypedDict):
    addBanding: AddBandingRequest

class _RequestDeleteBanding(TypedDict):
    deleteBanding: DeleteBandingRequest

class _RequestCreateDeveloperMetadata(TypedDict):
    createDeveloperMetadata: CreateDeveloperMetadataRequest

class _RequestUpdateDeveloperMetadata(TypedDict):
    updateDeveloperMetadata: UpdateDeveloperMetadataRequest

class _RequestDeleteDeveloperMetadata(TypedDict):
    deleteDeveloperMetadata: DeleteDeveloperMetadataRequest

class _RequestRandomizeRange(TypedDict):
    randomizeRange: RandomizeRangeRequest

class _RequestAddDimensionGroup(TypedDict):
    addDimensionGroup: AddDimensionGroupRequest

class _RequestDeleteDimensionGroup(TypedDict):
    deleteDimensionGroup: DeleteDimensionGroupRequest

class _RequestUpdateDimensionGroup(TypedDict):
    updateDimensionGroup: UpdateDimensionGroupRequest

class _RequestTrimWhitespace(TypedDict):
    trimWhitespace: TrimWhiteSpaceRequest

class _RequestDeleteDuplicates(TypedDict):
    deleteDuplicates: DeleteDuplicatesRequest

class _RequestUpdateEmbeddedObjectBorder(TypedDict):
    updateEmbeddedObjectBorder: UpdateEmbeddedObjectBorderRequest

class _RequestAddSlicer(TypedDict):
    addSlicer: AddSlicerRequest

class _RequestUpdateSlicer(TypedDict):
    updateSlicerSpec: UpdateSlicerSpecRequest

class _RequestAddDataSource(TypedDict):
    addDataSource: AddDataSourceRequest

class _RequestUpdateDataSource(TypedDict):
    updateDataSource: UpdateDataSourceRequest

class _RequestDeleteDataSource(TypedDict):
    deleteDataSource: DeleteDataSourceRequest

class _RequestRefreshDataSource(TypedDict):
    refreshDataSource: RefreshDataSourceRequest

class _RequestCancelDataSourceRefresh(TypedDict):
    cancelDataSourceRefresh: CancelDataSourceRefreshRequest

class _RequestAddTable(TypedDict):
    addTable: AddTableRequest

class _RequestUpdateTable(TypedDict):
    updateTable: UpdateTableRequest

class _RequestDeleteTable(TypedDict):
    deleteTable: DeleteTableRequest

SpreadsheetBatchUpdateRequest = Union[
    _RequestUpdateSpreadsheetProperties,
    _RequestUpdateSheetProperties,
    _RequestUpdateDimensionProperties,
    _RequestUpdateNamedRange,
    _RequestRepeatCell,
    _RequestAddNamedRange,
    _RequestDeleteNamedRange,
    _RequestAddSheet,
    _RequestDeleteSheet,
    _RequestAutoFill,
    _RequestCutPaste,
    _RequestCopyPaste,
    _RequestMergeCells,
    _RequestUnmergeCells,
    _RequestUpdateBorders,
    _RequestUpdateCells,
    _RequestAddFilterView,
    _RequestAppendCells,
    _RequestClearBasicFilter,
    _RequestDeleteDimension,
    _RequestDeleteEmbeddedObject,
    _RequestDeleteFilterView,
    _RequestDuplicateFilterView,
    _RequestDuplicateSheet,
    _RequestFindReplace,
    _RequestInsertDimension,
    _RequestInsertRange,
    _RequestMoveDimension,
    _RequestUpdateEmbeddedObjectPosition,
    _RequestPasteData,
    _RequestTextToColumns,
    _RequestUpdateFilterView,
    _RequestDeleteRange,
    _RequestAppendDimension,
    _RequestAddConditionalFormatRule,
    _RequestUpdateConditionalFormatRule,
    _RequestDeleteConditionalFormatRule,
    _RequestSortRange,
    _RequestSetDataValidation,
    _RequestSetBasicFilter,
    _RequestAddProtectedRange,
    _RequestUpdateProtectedRange,
    _RequestDeleteProtectedRange,
    _RequestAutoResizeDimensions,
    _RequestAddChart,
    _RequestUpdateChartSpec,
    _RequestUpdateBanding,
    _RequestAddBanding,
    _RequestDeleteBanding,
    _RequestCreateDeveloperMetadata,
    _RequestUpdateDeveloperMetadata,
    _RequestDeleteDeveloperMetadata,
    _RequestRandomizeRange,
    _RequestAddDimensionGroup,
    _RequestDeleteDimensionGroup,
    _RequestUpdateDimensionGroup,
    _RequestTrimWhitespace,
    _RequestDeleteDuplicates,
    _RequestUpdateEmbeddedObjectBorder,
    _RequestAddSlicer,
    _RequestUpdateSlicer,
    _RequestAddDataSource,
    _RequestUpdateDataSource,
    _RequestDeleteDataSource,
    _RequestRefreshDataSource,
    _RequestCancelDataSourceRefresh,
    _RequestAddTable,
    _RequestUpdateTable,
    _RequestDeleteTable
]
"""A single kind of update to apply to a spreadsheet.

See each individual request type for more details.

`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#request>`_
"""

################################################################################
class UpdateSpreadsheetPropertiesRequest(TypedDict):
    """Updates properties of a spreadsheet.

    Members:
        - **properties** (SpreadsheetProperties): The spreadsheet properties to update.
        - **fields** (str): The fields that should be updated. At least one field must be specified. The root ``properties`` is implied and should not be specified. A single ``*`` can be used as shorthand for listing every field.

    `Google API  reference<https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#updatespreadsheetpropertiesrequest>`_
    """
    properties: SpreadsheetProperties
    fields: str

################################################################################
class UpdateSheetPropertiesRequest(TypedDict):
    """Updates properties of the sheet with the specified ``sheetId``.

    Members:
        - **properties** (SheetProperties): The sheet properties to update.
        - **fields** (str): The fields that should be updated. At least one field must be specified. The root ``properties`` is implied and should not be specified. A single ``*`` can be used as shorthand for listing every field.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#updatesheetpropertiesrequest>`_
    """
    properties: SheetProperties
    fields: str

################################################################################
class _UpdateDimensionPropertiesRequestBase(TypedDict, total=False):
    properties: DimensionProperties
    fields: str

class _UpdateDimensionPropertiesRequestWithRange(_UpdateDimensionPropertiesRequestBase):
    range: DimensionRange
    dataSourceSheetRange: NotRequired[None]

class _UpdateDimensionPropertiesRequestWithDataSourceSheetRange(_UpdateDimensionPropertiesRequestBase):
    range: NotRequired[None]
    dataSourceSheetRange: DataSourceSheetDimensionRange

UpdateDimensionPropertiesRequest = Union[
    _UpdateDimensionPropertiesRequestWithRange,
    _UpdateDimensionPropertiesRequestWithDataSourceSheetRange
]
"""Updates properties of dimensions within the specified range.

Members:
    - **properties** (DimensionProperties): The properties to update.
    - **fields** (str): The fields that should be updated. At least one field must be specified. The root ``properties`` is implied and should not be specified. A single ``*`` can be used as shorthand for listing every field.
    - **range** (DimensionRange): The rows or columns to update.
    - **dataSourceSheetRange** (DataSourceSheetDimensionRange): The columns on a data source sheet to update.
    
`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#updatedimensionpropertiesrequest>`_
"""

################################################################################
class DataSourceSheetDimensionRange(TypedDict):
    """A range along a single dimension on a ``DATA_SOURCE`` sheet.

    Members:
        - **sheetId** (int): The ID of the data source sheet the range is on.
        - **columnReferences** (List[DataSourceColumnReference]): The columns on the data source sheet.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/other#datasourcesheetdimensionrange>`_
    """
    sheetId: int
    columnReferences: List[DataSourceColumnReference]

################################################################################
class UpdateNamedRangeRequest(TypedDict):
    """Updates properties of the named range with the specified ``namedRangeId``.

    Members:
        - **namedRange** (NamedRange): The named range to update with the new properties.
        - **fields** (str): The fields that should be updated. At least one field must be specified. The root ``namedRange`` is implied and should not be specified. A single ``*`` can be used as shorthand for listing every field.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#updatenamedrangerequest>`_
    """
    namedRange: NamedRange
    fields: str

################################################################################
class RepeatCellRequest(TypedDict):
    """Updates all cells in the range to the values in the given Cell object.

    Only the fields listed in the fields field are updated; others are unchanged.

    If writing a cell with a formula, the formula's ranges will automatically
    increment for each field in the range. For example, if writing a cell with
    formula ``=A1`` into range B2:C4, B2 would be ``=A1``, B3 would be ``=A2``,
    B4 would be ``=A3``, C2 would be ``=B1``, C3 would be ``=B2``, C4 would be ``=B3``.

    To keep the formula's ranges static, use the $ indicator. For example, use
    the formula ``=$A$1`` to prevent both the row and the column from incrementing.

    Members:
        - **range** (GridRange): The range to repeat the cell in.
        - **cell** (CellData): The cell data to write.
        - **fields** (str): The fields that should be updated. At least one field must be specified. The root ``cell`` is implied and should not be specified. A single ``"*"`` can be used as shorthand for listing every field.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#repeatcellrequest>`_
    """
    range: GridRange
    cell: CellData
    fields: str

################################################################################
class AddNamedRangeRequest(TypedDict):
    """Adds a named range to the spreadsheet.

    Members:
        - **namedRange** (NamedRange): The named range to add. The ``namedRangeId`` field is optional; if one is not set, an id will be randomly generated.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#addnamedrangerequest>`_
    """
    namedRange: NamedRange

################################################################################
class DeleteNamedRangeRequest(TypedDict):
    """Removes the named range with the given ID from the spreadsheet.

    Members:
        - **namedRangeId** (str): The ID of the named range to delete.
    """
    namedRangeId: str

################################################################################
class AddSheetRequest(TypedDict):
    """Adds a new sheet.

    When a sheet is added at a given index, all subsequent sheets' indexes are
    incremented. To add an object sheet, use ``AddChartRequest`` instead and specify
    ``EmbeddedObjectPosition.sheetId`` or ``EmbeddedObjectPosition.newSheet``.

    Members:
        - **properties** (SheetProperties): The properties the new sheet should have. All properties are optional. The ``sheetId`` field is optional; if one is not set, an id will be randomly generated.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#addsheetrequest>`_
    """
    properties: SheetProperties

################################################################################
class DeleteSheetRequest(TypedDict):
    """Deletes the requested sheet.

    Members:
        - **sheetId** (int): The ID of the sheet to delete.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#deletesheetrequest>`_
    """
    sheetId: int

################################################################################
class _AutoFillRequestBase(TypedDict, total=False):
    useAlternateSeries: bool

class _AutoFillRequestWithRange(_AutoFillRequestBase):
    range: GridRange
    sourceAndDestination: NotRequired[None]

class _AutoFillRequestWithSourceAndDestination(_AutoFillRequestBase):
    range: NotRequired[None]
    sourceAndDestination: SourceAndDestination

AutoFillRequest = Union[
    _AutoFillRequestWithRange,
    _AutoFillRequestWithSourceAndDestination
]
"""Fills in more data based on existing data.

Members:
    - **useAlternateSeries** (bool): True if we should generate data with the "alternate" series. This differs based on the type and amount of source data.
    - **range** (GridRange): The range to autofill. This will examine the range and detect the location that has data and automatically fill that data in to the rest of the range.
    - **sourceAndDestination** (SourceAndDestination): The source and destination areas to autofill. This explicitly lists the source of the autofill and where to extend that data.
    
`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#autofillrequest>`_
"""

################################################################################
class SourceAndDestination(TypedDict):
    """A combination of a source range and how to extend that source.

    Members:
        - **source** (GridRange): The location of the data to use as the source of the autofill.
        - **dimension** (Dimension): The dimension that data should be filled into.
        - **fillLength** (int): The number of rows or columns that data should be filled into. Positive numbers expand beyond the last row or last column of the source. Negative numbers expand before the first row or first column of the source.
    """
    source: GridRange
    dimension: Dimension
    fillLength: int

################################################################################
class CutPasteRequest(TypedDict):
    """Moves data from the source to the destination.

    Members:
        - **source** (GridRange): The source data to cut.
        - **destination** (GridCoordinate): The top-left coordinate of the destination range.
        - **pasteType** (PasteType): What kind of data to paste.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#cutpasterequest>`_
    """
    source: GridRange
    destination: GridCoordinate
    pasteType: PasteType

################################################################################
class CopyPasteRequest(TypedDict):
    """Copies data from the source to the destination.

    Members:
        - **source** (GridRange): The source data to copy.
        - **destination** (GridRange): The location to paste to.
        - **pasteType** (PasteType): What kind of data to paste.
        - **pasteOrientation** (PasteOrientation): How the data should be oriented when pasting.
    """
    source: GridRange
    destination: GridRange
    pasteType: PasteType
    pasteOrientation: PasteOrientation

################################################################################
class MergeCellsRequest(TypedDict):
    """Merges all cells in the range.

    Members:
        - **range** (GridRange): The range of cells to merge.
        - **mergeType** (MergeType): The type of merge to perform.
    """
    range: GridRange
    mergeType: MergeType

################################################################################
class UnmergeCellsRequest(TypedDict):
    """Unmerges cells in the given range.

    Members:
        - **range** (GridRange): The range within which all cells should be unmerged. If the range spans multiple merges, all will be unmerged. The range must not partially span any merge.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#unmergecellsrequest>`_
    """
    range: GridRange

################################################################################
class UpdateBordersRequest(TypedDict):
    """Updates the borders of a range.

    If a field is not set in the request, that means the border remains as-is.
    For example, with two subsequent UpdateBordersRequest:

    - range: A1:A5 ``{ top: RED, bottom: WHITE }``
    - range: A1:A5 ``{ left: BLUE }``

    That would result in A1:A5 having a borders of ``{ top: RED, bottom: WHITE, left: BLUE }``.
    If you want to clear a border, explicitly set the style to ``NONE``.

    Members:
        - **range** (GridRange): The range whose borders should be updated.
        - **top** (Border): The border to put on the top of the range.
        - **bottom** (Border): The border to put on the bottom of the range.
        - **left** (Border): The border to put on the left of the range.
        - **right** (Border): The border to put on the right of the range.
        - **innerHorizontal** (Border): The horizontal border to put within the range.
        - **innerVertical** (Border): The vertical border to put within the range.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#updatebordersrequest>`_
    """
    range: GridRange
    top: Border
    bottom: Border
    left: Border
    right: Border
    innerHorizontal: Border
    innerVertical: Border

################################################################################
class _UpdateCellsRequestBase(TypedDict, total=False):
    rows: List[RowData]
    fields: str

class _UpdateCellsRequestWithStart(_UpdateCellsRequestBase):
    start: GridCoordinate
    range: NotRequired[None]

class _UpdateCellsRequestWithRange(_UpdateCellsRequestBase):
    start: NotRequired[None]
    range: GridRange

UpdateCellsRequest = Union[
    _UpdateCellsRequestWithStart,
    _UpdateCellsRequestWithRange
]
"""Updates all cells in a range with new data.

Members:
    - **rows** (List[RowData]): The data to write.
    - **fields** (str): The fields that should be updated. At least one field must be specified. The root ``rows`` is implied and should not be specified. A single ``*`` can be used as shorthand for listing every field.
    - **start** (GridCoordinate): The coordinate to start updating data at.
    - **range** (GridRange): The range to write data to.
    
`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#updatecellsrequest>`_
"""

################################################################################
class AddFilterViewRequest(TypedDict):
    """Adds a filter view.

    Members:
        - **filter** (FilterView): The filter to add. The ``filterViewId`` field is optional; if one is not set, an id will be randomly generated.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#addfilterviewrequest>`_
    """
    filter: FilterView

################################################################################
class AppendCellsRequest(TypedDict):
    """Adds new cells after the last row with data in a sheet, inserting new
    rows into the sheet if necessary.

    Members:
        - **sheetId** (int): The sheet ID to append the data to.
        - **rows** (List[RowData]): The data to append.
        - **fields** (str): The fields that should be updated. At least one field must be specified. The root ``rows`` is implied and should not be specified. A single ``*`` can be used as shorthand for listing every field.
        - **tableId** (str): The ID of the table to append data to. The data will be only appended to the table body.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#appendcellsrequest>`_
    """
    sheetId: int
    rows: List[RowData]
    fields: str
    tableId: str

################################################################################
class ClearBasicFilterRequest(TypedDict):
    """Clears the basic filter on a sheet, if it exists.

    Members:
        - **sheetId** (int): The sheet ID on which the basic filter should be cleared.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#clearbasicfilterrequest>`_
    """
    sheetId: int

################################################################################
class DeleteDimensionRequest(TypedDict):
    """Deletes rows or columns in a sheet.

    Members:
        - **range** (DimensionRange): The range of dimensions to delete from the sheet.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#deletedimensionrequest>`_
    """
    range: DimensionRange

################################################################################
class DeleteEmbeddedObjectRequest(TypedDict):
    """Deletes an embedded object (e.g., chart, image) in a sheet.

    Members:
        - **objectId** (int): The ID of the embedded object to delete.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#deleteembeddedobjectrequest>`_
    """
    objectId: int

################################################################################
class DeleteFilterViewRequest(TypedDict):
    """Deletes a filter view from a sheet.

    Members:
        - **filterId** (int): The ID of the filter to delete.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#deletefilterviewrequest>`_
    """
    filterId: int

################################################################################
class DuplicateFilterViewRequest(TypedDict):
    """Duplicates a filter view.

    Members:
        - **filterId** (int): The ID of the filter to duplicate.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#duplicatefilterviewrequest>`_
    """
    filterId: int

################################################################################
class DuplicateSheetRequest(TypedDict):
    """Duplicates a sheet.

    Members:
        - **sourceSheetId** (int): The sheet to duplicate. If the source sheet is of ``DATA_SOURCE`` type, its backing ``DataSource`` is also duplicated and associated with the new copy of the sheet.
        - **newSheetId** (int): The zero-based index where the new sheet should be inserted. The index of all sheets after this are incremented.
        - **insertSheetIndex** (int): If set, the ID of the new sheet. If not set, an ID is chosen. If set, the ID must not conflict with any existing sheet ID. If set, it must be non-negative.
        - **newSheetName** (str): The name of the new sheet. If empty, a new name is chosen for you.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#duplicatesheetrequest>`_
    """
    sourceSheetId: int
    insertSheetIndex: int
    newSheetId: int
    newSheetName: str

################################################################################
class _FindReplaceRequestBase(TypedDict, total=False):
    find: str
    replacement: str
    matchCase: bool
    matchEntireCell: bool
    searchByRegex: bool
    includeFormulas: bool

class _FindReplaceRequestWithRange(_FindReplaceRequestBase):
    range: GridRange
    sheetId: NotRequired[None]
    allSheets: NotRequired[None]

class _FindReplaceRequestWithSheetId(_FindReplaceRequestBase):
    range: NotRequired[None]
    sheetId: int
    allSheets: NotRequired[None]

class _FindReplaceRequestWithAllSheets(_FindReplaceRequestBase):
    range: NotRequired[None]
    sheetId: NotRequired[None]
    allSheets: bool

FindReplaceRequest = Union[
    _FindReplaceRequestWithRange,
    _FindReplaceRequestWithSheetId,
    _FindReplaceRequestWithAllSheets
]
"""Finds and replaces data in cells over a range, sheet, or all sheets.

Members:
    - **find** (str): The value to search.
    - **replacement** (str): The value to use as the replacement.
    - **matchCase** (bool): True if the search is case sensitive.
    - **matchEntireCell** (bool): True if the find value should match the entire cell.
    - **searchByRegex** (bool): True if the find value is a regex.
    - **includeFormulas** (bool): True if the find should include cells with formulas.
    - **range** (GridRange): The range to find and replace over.
    - **sheetId** (int): The sheet to find and replace over.
    - **allSheets** (bool): True to find and replace over all sheets.
    
`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#findreplacerequest>`_
"""

################################################################################
class InsertDimensionRequest(TypedDict):
    """Inserts rows or columns in a sheet at a particular index.

    Members:
        - **range** (DimensionRange): The dimensions to insert. Both the start and end indexes must be bounded.
        - **inheritFromBefore** (bool): True if the new dimensions should inherit properties from the dimensions before them; false if they should inherit from the dimensions after them.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#insertdimensionrequest>`_
    """
    range: DimensionRange
    inheritFromBefore: bool

################################################################################
class InsertRangeRequest(TypedDict):
    """Inserts cells into a range, shifting the existing cells over or down.

    Members:
        - **range** (GridRange): The range to insert new cells into. The range is constrained to the current sheet boundaries.
        - **shiftDimension** (Dimension): The dimension which will be shifted when inserting cells. If ``ROWS``, existing cells will be shifted down. If ``COLUMNS``, existing cells will be shifted right.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#insertrangerequest>`_
    """
    range: GridRange
    shiftDimension: Dimension

################################################################################
class MoveDimensionRequest(TypedDict):
    """Moves rows or columns to another location in a sheet.

    Members:
        - **source** (DimensionRange): The source dimensions to move.
        - **destinationIndex** (int): The index of the first row or column in the destination.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#movedimensionrequest>`_
    """
    source: DimensionRange
    destinationIndex: int

################################################################################
class UpdateEmbeddedObjectPositionRequest(TypedDict):
    """Updates the position of an embedded object in a sheet.

    Members:
        - **objectId** (int): The ID of the object to move.
        - **newPosition** (EmbeddedObjectPosition): An explicit position to move the embedded object to.
        - **fields** (str): The fields of ``OverlayPosition`` that should be updated when setting a new position. Used only if ``newPosition.overlayPosition`` is set, in which case at least one field must be specified. The root ``newPosition.overlayPosition`` is implied and should not be specified. A single ``"*"`` can be used as shorthand for listing every field.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#updateembeddedobjectpositionrequest>`_
    """
    objectId: int
    newPosition: EmbeddedObjectPosition
    fields: str

################################################################################
class _PasteDataRequestBase(TypedDict, total=False):
    coordinate: GridCoordinate
    data: str
    type: PasteType

class _PasteDataRequestWithDelimiter(_PasteDataRequestBase):
    delimiter: str
    html: NotRequired[None]

class _PasteDataRequestWithHtml(_PasteDataRequestBase):
    delimiter: NotRequired[None]
    html: bool

PasteDataRequest = Union[
    _PasteDataRequestWithDelimiter,
    _PasteDataRequestWithHtml
]
"""Inserts data into the spreadsheet starting at the specified coordinate.

Members:
    - **coordinate** (GridCoordinate): The coordinate at which the data should be inserted.
    - **data** (str): The data to insert.
    - **type** (PasteType): The paste type to use.
    - **delimiter** (str): The delimiter to use if the data is delimited.
    - **html** (bool): True if the data is HTML.
    
`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#pastedatarequest>`_
"""

################################################################################
class TextToColumnsRequest(TypedDict):
    """Splits cells in a column into multiple columns based on a delimiter.

    Members:
        - **source** (GridRange): The range to split. This must span exactly one column.
        - **delimiter** (str): The delimiter to use if ``delimiterType`` is ``CUSTOM``.
        - **delimiterType** (DelimiterType): The delimiter type to use.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#texttocolumnsrequest>`_
    """
    source: GridRange
    delimiter: str
    delimiterType: DelimiterType

################################################################################
class UpdateFilterViewRequest(TypedDict):
    """Updates a filter view.

    Members:
        - **filter** (FilterView): The new properties of the filter view.
        - **fields** (str): The fields that should be updated. At least one field must be specified. The root ``filter`` is implied and should not be specified. A single ``"*"`` can be used as shorthand for listing every field.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#updatefilterviewrequest>`_
    """
    filter: FilterView
    fields: str

################################################################################
class DeleteRangeRequest(TypedDict):
    """Deletes cells in a range, shifting the remaining cells over or up.

    Members:
        - **range** (GridRange): The range of cells to delete.
        - **shiftDimension** (Dimension): The dimension which will be shifted to replace the deleted cells. If ``ROWS``, existing cells will be shifted up. If ``COLUMNS``, existing cells will be shifted left.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#deleterangerequest>`_
    """
    range: GridRange
    shiftDimension: Dimension

################################################################################
class AppendDimensionRequest(TypedDict):
    """Appends rows or columns to the end of a sheet.

    Members:
        - **sheetId** (int): The ID of the sheet to append rows or columns to.
        - **dimension** (Dimension): Whether rows or columns should be appended.
        - **length** (int): The number of rows or columns to append.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#appenddimensionrequest>`_
    """
    sheetId: int
    dimension: Dimension
    length: int

################################################################################
class AddConditionalFormatRuleRequest(TypedDict):
    """Adds a new conditional format rule.

    Members:
        - **rule** (ConditionalFormatRule): The rule to add.
        - **index** (int): The zero-based index where the rule should be inserted.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#addconditionalformatrulerequest>`_
    """
    rule: ConditionalFormatRule
    index: int

################################################################################
class _UpdateConditionalFormatRuleRequestBase(TypedDict, total=False):
    index: int
    sheetId: int

class _UpdateConditionalFormatRuleRequestByRule(_UpdateConditionalFormatRuleRequestBase):
    rule: ConditionalFormatRule
    newIndex: NotRequired[None]

class _UpdateConditionalFormatRuleRequestByIndex(_UpdateConditionalFormatRuleRequestBase):
    rule: NotRequired[None]
    newIndex: int

UpdateConditionalFormatRuleRequest = Union[
    _UpdateConditionalFormatRuleRequestByRule,
    _UpdateConditionalFormatRuleRequestByIndex
]
"""Updates a conditional format rule at the given index, or moves a conditional 
format rule to another index.

Members:
    - **index** (int): The zero-based index of the rule that should be replaced or moved.
    - **sheetId** (int): The sheet of the rule to move. Required if ``newIndex`` is set, unused otherwise.
    - **rule** (ConditionalFormatRule): The rule that should replace the rule at the given index.
    - **newIndex** (int): The zero-based new index the rule should end up at.
    
`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#updateconditionalformatrulerequest>`_
"""

################################################################################
class DeleteConditionalFormatRuleRequest(TypedDict):
    """Deletes a conditional format rule at the given index.

    Members:
        - **index** (int): The zero-based index of the rule to delete.
        - **sheetId** (int): The sheet the rule is being deleted from.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#deleteconditionalformatrulerequest>`_
    """
    index: int
    sheetId: int

################################################################################
class SortRangeRequest(TypedDict):
    """Sorts a range of cells.

    Members:
        - **range** (GridRange): The range to sort.
        - **sortSpecs** (List[SortSpec]): The sort order per column. Later specifications are used when values are equal in the earlier specifications.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#sortrangerequest>`_
    """
    range: GridRange
    sortSpecs: List[SortSpec]

################################################################################
class SetDataValidationRequest(TypedDict):
    """Sets data validation for one or more cells.

    Members:
        - **range** (GridRange): The range the data validation rule should apply to.
        - **rule** (DataValidationRule): The data validation rule to set on each cell in the range, or empty to clear the data validation in the range.
        - **filteredRowsIncluded** (bool): Optional. True if the data validation rule should apply to filtered rows.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#setdatavalidationrequest>`_
    """
    range: GridRange
    rule: DataValidationRule
    filteredRowsIncluded: NotRequired[bool]

################################################################################
class SetBasicFilterRequest(TypedDict):
    """Sets the basic filter on a sheet.

    Members:
        - **filter** (BasicFilter): The filter to set.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#setbasicfilterrequest>`_
    """
    filter: BasicFilter

################################################################################
class AddProtectedRangeRequest(TypedDict):
    """Adds a new protected range.

    Members:
        - **protectedRange** (ProtectedRange): The protected range to add. The ``protectedRangeId`` field is optional; if one is not set, an id will be randomly generated.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#addprotectedrangerequest>`_
    """
    protectedRange: ProtectedRange

################################################################################
class UpdateProtectedRangeRequest(TypedDict):
    """Updates a protected range.

    Members:
        - **protectedRange** (ProtectedRange): The protected range to update with the new properties.
        - **fields** (str): The fields that should be updated. At least one field must be specified. The root ``protectedRange`` is implied and should not be specified. A single ``*`` can be used as shorthand for listing every field.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#updateprotectedrangerequest>`_
    """
    protectedRange: ProtectedRange
    fields: str

################################################################################
class DeleteProtectedRangeRequest(TypedDict):
    """Deletes a protected range.

    Members:
        - **protectedRangeId** (int): The ID of the protected range to delete.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#deleteprotectedrangerequest>`_
    """
    protectedRangeId: int

################################################################################
class _AutoResizeDimensionsRequest(TypedDict):
    dimensions: DimensionRange
    dataSourceSheetDimensions: NotRequired[None]

class _AutoResizeDataSourceSheetDimensionsRequest(TypedDict):
    dimensions: NotRequired[None]
    dataSourceSheetDimensions: DataSourceSheetDimensionRange

AutoResizeDimensionsRequest = Union[
    _AutoResizeDimensionsRequest,
    _AutoResizeDataSourceSheetDimensionsRequest
]
"""Automatically resizes one or more dimensions based on the contents of the 
cells in that dimension.

Members:
    - **dimensions** (DimensionRange): The dimensions to automatically resize.
    - **dataSourceSheetDimensions** (DataSourceSheetDimensionRange): The columns on a data source sheet to automatically resize.
    
`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#autoresizedimensionsrequest>`_
"""

################################################################################
class AddChartRequest(TypedDict):
    """Adds a chart to a sheet.

    Members:
        - **chart** (EmbeddedChart): The chart to add. The ``chartId`` field is optional; if one is not set, an id will be randomly generated.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#addchartrequest>`_
    """
    chart: EmbeddedChart

################################################################################
class UpdateChartSpecRequest(TypedDict):
    """Updates the specifications of a chart.

    Members:
        - **chartId** (int): The ID of the chart to update.
        - **spec** (ChartSpec): The specification to apply to the chart.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#updatechartspecrequest>`_
    """
    chartId: int
    spec: ChartSpec

################################################################################
class UpdateBandingRequest(TypedDict):
    """Updates the banded range with new properties.

    Members:
        - **bandedRange** (BandedRange): The banded range to update with the new properties.
        - **fields** (str): The fields that should be updated. At least one field must be specified. The root ``bandedRange`` is implied and should not be specified. A single ``"*"`` can be used as shorthand for listing every field.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#updatebandingrequest>`_
    """
    bandedRange: BandedRange
    fields: str

################################################################################
class AddBandingRequest(TypedDict):
    """Adds a new banded range.

    Members:
        - **bandedRange** (BandedRange): The banded range to add. The ``bandedRangeId`` field is optional; if one is not set, an id will be randomly generated.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#addbandingrequest>`_
    """
    bandedRange: BandedRange

################################################################################
class DeleteBandingRequest(TypedDict):
    """Removes the banded range with the given ID from the spreadsheet.

    Members:
        - **bandedRangeId** (int): The ID of the banded range to delete.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#deletebandingrequest>`_
    """
    bandedRangeId: int

################################################################################
class CreateDeveloperMetadataRequest(TypedDict):
    """Creates a new developer metadata entry.

    Members:
        - **developerMetadata** (DeveloperMetadata): The developer metadata to create.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#createdevelopermetadatarequest>`_
    """
    developerMetadata: DeveloperMetadata

################################################################################
class UpdateDeveloperMetadataRequest(TypedDict):
    """Updates an existing developer metadata entry.

    Members:
        - **dataFilters** (List[DataFilter]): The filters matching the developer metadata entries to update.
        - **developerMetadata** (DeveloperMetadata): The value that all metadata matched by the data filters will be updated to.
        - **fields** (str): The fields that should be updated. At least one field must be specified. The root ``developerMetadata`` is implied and should not be specified. A single ``"*"`` can be used as shorthand for listing every field.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#updatedevelopermetadatarequest>`_
    """
    dataFilters: List[DataFilter]
    developerMetadata: DeveloperMetadata
    fields: str

################################################################################
class DeleteDeveloperMetadataRequest(TypedDict):
    """A request to delete developer metadata.

    Members:
        - **dataFilters** (List[DataFilter]): The data filter describing the criteria used to select which developer metadata entry to delete.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#deletedevelopermetadatarequest>`_
    """
    dataFilter: DataFilter

################################################################################
class RandomizeRangeRequest(TypedDict):
    """Randomizes the order of the rows or columns in a range.

    Members:
        - **range** (GridRange): The range to randomize.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#randomizerangerequest>`_
    """
    range: GridRange

################################################################################
class AddDimensionGroupRequest(TypedDict):
    """Adds a group to the specified dimensions.

    Members:
        - **range** (DimensionRange): The range over which to create a group.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#adddimensiongrouprequest>`_
    """
    range: DimensionRange

################################################################################
class DeleteDimensionGroupRequest(TypedDict):
    """Deletes a group over the specified range by decrementing the depth of
    the dimensions in the range.

    Members:
        - **range** (DimensionRange): The range of the group to be deleted.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#deletedimensiongrouprequest>`_
    """
    range: DimensionRange

################################################################################
class UpdateDimensionGroupRequest(TypedDict):
    """Updates the properties of a dimension group.

    Members:
        - **range** (DimensionGroup): The group whose state should be updated.
        - **fields** (str): The fields that should be updated. At least one field must be specified. The root ``range`` is implied and should not be specified. A single ``"*"`` can be used as shorthand for listing every field.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#updatedimensiongrouprequest>`_
    """
    range: DimensionGroup
    fields: str

################################################################################
class TrimWhiteSpaceRequest(TypedDict):
    """Trims the whitespace (such as spaces, tabs, or new lines) in every cell
    in the specified range.

    This request removes all whitespace from the start and end of each cell's
    text, and reduces any subsequence of remaining whitespace characters to a
    single space. If the resulting trimmed text starts with a '+' or '=' character,
    the text remains as a string value and isn't interpreted as a formula.

    Members:
        - **range** (GridRange): The range whose cells to trim whitespace from.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#trimwhitespacerequest>`_
    """
    range: GridRange

################################################################################
class DeleteDuplicatesRequest(TypedDict):
    """Deletes rows containing duplicate values in the specified range.

    Members:
        - **range** (GridRange): The range in which to find duplicate values.
        - **comparisonColumns** (List[DimensionRange]): The columns within the range to analyze for duplicate values. If no columns are selected then all columns are analyzed for duplicates.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#deleteduplicatesrequest>`_
    """
    range: GridRange
    comparisonColumns: List[DimensionRange]

################################################################################
class UpdateEmbeddedObjectBorderRequest(TypedDict):
    """Updates the border of an embedded object in a sheet.

    Members:
        - **objectId** (int): The ID of the embedded object to update.
        - **border** (EmbeddedObjectBorder): The border to set on the embedded object.
        - **fields** (str): The fields of ``EmbeddedObjectBorder`` that should be updated when setting a new border. At least one field must be specified. The root ``border`` is implied and should not be specified. A single ``"*"`` can be used as shorthand for listing every field.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#updateembeddedobjectborderrequest>`_
    """
    objectId: int
    border: EmbeddedObjectBorder
    fields: str

################################################################################
class AddSlicerRequest(TypedDict):
    """Adds a slicer to a sheet.

    Members:
        - **slicer** (Slicer): The slicer to add. The ``slicerId`` field is optional; if one is not set, an id will be randomly generated.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#addslicerrequest>`_
    """
    slicer: Slicer

################################################################################
class UpdateSlicerSpecRequest(TypedDict):
    """Updates the specifications of a slicer.

    Members:
        - **slicerId** (int): The ID of the slicer to update.
        - **spec** (SlicerSpec): The specification to apply to the slicer.
        - **fields** (str): The fields that should be updated. At least one field must be specified. The root ``spec`` is implied and should not be specified. A single ``"*"`` can be used as shorthand for listing every field.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#updateslicerspecrequest>`_
    """
    slicerId: int
    spec: SlicerSpec
    fields: str

################################################################################
class AddDataSourceRequest(TypedDict):
    """Adds a data source to a spreadsheet.

    Members:
        - **dataSource** (DataSource): The data source to add.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#adddatasourcerequest>`_
    """
    dataSource: DataSource

################################################################################
class UpdateDataSourceRequest(TypedDict):
    """Updates a data source in a spreadsheet.

    After the data source is updated successfully, an execution is triggered to
    refresh the associated ``DATA_SOURCE`` sheet to read data from the updated
    data source.

    Members:
        - **dataSource** (DataSource): The data source to update.
        - **fields** (str): The fields that should be updated. At least one field must be specified. The root ``dataSource`` is implied and should not be specified. A single ``"*"`` can be used as shorthand for listing every field.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#updatedatasourcerequest>`_
    """
    dataSource: DataSource
    fields: str

################################################################################
class DeleteDataSourceRequest(TypedDict):
    """Deletes a data source from a spreadsheet.

    Members:
        - **dataSourceId** (str): The ID of the data source to delete.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#deletedatasourcerequest>`_
    """
    dataSourceId: str

################################################################################
class _RefreshDataSourceRequestBase(TypedDict, total=False):
    force: bool

class _RefreshDataSourceRequestWithRefs(_RefreshDataSourceRequestBase):
    references: DataSourceObjectReferences
    dataSourceId: NotRequired[None]
    isAll: NotRequired[None]

class _RefreshDataSourceRequestWithId(_RefreshDataSourceRequestBase):
    references: NotRequired[None]
    dataSourceId: str
    isAll: NotRequired[None]

class _RefreshDataSourceRequestWithAll(_RefreshDataSourceRequestBase):
    references: NotRequired[None]
    dataSourceId: NotRequired[None]
    isAll: bool

RefreshDataSourceRequest = Union[
    _RefreshDataSourceRequestWithRefs,
    _RefreshDataSourceRequestWithId,
    _RefreshDataSourceRequestWithAll
]
"""Refreshes one or multiple data source objects in the spreadsheet by the specified references.

Members:
    - **force** (bool): Refreshes the data source objects regardless of the current state.
    - **references** (List[DataSourceObjectReferences]): The references to the data source objects to refresh.
    - **dataSourceId** (str): The ID of the data source to refresh.
    - **isAll** (bool): True to refresh all existing data source objects in the spreadsheet.
    
`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#refreshdatasourcerequest>`_
"""

################################################################################
class DataSourceObjectReferences(TypedDict):
    """References to a data source object in the spreadsheet.

    Members:
        - **references** (List[DataSourceObjectReference]): The references to the data source objects.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#datasourceobjectreferences>`_
    """
    references: List[DataSourceObjectReference]

################################################################################
class _DataSourceObjectReferenceWithSheetId(TypedDict):
    sheetId: int
    chartId: NotRequired[None]
    dataSourceTableAnchorCell: NotRequired[None]
    dataSourcePivotTableAnchorCell: NotRequired[None]
    dataSourceFormulaCell: NotRequired[None]

class _DataSourceObjectReferenceWithChartId(TypedDict):
    sheetId: NotRequired[None]
    chartId: int
    dataSourceTableAnchorCell: NotRequired[None]
    dataSourcePivotTableAnchorCell: NotRequired[None]
    dataSourceFormulaCell: NotRequired[None]

class _DataSourceObjectReferenceWithTableAnchorCell(TypedDict):
    sheetId: NotRequired[None]
    chartId: NotRequired[None]
    dataSourceTableAnchorCell: GridCoordinate
    dataSourcePivotTableAnchorCell: NotRequired[None]
    dataSourceFormulaCell: NotRequired[None]

class _DataSourceObjectReferenceWithPivotTableAnchorCell(TypedDict):
    sheetId: NotRequired[None]
    chartId: NotRequired[None]
    dataSourceTableAnchorCell: NotRequired[None]
    dataSourcePivotTableAnchorCell: GridCoordinate
    dataSourceFormulaCell: NotRequired[None]

class _DataSourceObjectReferenceWithFormulaCell(TypedDict):
    sheetId: NotRequired[None]
    chartId: NotRequired[None]
    dataSourceTableAnchorCell: NotRequired[None]
    dataSourcePivotTableAnchorCell: NotRequired[None]
    dataSourceFormulaCell: GridCoordinate

DataSourceObjectReference = Union[
    _DataSourceObjectReferenceWithSheetId,
    _DataSourceObjectReferenceWithChartId,
    _DataSourceObjectReferenceWithTableAnchorCell,
    _DataSourceObjectReferenceWithPivotTableAnchorCell,
    _DataSourceObjectReferenceWithFormulaCell
]
"""Reference to a data source object.

Members:
    - **sheetId** (int): A references to a ``DATA_SOURCE`` sheet.
    - **chartId** (int): The chart ID of the data source object.
    - **dataSourceTableAnchorCell** (GridCoordinate): Reference to a ``DataSourceTable`` anchored at the cell.
    - **dataSourcePivotTableAnchorCell** (GridCoordinate): Reference to a data source ``PivotTable`` anchored at the cell.
    - **dataSourceFormulaCell** (GridCoordinate): Reference to a cell containing ``DataSourceFormula``.
    
`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#datasourceobjectreference>`_
"""

################################################################################
class _CancelDataSourceRefreshRequestWithRefs(TypedDict):
    references: DataSourceObjectReferences
    dataSourceId: NotRequired[None]
    isAll: NotRequired[None]

class _CancelDataSourceRefreshRequestWithDataSource(TypedDict):
    references: NotRequired[None]
    dataSourceId: str
    isAll: NotRequired[None]

class _CancelDataSourceRefreshRequestWithAll(TypedDict):
    references: NotRequired[None]
    dataSourceId: NotRequired[None]
    isAll: bool

CancelDataSourceRefreshRequest = Union[
    _CancelDataSourceRefreshRequestWithRefs,
    _CancelDataSourceRefreshRequestWithDataSource,
    _CancelDataSourceRefreshRequestWithAll
]
"""Cancels one or multiple refreshes of data source objects in the spreadsheet 
by the specified references.

Members:
    - **references** (List[DataSourceObjectReferences]): References to data source objects whose refreshes are to be cancelled.
    - **dataSourceId** (str): Reference to a ``DataSource``. If specified, cancels all associated data source object refreshes for this data source.
    - **isAll** (bool): Cancels all existing data source object refreshes for all data sources in the spreadsheet.
    
`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#canceldatasourcerefreshrequest>`_
"""

################################################################################
class AddTableRequest(TypedDict):
    """Adds a data source table to a sheet.

    Members:
        - **table** (Table): The table to add.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#addtablerequest>`_
    """
    table: Table

################################################################################
class UpdateTableRequest(TypedDict):
    """Updates a data source table in a sheet.

    Members:
        - **table** (Table): The table to update.
        - **fields** (str): The fields that should be updated. At least one field must be specified. The root ``table`` is implied and should not be specified. A single ``"*"`` can be used as shorthand for listing every field.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#updatetablerequest>`_
    """
    table: Table
    fields: str

################################################################################
class DeleteTableRequest(TypedDict):
    """Deletes a data source table from a sheet.

    Members:
        - **tableId** (int): The ID of the table to delete.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#deletetablerequest>`_
    """
    tableId: int

################################################################################
