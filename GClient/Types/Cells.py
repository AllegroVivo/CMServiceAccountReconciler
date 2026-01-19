from __future__ import annotations

from typing import TYPE_CHECKING, TypedDict, Union, NotRequired, List

from .Enums import *

if TYPE_CHECKING:
    from .Other import (
        ColorStyle, ExtendedValue, BooleanCondition, TextFormat,
        DataSourceColumnReference, FilterSpec, SortSpec, DataExecutionStatus
    )
    from .PivotTables import PivotTable
################################################################################
class CellData(TypedDict):
    """Data about a specific cell.

    Members:
        - **userEnteredValue** (ExtendedValue): The value the user entered in the cell. e.g., ``1234``, ``'Hello'``, or ``=NOW()``
        - **effectiveValue** (ExtendedValue): (Read-Only) The effective value of the cell. For cells with formulas, this is the calculated value. For cells with literals, this is the same as the userEnteredValue.
        - **formattedValue** (str): (Read-Only) The formatted value of the cell. This is the value as it's shown to the user.
        - **userEnteredFormat** (CellFormat): The format the user entered for the cell. When writing, the new format will be merged with the existing format.
        - **effectiveFormat** (CellFormat): (Read-Only) The effective format being used by the cell. This includes the results of applying any conditional formatting and, if the cell contains a formula, the computed number format. If the effective format is the default format, effective format will not be written.
        - **hyperlink** (str): (Read-Only) A hyperlink this cell points to, if any. If the cell contains multiple hyperlinks, this field will be empty.
        - **note** (str): Any note associated with the cell.
        - **textFormatRuns** (List[TextFormatRun]): Runs of rich text applied to subsections of the cell.
        - **dataValidation** (DataValidationRule): A data validation rule on the cell, if any. When writing, the new data validation rule will overwrite any prior rule.
        - **pivotTable** (PivotTable): A pivot table anchored at this cell.
        - **dataSourceTable** (DataSourceTable): A data source table anchored at this cell.
        - **dataSourceFormula** (DataSourceFormula): Output only. Information about a data source formula on the cell. The field is set if ``userEnteredValue`` is a formula referencing some ``DATA_SOURCE`` sheet, e.g. ``=SUM(DataSheet!Column)``.
        - **chipRuns** (List[ChipRun]): (Optional) Runs of chips applied to subsections of the cell. Properties of a run start at a specific index in the text and continue until the next run.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/cells#celldata>`_
    """
    userEnteredValue: ExtendedValue
    effectiveValue: ExtendedValue
    formattedValue: str
    userEnteredFormat: CellFormat
    effectiveFormat: CellFormat
    hyperlink: str
    note: str
    textFormatRuns: List[TextFormatRun]
    dataValidation: DataValidationRule
    pivotTable: PivotTable
    dataSourceTable: DataSourceTable
    dataSourceFormula: DataSourceFormula
    chipRuns: List[ChipRun]

################################################################################
class CellFormat(TypedDict):
    """The format of a cell.

    Members:
        - **numberFormat** (NumberFormat): A format describing how number values should be represented to the user.
        - **backgroundColorStyle** (ColorStyle): The background color of the cell.
        - **borders** (Borders): The borders of the cell.
        - **padding** (Padding): The padding of the cell.
        - **horizontalAlignment** (HorizontalAlign): The horizontal alignment of the value in the cell.
        - **verticalAlignment** (VerticalAlign): The vertical alignment of the value in the cell.
        - **wrapStrategy** (WrapStrategy): The wrap strategy for the value in the cell.
        - **textDirection** (TextDirection): The direction of the text in the cell.
        - **textFormat** (TextFormat): The format of the text in the cell (unless overridden by a format run).
        - **hyperlinkDisplayType** (HyperlinkDisplayType): If one exists, how a hyperlink should be displayed in the cell.
        - **textRotation** (TextRotation): The rotation applied to text in a cell.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/cells#cellformat>`_
    """
    numberFormat: NumberFormat
    backgroundColorStyle: ColorStyle
    borders: Borders
    padding: Padding
    horizontalAlignment: HorizontalAlign
    verticalAlignment: VerticalAlignment
    wrapStrategy: WrapStrategy
    textDirection: TextDirection
    textFormat: TextFormat
    hyperlinkDisplayType: HyperlinkDisplayType
    textRotation: TextRotation

################################################################################
class NumberFormat(TypedDict):
    """The number format of a cell.

    Members:
        - **type** (NumberFormatType): The type of the number format. When writing, this field must be set.
        - **pattern** (str): Pattern string used for formatting. If not set, a default pattern based on the user's locale will be used if necessary for the given type.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/cells#numberformat>`_
    """
    type: NumberFormatType
    pattern: str

################################################################################
class Borders(TypedDict):
    """The borders of the cell.

    Members:
        - **top** (Border): The top border of the cell.
        - **bottom** (Border): The bottom border of the cell.
        - **left** (Border): The left border of the cell.
        - **right** (Border): The right border of the cell.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/cells#borders>`_
    """
    top: Border
    bottom: Border
    left: Border
    right: Border

################################################################################
class Border(TypedDict):
    """A border along a cell.

    Members:
        - **style** (Style): The style of the border.
        - **colorStyle** (ColorStyle): The color of the border.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/cells#border>`_
    """
    style: Style
    colorStyle: ColorStyle

################################################################################
class Padding(TypedDict):
    """The amount of padding around the cell, in pixels.

    When updating padding, every field must be specified.

    Members:
        - **top** (int): The padding on the top of the cell.
        - **right** (int): The padding on the right of the cell.
        - **bottom** (int): The padding on the bottom of the cell.
        - **left** (int): The padding on the left of the cell.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/cells#padding>`_
    """
    top: int
    right: int
    bottom: int
    left: int

################################################################################
class _TextRotationWithAngle(TypedDict):
    angle: int
    vertical: NotRequired[None]

class _TextRotationVertical(TypedDict):
    angle: NotRequired[None]
    vertical: bool

TextRotation = Union[_TextRotationWithAngle, _TextRotationVertical]
"""The rotation applied to text in a cell.

Members:
    - **angle** (int): The angle between the standard orientation and the desired orientation. Measured in degrees. Valid values are between -90 and 90. Positive angles are angled upwards, negative are angled downwards.
    - **vertical** (bool): If true, text reads top to bottom, but the orientation of individual characters is unchanged.

`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/cells#textrotation>`_
"""

################################################################################
class TextFormatRun(TypedDict):
    """A run of a text format.

    The format of this run continues until the start index of the next run. When
    updating, all fields must be set.

    Members:
        - **startIndex** (int): The zero-based character index where this run starts, in UTF-16 code units.
        - **format** (TextFormat): The format of this run. Absent values inherit the cell's format.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/cells#textformatrun>`_
    """
    startIndex: int
    format: TextFormat

################################################################################
class DataValidationRule(TypedDict):
    """A data validation rule.

    Members:
        - **condition** (BooleanCondition): The condition that the data in the cell must satisfy.
        - **inputMessage** (str): A message to show the user when adding data to the cell.
        - **strict** (bool): True if invalid data should be rejected.
        - **showCustomUi** (bool): True if the UI should be customized based on the kind of condition. If true, "List" conditions will show a dropdown.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/cells#datavalidationrule>`_
    """
    condition: BooleanCondition
    inputMessage: str
    strict: bool
    showCustomUi: bool

################################################################################
class DataSourceTable(TypedDict):
    """A data source table, which allows the user to import a static table of
    data from the DataSource into Sheets.

    This is also known as ``"Extract"`` in the Sheets editor.

    Members:
        - **dataSourceId** (str): The ID of the data source the data source table is associated with.
        - **columnSelectionType** (DataSourceColumnSelectionType): The type to select columns for the data source table. Defaults to ``SELECTED``.
        - **columns** (List[DataSourceColumnReference]): Columns selected for the data source table. The ``columnSelectionType`` must be ``SELECTED``.
        - **filterSpecs** (List[FilterSpec]): The filter specifications for the data source table.
        - **sortSpecs** (List[SortSpec]): Sort specifications in the data source table. The result of the data source table is sorted based on the sort specifications in order.
        - **rowLimit** (int): The limit of rows to return. If not set, a default limit is applied.
        - **dataExecutionStatus** (DataExecutionStatus): Output only. The data execution status.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/cells#datasourcetable>`_
    """
    dataSourceId: str
    columnSelectionType: DataSourceTableColumnSelectionType
    columns: List[DataSourceColumnReference]
    filterSpecs: List[FilterSpec]
    sortSpecs: List[SortSpec]
    rowLimit: int
    dataExecutionStatus: DataExecutionStatus

################################################################################
class DataSourceFormula(TypedDict):
    """A data source formula

    Members:
        - **dataSourceId** (str): The ID of the data source the formula is associated with.
        - **dataExecutionStatus** (DataExecutionStatus): Output only. The data execution status.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/cells#datasourceformula>`_
    """
    dataSourceId: str
    dataExecutionStatus: DataExecutionStatus

################################################################################
class ChipRun(TypedDict):
    """The run of a chip. The chip continues until the start index of the next run.

    Members:
        - **startIndex** (int): Required. The zero-based character index where this run starts, in UTF-16 code units.
        - **chip** (Chip): Optional. The chip of this run.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/cells#chiprun>`_
    """
    startIndex: int
    chip: Chip

################################################################################
class _ChipWithPerson(TypedDict):
    personProperties: PersonProperties
    richLinkProperties: NotRequired[None]

class _ChipWithRichLink(TypedDict):
    personProperties: NotRequired[None]
    richLinkProperties: RichLinkProperties

Chip = Union[_ChipWithPerson, _ChipWithRichLink]
"""The Smart Chip.

Members:
    - **personProperties** (PersonProperties): Properties of a linked person.
    - **richLinkProperties** (RichLinkProperties): Properties of a rich link.

`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/cells#chip>`_
"""

################################################################################
class PersonProperties(TypedDict):
    """Properties specific to a linked person.

    Members:
        - **email** (str): Required. The email address linked to this person. This field is always present.
        - **displayFormat** (DisplayFormat): Optional. The display format of the person chip. If not set, the default display format is used.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/cells#personproperties>`_
    """
    email: str
    displayFormat: DisplayFormat

################################################################################
class RichLinkProperties(TypedDict):
    """Properties of a link to a Google resource.

    Only Drive files can be written as chips. All other rich link types are read only.

    Members:
        - **uri** (str): Required. The URI to the link. This is always present.
        - **mimeType** (str): Output only. The MIME type of the link, if there's one.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/cells#richlinkproperties>`_

    Note:
        URIs cannot exceed 2000 bytes when writing.
    """
    uri: str
    mimeType: str

################################################################################
