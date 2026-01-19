from __future__ import annotations

from typing import TYPE_CHECKING, TypedDict, Union, NotRequired, List

from ..Enums import *

if TYPE_CHECKING:
    from .Requests import DataSourceObjectReference
    from ..DeveloperMetadata import DeveloperMetadata
    from ..Other import EmbeddedObjectPosition, DataExecutionStatus
    from ..Sheets import (
        SheetProperties, FilterView, ConditionalFormatRule, ProtectedRange,
        BandedRange, DimensionGroup, Slicer, Table
    )
    from ..Spreadsheets import NamedRange, DataSource
################################################################################
class _ResponseAddNamedRange(TypedDict):
    addNamedRange: AddNamedRangeResponse

class _ResponseAddSheet(TypedDict):
    addSheet: AddSheetResponse

class _ResponseAddFilterView(TypedDict):
    addFilterView: AddFilterViewResponse

class _ResponseDuplicateFilterView(TypedDict):
    duplicateFilterView: DuplicateFilterViewResponse

class _ResponseDuplicateSheet(TypedDict):
    duplicateSheet: DuplicateSheetResponse

class _ResponseFindReplace(TypedDict):
    findReplace: FindReplaceResponse

class _ResponseUpdateEmbeddedObjectPosition(TypedDict):
    updateEmbeddedObjectPosition: UpdateEmbeddedObjectPositionResponse

class _ResponseUpdateConditionalFormatRule(TypedDict):
    updateConditionalFormatRule: UpdateConditionalFormatRuleResponse

class _ResponseDeleteConditionalFormatRule(TypedDict):
    deleteConditionalFormatRule: DeleteConditionalFormatRuleResponse

class _ResponseAddProtectedRange(TypedDict):
    addProtectedRange: AddProtectedRangeResponse

class _ResponseAddChart(TypedDict):
    addChart: AddChartResponse

class _ResponseAddBanding(TypedDict):
    addBanding: AddBandingResponse

class _ResponseCreateDeveloperMetadata(TypedDict):
    createDeveloperMetadata: CreateDeveloperMetadataResponse

class _ResponseUpdateDeveloperMetadata(TypedDict):
    updateDeveloperMetadata: UpdateDeveloperMetadataResponse

class _ResponseDeleteDeveloperMetadata(TypedDict):
    deleteDeveloperMetadata: DeleteDeveloperMetadataResponse

class _ResponseAddDimensionGroup(TypedDict):
    addDimensionGroup: AddDimensionGroupResponse

class _ResponseDeleteDimensionGroup(TypedDict):
    deleteDimensionGroup: DeleteDimensionGroupResponse

class _ResponseTrimWhitespace(TypedDict):
    trimWhitespace: TrimWhitespaceResponse

class _ResponseDeleteDuplicates(TypedDict):
    deleteDuplicates: DeleteDuplicatesResponse

class _ResponseAddSlicer(TypedDict):
    addSlice: AddSlicerResponse

class _ResponseAddDataSource(TypedDict):
    addDataSource: AddDataSourceResponse

class _ResponseUpdateDataSource(TypedDict):
    updateDataSource: UpdateDataSourceResponse

class _ResponseRefreshDataSource(TypedDict):
    refreshDataSource: RefreshDataSourceResponse

class _ResponseCancelDataSourceRefresh(TypedDict):
    cancelDataSourceRefresh: CancelDataSourceRefreshResponse

class _ResponseAddTable(TypedDict):
    addTable: AddTableResponse

SpreadsheetBatchUpdateResponse = Union[
    _ResponseAddNamedRange,
    _ResponseAddSheet,
    _ResponseAddFilterView,
    _ResponseDuplicateFilterView,
    _ResponseDuplicateSheet,
    _ResponseFindReplace,
    _ResponseUpdateEmbeddedObjectPosition,
    _ResponseUpdateConditionalFormatRule,
    _ResponseDeleteConditionalFormatRule,
    _ResponseAddProtectedRange,
    _ResponseAddChart,
    _ResponseAddBanding,
    _ResponseCreateDeveloperMetadata,
    _ResponseUpdateDeveloperMetadata,
    _ResponseDeleteDeveloperMetadata,
    _ResponseAddDimensionGroup,
    _ResponseDeleteDimensionGroup,
    _ResponseTrimWhitespace,
    _ResponseDeleteDuplicates,
    _ResponseAddSlicer,
    _ResponseAddDataSource,
    _ResponseUpdateDataSource,
    _ResponseRefreshDataSource,
    _ResponseCancelDataSourceRefresh,
    _ResponseAddTable
]
"""A single response from an update.

`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response>`_
"""

################################################################################
class AddNamedRangeResponse(TypedDict):
    """The result of adding a named range.

    Members:
        - **namedRange** (NamedRange): The named range that was added.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#addnamedrangeresponse>`_
    """
    namedRange: NamedRange

################################################################################
class AddSheetResponse(TypedDict):
    """The result of adding a sheet.

    Members:
        - **properties** (SheetProperties): The properties of the sheet that was added.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#addsheetresponse>`_
    """
    properties: SheetProperties

################################################################################
class AddFilterViewResponse(TypedDict):
    """The result of adding a filter view.

    Members:
        - **filter** (FilterView): The filter view that was added.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#addfilterviewresponse>`_
    """
    filter: FilterView

################################################################################
class DuplicateFilterViewResponse(TypedDict):
    """The result of duplicating a filter view.

    Members:
        - **filter** (FilterView): The newly created filter view.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#duplicatefilterviewresponse>`_
    """
    filter: FilterView

################################################################################
class DuplicateSheetResponse(TypedDict):
    """The result of duplicating a sheet.

    Members:
        - **properties** (SheetProperties): The properties of the duplicated sheet.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#duplicatesheetresponse>`_
    """
    properties: SheetProperties

################################################################################
class FindReplaceResponse(TypedDict):
    """The result of a find/replace request.

    Members:
        - **valuesChanged** (int): The number of non-formula cells changed.
        - **formulasChanged** (int): The number of formulas cells changed.
        - **rowsChanged** (int): The number of rows changed.
        - **sheetsChanged** (int): The number of sheets changed.
        - **occurrencesChanged** (int): The number of occurrences (possibly multiple within a cell) changed.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#findreplaceresponse>`_
    """
    valuesChanged: int
    formulasChanged: int
    rowsChanged: int
    sheetsChanged: int
    occurrencesChanged: int

################################################################################
class UpdateEmbeddedObjectPositionResponse(TypedDict):
    """The result of updating an embedded object's position.

    Members:
        - **position** (EmbeddedObjectPosition): The new position of the embedded object.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#updateembeddedobjectpositionresponse>`_
    """
    position: EmbeddedObjectPosition

################################################################################
class _UpdateConditionalFormatRuleResponseBase(TypedDict, total=False):
    newRule: ConditionalFormatRule
    newIndex: int

class _UpdateConditionalFormatRuleResponseWithRule(_UpdateConditionalFormatRuleResponseBase):
    oldRule: ConditionalFormatRule
    oldIndex: NotRequired[None]

class _UpdateConditionalFormatRuleResponseWithIndex(_UpdateConditionalFormatRuleResponseBase):
    oldRule: NotRequired[None]
    oldIndex: int

UpdateConditionalFormatRuleResponse = Union[
    _UpdateConditionalFormatRuleResponseWithRule,
    _UpdateConditionalFormatRuleResponseWithIndex
]
"""The result of updating a conditional format rule.

Members:
    - **newRule** (ConditionalFormatRule): The new rule that replaced the old rule (if replacing), or the rule that was moved (if moved)
    - **newIndex** (int): The index of the new rule.
    - **oldRule** (ConditionalFormatRule): The old (deleted) rule. Not set if a rule was moved (because it is the same as ``newRule``).
    - **oldIndex** (int): The old index of the rule. Not set if a rule was replaced (because it is the same as ``newIndex``).

`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#updateconditionalformatruleresponse>`_
"""

################################################################################
class DeleteConditionalFormatRuleResponse(TypedDict):
    """The result of deleting a conditional format rule.

    Members:
        - **rule** (ConditionalFormatRule): The rule that was deleted.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#deleteconditionalformatruleresponse>`_
    """
    rule: ConditionalFormatRule

################################################################################
class AddProtectedRangeResponse(TypedDict):
    """The result of adding a protected range.

    Members:
        - **protectedRange** (ProtectedRange): The protected range that was added.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#addprotectedrangeresponse>`_
    """
    protectedRange: ProtectedRange

################################################################################
class AddChartResponse(TypedDict):
    """The result of adding a chart.

    Members:
        - **chart** (EmbeddedChart): The chart that was added.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#addchartresponse>`_
    """
    chart: EmbeddedChart

################################################################################
class AddBandingResponse(TypedDict):
    """The result of adding banded ranges.

    Members:
        - **bandedRange** (BandedRange): The banded range that was added.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#addbandingresponse>`_
    """
    bandedRange: BandedRange

################################################################################
class CreateDeveloperMetadataResponse(TypedDict):
    """The result of creating developer metadata.

    Members:
        - **developerMetadata** (DeveloperMetadata): The developer metadata that was created.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#createdevelopermetadataresponse>`_
    """
    developerMetadata: DeveloperMetadata

################################################################################
class UpdateDeveloperMetadataResponse(TypedDict):
    """The result of updating developer metadata.

    Members:
        - **developerMetadata** (List[DeveloperMetadata]): The developer metadata that was updated.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#updatedevelopermetadataresponse>`_
    """
    developerMetadata: List[DeveloperMetadata]

################################################################################
class DeleteDeveloperMetadataResponse(TypedDict):
    """The result of deleting developer metadata.

    Members:
        - **developerMetadata** (List[DeveloperMetadata]): The developer metadata that was deleted.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#deletedevelopermetadataresponse>`_
    """
    developerMetadata: List[DeveloperMetadata]

################################################################################
class AddDimensionGroupResponse(TypedDict):
    """The result of adding a dimension group.

    Members:
        - **dimensionGroup** (List[DimensionGroup]): All groups of a dimension after adding a group to that dimension.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#adddimensiongroupresponse>`_
    """
    dimensionGroups: List[DimensionGroup]

################################################################################
class DeleteDimensionGroupResponse(TypedDict):
    """The result of deleting a dimension group.

    Members:
        - **dimensionGroup** (List[DimensionGroup]): All groups of a dimension after deleting a group from that dimension.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#deletedimensiongroupresponse>`_
    """
    dimensionGroups: List[DimensionGroup]

################################################################################
class TrimWhitespaceResponse(TypedDict):
    """The result of trimming whitespace.

    Members:
        - **cellsChangedCount** (int): The number of cells that were trimmed of whitespace.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#trimwhitespaceresponse>`_
    """
    cellsChangedCount: int

################################################################################
class DeleteDuplicatesResponse(TypedDict):
    """The result of deleting duplicates.

    Members:
        - **duplicatesRemovedCount** (int): The number of duplicate rows removed.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#deleteduplicatesresponse>`_
    """
    duplicatesRemovedCount: int

################################################################################
class AddSlicerResponse(TypedDict):
    """The result of adding a slicer.

    Members:
        - **slicer** (Slicer): The slicer that was added.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#addslicerresponse>`_
    """
    slicer: Slicer

################################################################################
class AddDataSourceResponse(TypedDict):
    """The result of adding a data source.

    Members:
        - **dataSource** (DataSource): The data source that was added.
        - **dataExecutionStatus** (DataExecutionStatus): The status of the most recent data execution.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#adddatasourceresponse>`_
    """
    dataSource: DataSource
    dataExecutionStatus: DataExecutionStatus

################################################################################
class UpdateDataSourceResponse(TypedDict):
    """The result of updating a data source.

    Members:
        - **dataSource** (DataSource): The data source that was updated.
        - **dataExecutionStatus** (DataExecutionStatus): The status of the most recent data execution.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#updatedatasourceresponse>`_
    """
    dataSource: DataSource
    dataExecutionStatus: DataExecutionStatus

################################################################################
class RefreshDataSourceResponse(TypedDict):
    """The result of refreshing a data source.

    Members:
        - **statuses** (List[RefreshDataSourceObjectExecutionStatus]): All the refresh status for the data source object references specified in the request. If ``isAll`` is specified, the field contains only those in failure status.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#refreshdatasourceresponse>`_
    """
    statuses: List[RefreshDataSourceObjectExecutionStatus]

################################################################################
class RefreshDataSourceObjectExecutionStatus(TypedDict):
    """The execution status of a data source object during a refresh.

    Members:
        - **reference** (DataSourceObjectReference): Reference to a data source object being refreshed.
        - **dataExecutionStatus** (DataExecutionStatus): The status of the data execution for this object.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#refreshdatasourceobjectexecutionstatus>`_
    """
    reference: DataSourceObjectReference
    dataExecutionStatus: DataExecutionStatus

################################################################################
class CancelDataSourceRefreshResponse(TypedDict):
    """The result of canceling a data source refresh.

    Members:
        - **statuses** (List[CancelDataSourceRefreshStatus]): All the cancel status for the data source object references specified in the request.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#canceldatasourcerefreshresponse>`_
    """
    statuses: List[CancelDataSourceRefreshStatus]

################################################################################
class CancelDataSourceRefreshStatus(TypedDict):
    """The cancel status of a data source object during a cancel refresh.

    Members:
        - **reference** (DataSourceObjectReference): Reference to a data source object being canceled.
        - **refreshCancellationStatus** (RefreshCancellationStatus): The status of the refresh cancellation for this object.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#canceldatasourcerefreshstatus>`_
    """
    reference: DataSourceObjectReference
    refreshCancellationStatus: RefreshCancellationStatus

################################################################################
class RefreshCancellationStatus(TypedDict):
    """The status of a refresh cancellation.

    Members:
        - **state** (RefreshCancellationState): The state of a call to cancel a refresh in Sheets.
        - **errorCode** (RefreshCancellationErrorCode): The error code for the refresh cancellation.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#refreshcancellationstatus>`_
    """
    state: RefreshCancellationState
    errorCode: RefreshCancellationErrorCode

################################################################################
class AddTableResponse(TypedDict):
    """The result of adding a table.

    Members:
        - **table** (Table): The table that was added.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/response#addtableresponse>`_
    """
    table: Table

################################################################################
