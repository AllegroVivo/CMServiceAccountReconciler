from __future__ import annotations

from typing import TypedDict, Union, NotRequired, List

from .Enums import *
################################################################################
class Color(TypedDict):
    """Represents a color in the RGBA color space.

    Members:
        - **red** (float): The red component of the color, from 0.0 to 1.0.
        - **green** (float): The green component of the color, from 0.0 to 1.0.
        - **blue** (float): The blue component of the color, from 0.0 to 1.0.
        - **alpha** (float): The alpha component of the color, from 0.0 (transparent) to 1.0 (opaque).

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/other#color>`_
    """
    red: float
    green: float
    blue: float
    alpha: float

################################################################################
class _ColorStyleRGB(TypedDict):
    rgbColor: Color
    themeColor: NotRequired[None]

class _ColorStyleTheme(TypedDict):
    rgbColor: NotRequired[None]
    themeColor: ThemeColorType

ColorStyle = Union[_ColorStyleRGB, _ColorStyleTheme]
"""A color value.

Members:
    - **rgbColor** (Color): RGB color. The alpha value in the Color object isn't generally supported.
    - **themeColor** (ThemeColorType): The theme color.

`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/other#colorstyle>`_
"""

################################################################################
class TextFormat(TypedDict):
    """The format of a run of text in a cell. Absent values indicate that the field isn't specified.

    Members:
        - **foregroundColorStyle** (ColorStyle): The foreground color of the text.
        - **fontFamily** (str): The font family.
        - **fontSize** (int): The size of the font.
        - **bold** (bool): True if the text is bold.
        - **italic** (bool): True if the text is italic.
        - **strikethrough** (bool): Whether the text is strikethrough.
        - **underline** (bool): Whether the text is underlined.
        - **link** (Link): The link destination of the text, if any.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/other#textformat>`_
    """
    foregroundColorStyle: NotRequired[ColorStyle]
    fontFamily: NotRequired[str]
    fontSize: NotRequired[int]
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    link: NotRequired[Link]

################################################################################
class Link(TypedDict):
    """An external or local reference.

    Members:
        - **uri** (str): The URL of the link.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/other#link>`_
    """
    uri: str

################################################################################
class DataSourceColumn(TypedDict):
    """A column in a data source.

    Members:
        - **reference** (DataSourceColumnReference): The column reference.
        - **formula** (str): The formula of the calculated column.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/other#datasourcecolumn>`_
    """
    reference: DataSourceColumnReference
    formula: str

################################################################################
class DataSourceColumnReference(TypedDict):
    """An unique identifier that references a data source column.

    Members:
        - **name** (str): The display name of the column. It should be unique within a data source.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/other#datasourcecolumnreference>`_
    """
    name: str

################################################################################
class DataExecutionStatus(TypedDict):
    """The data execution status.

    A data execution is created to sync a data source object with the latest
    data from a ``DataSource``. It is usually scheduled to run in the background,
    you can check its ``state`` to tell if an execution is completed.

    There are several scenarios where a data execution is triggered to run:

        - ``Adding a data source creates`` an associated data source sheet as well as a data execution to sync the data from the data source to the sheet.
        - ``Updating a data source`` creates a data execution to refresh the associated data source sheet similarly.
        - You can send a ``refresh request`` to explicitly refresh one or multiple data source objects.

    Members:
        - **state** (DataExecutionState): The current state of this data execution.
        - **errorCode** (DataExecutionErrorCode): The error code if the execution failed.
        - **errorMessage** (str): The error message, which may be empty.
        - **lastRefreshTime** (str): The last time this data execution was refreshed.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/other#dataexecutionstatus>`_
    """
    state: DataExecutionState
    errorCode: DataExecutionErrorCode
    errorMessage: str
    lastRefreshTime: str

################################################################################
class _ExtendedValueNumber(TypedDict):
    numberValue: float
    stringValue: NotRequired[None]
    boolValue: NotRequired[None]
    formulaValue: NotRequired[None]
    errorValue: NotRequired[None]

class _ExtendedValueString(TypedDict):
    numberValue: NotRequired[None]
    stringValue: str
    boolValue: NotRequired[None]
    formulaValue: NotRequired[None]
    errorValue: NotRequired[None]

class _ExtendedValueBool(TypedDict):
    numberValue: NotRequired[None]
    stringValue: NotRequired[None]
    boolValue: bool
    formulaValue: NotRequired[None]
    errorValue: NotRequired[None]

class _ExtendedValueFormula(TypedDict):
    numberValue: NotRequired[None]
    stringValue: NotRequired[None]
    boolValue: NotRequired[None]
    formulaValue: str
    errorValue: NotRequired[None]

class _ExtendedValueError(TypedDict):
    numberValue: NotRequired[None]
    stringValue: NotRequired[None]
    boolValue: NotRequired[None]
    formulaValue: NotRequired[None]
    errorValue: ErrorValue

ExtendedValue = Union[
    _ExtendedValueNumber,
    _ExtendedValueString,
    _ExtendedValueBool,
    _ExtendedValueFormula,
    _ExtendedValueError,
]
"""The kinds of value that a cell in a spreadsheet can have.

Members:
    - **numberValue** (float): Represents a double value. Note: Dates, Times and DateTimes are represented as doubles in ``SERIAL_NUMBER`` format.
    - **stringValue** (str): Represents a string value. Leading single quotes are not included. For example, if the user typed ``'123`` into the UI, this would be represented as a ``stringValue`` of ``123``.
    - **boolValue** (bool): A boolean value.
    - **formulaValue** (str): A formula value.
    - **errorValue** (ErrorValue): An error value. This field is read-only.

`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/other#extendedvalue>`_
"""

################################################################################
class ErrorValue(TypedDict):
    """An error in a cell.

    Members:
        - **type** (ErrorType): The type of error.
        - **message** (str): A message with more information about the error.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/other#errorvalue>`_
    """
    type: ErrorType
    message: str

################################################################################
class BooleanCondition(TypedDict):
    """A condition that can evaluate to true or false.

    BooleanConditions are used by conditional formatting, data validation,
    and the criteria in filters.

    Members:
        - **type** (ConditionType): The type of condition.
        - **values** (List[ConditionValue]): The values of the condition. The number of supported values depends on the ``type``. Some support zero values, others one or two values, and ``ConditionType.ONE_OF_LIST`` supports an arbitrary number of values.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/other#booleancondition>`_
    """
    type: ConditionType
    values: List[ConditionValue]

################################################################################
class _ConditionValueRelDate(TypedDict):
    relativeDate: RelativeDate
    userEnteredValue: NotRequired[None]

class _ConditionValueUserEntered(TypedDict):
    relativeDate: NotRequired[None]
    userEnteredValue: str

ConditionValue = Union[_ConditionValueRelDate, _ConditionValueUserEntered]
"""The value of a condition.

Members:
    - **relativeDate** (RelativeDate): A relative date value.
    - **userEnteredValue** (str): A user-entered value.
    
`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/other#conditionvalue>`_
"""

################################################################################
class GridRange(TypedDict):
    """A range on a sheet.

    All indexes are zero-based. Indexes are half open, i.e. the start index is
    inclusive and the end index is exclusive -- [startIndex, endIndex]. Missing
    indexes indicate the range is unbounded on that side.

    For example, if "Sheet1" is sheet ID 123456, then:

    ``Sheet1!A1:A1 == sheetId: 123456, startRowIndex: 0, endRowIndex: 1, startColumnIndex: 0, endColumnIndex: 1``

    ``Sheet1!A3:B4 == sheetId: 123456, startRowIndex: 2, endRowIndex: 4, startColumnIndex: 0, endColumnIndex: 2``

    ``Sheet1!A:B == sheetId: 123456, startColumnIndex: 0, endColumnIndex: 2``

    ``Sheet1!A5:B == sheetId: 123456, startRowIndex: 4, startColumnIndex: 0, endColumnIndex: 2``

    ``Sheet1 == sheetId: 123456``

    The start index must always be less than or equal to the end index. If the
    start index equals the end index, then the range is empty. Empty ranges are
    typically not meaningful and are usually rendered in the UI as ``#REF!``.

    Members:
        - **sheetId** (int): The sheet this range is on.
        - **startRowIndex** (int): The start row (inclusive) of the range, or not set if unbounded.
        - **endRowIndex** (int): The end row (exclusive) of the range, or not set if unbounded.
        - **startColumnIndex** (int): The start column (inclusive) of the range, or not set if unbounded.
        - **endColumnIndex** (int): The end column (exclusive) of the range, or not set if unbounded.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/other#gridrange>`_
    """
    sheetId: int
    startRowIndex: NotRequired[int]
    endRowIndex: NotRequired[int]
    startColumnIndex: NotRequired[int]
    endColumnIndex: NotRequired[int]

################################################################################
class _FilterSpecBase(TypedDict):
    filterCriteria: FilterCriteria

class FilterSpecByColumnIdx(_FilterSpecBase):
    columnIndex: int
    dataSourceColumnReference: NotRequired[None]

class FilterSpecByDataSourceColumnRef(_FilterSpecBase):
    columnIndex: NotRequired[None]
    dataSourceColumnReference: DataSourceColumnReference

FilterSpec = Union[FilterSpecByColumnIdx, FilterSpecByDataSourceColumnRef]
"""The filter criteria associated with a specific column.

Members:
    - **filterCriteria** (FilterCriteria): The criteria for the column.
    - **columnIndex** (int): The zero-based column index.
    - **dataSourceColumnReference** (DataSourceColumnReference): The data source column reference
    
`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/other#filterspec>`_
"""

################################################################################
class FilterCriteria(TypedDict):
    """Criteria for showing/hiding rows in a filter or filter view.

    Members:
        - **hiddenValues** (List[str]): Values that should be hidden.
        - **condition** (BooleanCondition): A condition that must be true for values to be shown.
        - **visibleBackgroundColorStyle** (ColorStyle): The background fill color to filter by; only cells with this fill color are shown.
        - **visibleForegroundColorStyle** (ColorStyle): The foreground text color to filter by; only cells with this text color are shown.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/other#filtercriteria>`_
    """
    hiddenValues: List[str]
    condition: BooleanCondition
    visibleBackgroundColorStyle: ColorStyle
    visibleForegroundColorStyle: ColorStyle

################################################################################
class _SortSpecBase(TypedDict):
    sortOrder: SortOrder
    foregroundColorStyle: ColorStyle
    backgroundColorStyle: ColorStyle

class _SortSpecByIdx(_SortSpecBase):
    dimensionIndex: int
    dataSourceColumnReference: NotRequired[None]

class _SortSpecByDataSourceColumnRef(_SortSpecBase):
    dimensionIndex: NotRequired[None]
    dataSourceColumnReference: DataSourceColumnReference

SortSpec = Union[_SortSpecByIdx, _SortSpecByDataSourceColumnRef]
"""A sort order associated with a specific column or row.

Members:
    - **sortOrder** (SortOrder): The order to sort by.
    - **foregroundColorStyle** (ColorStyle): The foreground color to sort by; cells with this foreground color are sorted to the top.
    - **backgroundColorStyle** (ColorStyle): The background color to sort by; cells with this background color are sorted to the top.
    - **dimensionIndex** (int): The dimension the sort should be applied to.
    - **dataSourceColumnReference** (DataSourceColumnReference): Reference to a data source column.
    
`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/other#sortspec>`_
"""

################################################################################
class _EmbeddedObjectPositionBySheet(TypedDict):
    sheetId: int
    overlayPosition: NotRequired[None]
    newSheet: NotRequired[None]

class _EmbeddedObjectPositionByOverlayPosition(TypedDict):
    sheetId: NotRequired[None]
    overlayPosition: OverlayPosition
    newSheet: NotRequired[None]

class _EmbeddedObjectPositionByNewSheet(TypedDict):
    sheetId: NotRequired[None]
    overlayPosition: NotRequired[None]
    newSheet: bool

EmbeddedObjectPosition = Union[
    _EmbeddedObjectPositionBySheet,
    _EmbeddedObjectPositionByOverlayPosition,
    _EmbeddedObjectPositionByNewSheet,
]
"""The position of an embedded object such as a chart.

Members:
    - **sheetId** (int): The sheet this is on. Set only if the embedded object is on its own sheet. Must be non-negative.
    - **overlayPosition** (OverlayPosition): The position at which the object is overlaid on top of a grid.
    - **newSheet** (bool): If true, the embedded object is put on a new sheet whose ID is chosen for you. Used only when writing.

`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/other#embeddedobjectposition>`_
"""

################################################################################
class OverlayPosition(TypedDict):
    """The location an object is overlaid on top of a grid.

    Members:
        - **anchorCell** (GridCoordinate): The cell the object is anchored to.
        - **offsetXPixels** (int): The horizontal offset, in pixels, that the object is offset from the anchor cell.
        - **offsetYPixels** (int): The vertical offset, in pixels, that the object is offset from the anchor cell.
        - **widthPixels** (int): The width of the object, in pixels. Defaults to 600.
        - **heightPixels** (int): The height of the object, in pixels. Defaults to 371.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/other#overlayposition>`_
    """
    anchorCell: GridCoordinate
    offsetXPixels: int
    offsetYPixels: int
    widthPixels: int
    heightPixels: int

################################################################################
class GridCoordinate(TypedDict):
    """A coordinate in a sheet.

    All indexes are zero-based.

    Members:
        - **sheetId** (int): The sheet this coordinate is on.
        - **rowIndex** (int): The row index of the coordinate.
        - **columnIndex** (int): The column index of the coordinate.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/other#gridcoordinate>`_
    """
    sheetId: int
    rowIndex: int
    columnIndex: int

################################################################################
