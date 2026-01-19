from __future__ import annotations

from typing import TYPE_CHECKING, TypedDict, Union, NotRequired, List

from .Enums import *

if TYPE_CHECKING:
    from .Charts import EmbeddedChart
    from .Other import (
        ColorStyle, GridRange, DataSourceColumn, DataSourceColumnReference,
        EmbeddedObjectPosition, DataExecutionStatus,
        BooleanCondition, SortSpec, FilterSpec, FilterCriteria
    )
    from .Cells import CellData, TextFormat, CellFormat
    from .Misc import DimensionRange
    from .DeveloperMetadata import DeveloperMetadata
################################################################################
class Sheet(TypedDict):
    """A sheet in a spreadsheet.

    Members:
        - **properties** (SheetProperties): The properties of the sheet.
        - **data** (List[GridData]): Data in the grid, if this is a grid sheet.
        - **merges** (List[GridRange]): The ranges that are merged together.
        - **conditionalFormats** (List[ConditionalFormatRule]): The conditional format rules in the sheet.
        - **filterViews** (List[FilterView]): The filter views in the sheet.
        - **protectedRanges** (List[ProtectedRange]): The protected ranges in the sheet.
        - **basicFilter** (BasicFilter): The filter on this sheet, if any.
        - **charts** (List[EmbeddedChart]): The specifications of every chart on this sheet.
        - **bandedRanges** (List[BandedRange]): The banded (alternating colors) ranges on this sheet.
        - **developerMetadata** (List[DeveloperMetadata]): The developer metadata associated with a sheet.
        - **rowGroups** (List[DimensionGroup]): All row groups on this sheet, ordered by increasing range start index, then by group depth.
        - **columnGroups** (List[DimensionGroup]): All column groups on this sheet, ordered by increasing range start index, then by group depth.
        - **slicers** (List[Slicer]): The slicers in the sheet.
        - **tables** (List[Table]): The tables in the sheet.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/sheets#sheet>`_
    """
    properties: SheetProperties
    data: List[GridData]
    merges: List[GridRange]
    conditionalFormats: List[ConditionalFormatRule]
    filterViews: List[FilterView]
    protectedRanges: List[ProtectedRange]
    basicFilter: BasicFilter
    charts: List[EmbeddedChart]
    bandedRanges: List[BandedRange]
    developerMetadata: List[DeveloperMetadata]
    rowGroups: List[DimensionGroup]
    columnGroups: List[DimensionGroup]
    slicers: List[Slicer]
    tables: List[Table]

################################################################################
class SheetProperties(TypedDict):
    """Properties of a sheet.

    Members:
        - **sheetId** (int): The ID of the sheet. Must be non-negative. This field cannot be changed once set.
        - **title** (str): The name of the sheet.
        - **index** (int): The index of the sheet within the spreadsheet.
        - **sheetType** (SheetType): The type of sheet. Defaults to GRID. This field cannot be changed once set.
        - **gridProperties** (GridProperties): Additional properties of the sheet if this sheet is a grid. When writing it is an error to set any grid properties on non-grid sheets.
        - **hidden** (bool): True if the sheet is hidden in the UI, false if it's visible.
        - **tabColorStyle** (ColorStyle): The color of the tab in the UI.
        - **rightToLeft** (bool): True if the sheet is an RTL sheet instead of an LTR sheet.
        - **dataSourceSheetProperties** (DataSourceSheetProperties): Output only. If present, the field contains DATA_SOURCE sheet specific properties.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/sheets#sheetproperties>`_
    """
    sheetId: int
    title: str
    index: int
    sheetType: SheetType
    gridProperties: GridProperties
    hidden: bool
    tabColorStyle: ColorStyle
    rightToLeft: bool
    dataSourceSheetProperties: DataSourceSheetProperties

################################################################################
class GridProperties(TypedDict):
    """Properties of a grid.

    Members:
        - **rowCount** (int): The number of rows in the grid.
        - **columnCount** (int): The number of columns in the grid.
        - **frozenRowCount** (int): The number of rows that are frozen in the grid.
        - **frozenColumnCount** (int): The number of columns that are frozen in the grid.
        - **hideGridlines** (bool): True if gridlines are not shown in the UI.
        - **rowGroupControlAfter** (bool): True if the row grouping control toggle is shown after the group.
        - **columnGroupControlAfter** (bool): True if the column grouping control toggle is shown after the group.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/sheets#gridproperties>`_
    """
    rowCount: int
    columnCount: int
    frozenRowCount: int
    frozenColumnCount: int
    hideGridlines: bool
    rowGroupControlAfter: bool
    columnGroupControlAfter: bool

################################################################################
class DataSourceSheetProperties(TypedDict):
    """Additional properties of a DATA_SOURCE sheet.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/sheets#datasourcesheetproperties>`_
    """
    dataSourceId: str
    columns: List[DataSourceColumn]
    dataExecutionStatus: DataExecutionStatus

################################################################################
class GridData(TypedDict):
    """Data in the grid, as well as metadata about the dimensions.

    Members:
        - **startRow** (int): The first row this ``GridData`` refers to, zero-based.
        - **startColumn** (int): The first column this ``GridData`` refers to, zero-based.
        - **rowData** (List[RowData]): The data in the grid, one entry per row, starting with the row in ``startRow``. The values in ``RowData`` will correspond to columns starting at ``startColumn``.
        - **rowMetadata** (List[DimensionProperties]): Metadata about the requested rows in the grid, starting with the row in ``startRow``.
        - **columnMetadata** (List[DimensionProperties]): Metadata about the requested columns in the grid, starting with the column in ``startColumn``.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/sheets#griddata>`_
    """
    startRow: int
    startColumn: int
    rowData: List[RowData]
    rowMetadata: List[DimensionProperties]
    columnMetadata: List[DimensionProperties]

################################################################################
class RowData(TypedDict):
    """Data about cell in a row.

    Members:
        - **values** (List[CellData]): The values in the row, one per column.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/sheets#rowdata>`_
    """
    values: List[CellData]

################################################################################
class DimensionProperties(TypedDict):
    """Properties about a dimension.

    Members:
        - **hiddenByFilter** (bool): True if this dimension is being filtered. This field is read-only.
        - **hiddenByUser** (bool): True if this dimension is explicitly hidden.
        - **pixelSize** (int): The height (if a row) or width (if a column) of the dimension in pixels.
        - **developerMetadata** (List[DeveloperMetadata]): The developer metadata associated with a single row or column.
        - **dataSourceColumnReference** (DataSourceColumnReference): Output only. If set, this is a column in a data source sheet.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/sheets#dimensionproperties>`_
    """
    hiddenByFilter: bool
    hiddenByUser: bool
    pixelSize: int
    developerMetadata: List[DeveloperMetadata]
    dataSourceColumnReference: DataSourceColumnReference

################################################################################
class _ConditionalFormatRuleBase(TypedDict, total=False):
    ranges: List[GridRange]

class _ConditionalFormatRuleBoolean(_ConditionalFormatRuleBase):
    booleanRule: BooleanRule
    gradientRule: NotRequired[None]

class _ConditionalFormatRuleGradient(_ConditionalFormatRuleBase):
    booleanRule: NotRequired[None]
    gradientRule: GradientRule

ConditionalFormatRule = Union[
    _ConditionalFormatRuleBoolean,
    _ConditionalFormatRuleGradient,
]
"""A rule describing a conditional format.

Members:
    - **ranges** (List[GridRange]): The ranges that are formatted if the condition is true. All the ranges must be on the same grid.
    - **booleanRule** (BooleanRule): The formatting is either "on" or "off" according to the rule.
    - **gradientRule** (GradientRule): The formatting will vary based on the gradients in the rule.

`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/sheets#conditionalformatrule>`_
"""

################################################################################
class BooleanRule(TypedDict):
    """A rule that may or may not match, depending on the condition.

    Members:
        - **condition** (BooleanCondition): The condition of the rule. If the condition evaluates to true, the format is applied.
        - **format** (CellFormat): The format to apply. Conditional formatting can only apply a subset of formatting: bold, italic, strikethrough, foreground color and, background color.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/sheets#booleanrule>`_
    """
    condition: BooleanCondition
    format: CellFormat

################################################################################
class GradientRule(TypedDict):
    """A rule that applies a gradient color scale format, based on the interpolation
    points listed.

    The format of a cell will vary based on its contents as compared to the values
    of the interpolation points.

    Members:
        - **minpoint** (InterpolationPoint): The starting interpolation point.
        - **midpoint** (InterpolationPoint): An optional midway interpolation point.
        - **maxpoint** (InterpolationPoint): The final interpolation point.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/sheets#gradientrule>`_
    """
    minpoint: InterpolationPoint
    midpoint: NotRequired[InterpolationPoint]
    maxpoint: InterpolationPoint

################################################################################
class InterpolationPoint(TypedDict):
    """A single interpolation point on a gradient conditional format.

    These pin the gradient color scale according to the color, type and value chosen.

    Members:
        - **colorStyle** (ColorStyle): The color this interpolation point should use.
        - **type** (InterpolationPointType): How the value should be interpreted.
        - **value** (str): The value this interpolation point uses. Might be a formula. Unused if type is MIN or MAX.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/sheets#interpolationpoint>`_
    """
    colorStyle: ColorStyle
    type: InterpolationPointType
    value: str

################################################################################
class FilterView(TypedDict):
    """A filter view.

    When writing, only one of ``range`` or ``namedRangeId`` or ``tableId`` may be set.

    Members:
        - **filterViewId** (int): The ID of the filter view.
        - **title** (str): The name of the filter view.
        - **range** (GridRange): The range the filter view covers.
        - **namedRangeId** (str): The named range this filter view is backed by, if any.
        - **tableId** (str): The table this filter view is backed by, if any.
        - **sortSpecs** (List[SortSpec]): The sort order per column. Later specifications are used when values are equal in the earlier specifications.
        - **filterSpecs** (List[FilterSpec]): The filter criteria for showing/hiding values per column.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/sheets#filterview>`_
    """
    filterViewId: int
    title: str
    range: GridRange
    namedRangeId: str
    tableId: str
    sortSpecs: List[SortSpec]
    filterSpecs: List[FilterSpec]

################################################################################
class ProtectedRange(TypedDict):
    """A protected range.

    When writing, only one of ``range`` or ``namedRangeId`` or ``tableId`` may be set.

    Members:
        - **protectedRangeId** (int): The ID of the protected range. This field is read-only.
        - **range** (GridRange): The range that is being protected. The range may be fully unbounded, in which case this is considered a protected sheet.
        - **namedRangeId** (str): The named range this protected range is backed by, if any.
        - **tableId** (str): The table this protected range is backed by, if any.
        - **description** (str): The description of this protected range.
        - **warningOnly** (bool): True if this protected range will show a warning when editing. Warning-based protection means that every user can edit data in the protected range, except editing will prompt a warning asking the user to confirm the edit.
        - **requestingUserCanEdit** (bool): True if the user who requested this protected range can edit the protected area. This field is read-only.
        - **unprotectedRanges** (List[GridRange]): The list of unprotected ranges within a protected sheet. Unprotected ranges are only supported on protected sheets.
        - **editors** (Editors): The users and groups with edit access to the protected range.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/sheets#protectedrange>`_
    """
    protectedRangeId: int
    range: GridRange
    namedRangeId: str
    tableId: str
    description: str
    warningOnly: bool
    requestingUserCanEdit: bool
    unprotectedRanges: List[GridRange]
    editors: Editors

################################################################################
class Editors(TypedDict):
    """The editors of a protected range.

    Members:
        - **users** (List[str]): The email addresses of users with edit access to the protected range.
        - **groups** (List[str]): The email addresses of groups with edit access to the protected range.
        - **domainUsersCanEdit** (bool): True if users in the domain of the spreadsheet's owner have edit access to the protected range.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/sheets#editors>`_
    """
    users: List[str]
    groups: List[str]
    domainUsersCanEdit: bool

################################################################################
class BasicFilter(TypedDict):
    """The default filter associated with a sheet.

    When writing, only one of ``range`` or ``tableId`` may be set.

    Members:
        - **range** (GridRange): The range the filter covers.
        - **tableId** (str): The table this filter is backed by, if any
        - **sortSpecs** (List[SortSpec]): The sort order per column. Later specifications are used when values are equal in the earlier specifications.
        - **filterSpecs** (List[FilterSpec]): The filter criteria for showing/hiding values per column.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/sheets#basicfilter>`_
    """
    range: GridRange
    tableId: str
    sortSpecs: List[SortSpec]
    filterSpecs: List[FilterSpec]

################################################################################
class BandedRange(TypedDict):
    """A banded (alternating colors) range in a sheet.

    At least one of ``rowProperties`` or ``columnProperties`` must be specified.

    Members:
        - **bandedRangeId** (int): The ID of the banded range. If unset, refer to bandedRangeReference.
        - **bandedRangeReference** (str): Output only. The reference of the banded range, used to identify the ID that is not supported by the bandedRangeId.
        - **range** (GridRange): The range over which the banded range applies.
        - **rowProperties** (BandingProperties): Properties for row bands. These properties are applied on a row-by-row basis throughout all the rows in the range.
        - **columnProperties** (BandingProperties): Properties for column bands. These properties are applied on a column- by-column basis throughout all the columns in the range.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/sheets#bandedrange>`_
    """
    bandedRangeId: int
    bandedRangeReference: str
    range: GridRange
    rowProperties: BandingProperties
    columnProperties: BandingProperties

################################################################################
class BandingProperties(TypedDict):
    """Properties referring a single dimension (either row or column).

    If both ``row_properties`` and ``column_properties`` are set, the fill colors
    are applied to cells according to the following rules:

        - ``headerColor`` and ``footerColor`` take priority over band colors.
        - ``firstBandColor`` takes priority over ``secondBandColor``.
        - ``rowProperties`` takes priority over ``columnProperties``.

    For example, the first row color takes priority over the first column color,
    but the first column color takes priority over the second row color. Similarly,
    the row header takes priority over the column header in the top left cell, but
    the column header takes priority over the first row color if the row header is not set.

    Members:
        - **headerColorStyle** (ColorStyle): The color of the header row or column.
        - **firstBandColorStyle** (ColorStyle): The first color that is alternating. (Required)
        - **secondBandColorStyle** (ColorStyle): The second color that is alternating. (Required)
        - **footerColorStyle** (ColorStyle): The color of the last row or column.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/sheets#bandingproperties>`_
    """
    headerColorStyle: ColorStyle
    firstBandColorStyle: ColorStyle
    secondBandColorStyle: ColorStyle
    footerColorStyle: ColorStyle

################################################################################
class DimensionGroup(TypedDict):
    """A group over an interval of rows or columns on a sheet, which can contain
    or be contained within other groups.

    A group can be collapsed or expanded as a unit on the sheet.

    Members:
        - **range** (DimensionRange): The range over which this group exists.
        - **depth** (int): The depth of the group, representing how many groups have a range that wholly contains the range of this group.
        - **collapsed** (bool): This field is true if this group is collapsed. A collapsed group remains collapsed if an overlapping group at a shallower depth is expanded.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/sheets#dimensiongroup>`_
    """
    range: DimensionRange
    depth: int
    collapsed: bool

################################################################################
class Slicer(TypedDict):
    """A slicer in a sheet.

    Members:
        - **slicerId** (int): The ID of the slicer.
        - **spec** (SlicerSpec): The specifications of the slicer.
        - **position** (EmbeddedObjectPosition): The position of the slicer.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/sheets#slicer>`_
    """
    slicerId: int
    spec: SlicerSpec
    position: EmbeddedObjectPosition

################################################################################
class SlicerSpec(TypedDict):
    """The specifications of a slicer.

    Members:
        - **dataRange** (GridRange): The data range of the slicer.
        - **filterCriteria** (FilterCriteria): The filtering criteria of the slicer.
        - **columnIndex** (int): The zero-based column index in the data table on which the filter is applied to.
        - **applyToPivotTables** (bool): True if the filter should apply to pivot tables. If not set, defaults to True.
        - **title** (str): The title of the slicer.
        - **textFormat** (TextFormat): The text format of title in the slicer. The link field is not supported.
        - **backgroundColorStyle** (ColorStyle): The background color of the slicer.
        - **horizontalAlignment** (HorizontalAlignment): The horizontal alignment of the title in the slicer. Defaults to ``LEFT``.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/sheets#slicerspec>`_
    """
    dataRange: GridRange
    filterCriteria: FilterCriteria
    columnIndex: int
    applyToPivotTables: bool
    title: str
    textFormat: TextFormat
    backgroundColorStyle: ColorStyle
    horizontalAlignment: HorizontalAlign

################################################################################
class Table(TypedDict):
    """A table.

    Members:
        - **tableId** (str): The id of the table.
        - **name** (str): The table name. This is unique to all tables in the same spreadsheet.
        - **range** (GridRange): The range the table covers.
        - **rowsProperties** (TableRowsProperties): Properties of the rows in the table.
        - **columnProperties** (List[TableColumnProperties]): Properties of the columns in the table.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/sheets#table>`_
    """
    tableId: str
    name: str
    range: GridRange
    rowsProperties: TableRowsProperties
    columnProperties: List[TableColumnProperties]

################################################################################
class TableRowsProperties(TypedDict):
    """Properties of the rows in a table.

    Members:
        - **headerColorStyle** (ColorStyle): The color of the header row.
        - **firstBandColorStyle** (ColorStyle): The first color that is alternating.
        - **secondBandColorStyle** (ColorStyle): The second color that is alternating.
        - **footerColorStyle** (ColorStyle): The color of the footer row.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/sheets#tablerowsproperties>`_
    """
    headerColorStyle: ColorStyle
    firstBandColorStyle: ColorStyle
    secondBandColorStyle: ColorStyle
    footerColorStyle: ColorStyle

################################################################################
class TableColumnProperties(TypedDict):
    """Properties of a single column in a table.

    Members:
        - **columnIndex** (int): The 0-based column index. This index is relative to its position in the table and is not necessarily the same as the column index in the sheet.
        - **columnName** (str): The name of the column.
        - **columnType** (ColumnType): The type of the column.
        - **dataValidationRule** (TableColumnDataValidationRule): The column data validation rule. Only set for dropdown column type.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/sheets#tablecolumnproperties>`_
    """
    columnIndex: int
    columnName: str
    columnType: ColumnType
    dataValidationRule: TableColumnDataValidationRule

################################################################################
class TableColumnDataValidationRule(TypedDict):
    """A data validation rule for a column in a table.

    Members:
        - **condition** (BooleanCondition): The condition that data in the cell must match. Valid only if the [BooleanCondition.type] is ``ONE_OF_LIST``.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/sheets#tablecolumndatavalidationrule>`_
    """
    condition: BooleanCondition

################################################################################
