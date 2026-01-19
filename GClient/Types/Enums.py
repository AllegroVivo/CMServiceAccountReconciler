from enum import Enum
################################################################################
class _FroggeEnum(Enum):

    def __str__(self):
        return str(self.value)

    def _generate_next_value_(name, *_):
        return name

################################################################################
class MimeType(_FroggeEnum):

    GoogleSheet = "application/vnd.google-apps.spreadsheet"
    PDF = "application/pdf"
    Excel = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    CSV = "text/csv"
    OpenOfficeSheet = "application/x-vnd.oasis.opendocument.spreadsheet"
    TSV = "text/tab-separated-values"
    ZIP = "application/zip"

################################################################################
class ExportFormat(_FroggeEnum):

    PDF = MimeType.PDF
    Excel = MimeType.Excel
    CSV = MimeType.CSV
    OpenOfficeSheet = MimeType.OpenOfficeSheet
    TSV = MimeType.TSV
    ZipFile = MimeType.ZIP

################################################################################
class PermissionType(_FroggeEnum):

    User = "user"
    Group = "group"
    Domain = "domain"
    Anyone = "anyone"

################################################################################
class PermissionRoleType(_FroggeEnum):

    Owner = "owner"
    Writer = "writer"
    Reader = "reader"

################################################################################
class SheetType(_FroggeEnum):

    Unspecified = "SHEET_TYPE_UNSPECIFIED"  # Default value, do not use.
    Grid = "GRID"  # Default sheet type - a grid.
    Object = "OBJECT"  # A sheet that holds objects such as charts or images.
    DataSource = "DATA_SOURCE"  # A sheet that connects to an external data source.

################################################################################
class ThemeColorType(_FroggeEnum):

    Unspecified = "THEME_COLOR_TYPE_UNSPECIFIED"
    TextPrimary = "TEXT"
    BackgroundPrimary = "BACKGROUND"
    Accent1 = "ACCENT1"
    Accent2 = "ACCENT2"
    Accent3 = "ACCENT3"
    Accent4 = "ACCENT4"
    Accent5 = "ACCENT5"
    Accent6 = "ACCENT6"
    Link = "LINK"

################################################################################
class DataExecutionState(_FroggeEnum):

    Unspecified = "DATA_EXECUTION_STATE_UNSPECIFIED"
    NotStarted = "NOT_STARTED"
    Running = "RUNNING"
    Cancelling = "CANCELLING"
    Succeeded = "SUCCEEDED"
    Failed = "FAILED"

################################################################################
class DataExecutionErrorCode(_FroggeEnum):

    Unspecified = "DATA_EXECUTION_ERROR_CODE_UNSPECIFIED"
    TimedOut = "TIMED_OUT"
    TooManyRows = "TOO_MANY_ROWS"
    TooManyColumns = "TOO_MANY_COLUMNS"
    TooManyCells = "TOO_MANY_CELLS"
    Engine = "ENGINE"
    ParameterError = "PARAMETER_INVALID"
    UnsupportedData = "UNSUPPORTED_DATA_TYPE"
    DuplicateColumnNames = "DUPLICATE_COLUMN_NAMES"
    Interrupted = "INTERRUPTED"
    ConcurrentQuery = "CONCURRENT_QUERY"
    TooManyCharsPerCell = "TOO_MANY_CHARS_PER_CELL"
    NotFound = "DATA_NOT_FOUND"
    AccessDenied = "PERMISSION_DENIED"
    MissingColumnAlias = "MISSING_COLUMN_ALIAS"
    ObjectNotFound = "OBJECT_NOT_FOUND"
    ObjectInError = "OBJECT_IN_ERROR_STATE"
    InvalidSpec = "OBJECT_SPEC_INVALID"
    Cancelled = "DATA_EXECUTION_CANCELLED"
    Other = "OTHER"

################################################################################
class SortOrder(_FroggeEnum):

    Unspecified = "SORT_ORDER_UNSPECIFIED"
    Ascending = "ASCENDING"
    Descending = "DESCENDING"

################################################################################
class ConditionType(_FroggeEnum):

    Unspecified = "CONDITION_TYPE_UNSPECIFIED"
    Greater = "NUMBER_GREATER"
    GreaterEqual = "NUMBER_GREATER_THAN_EQ"
    Less = "NUMBER_LESS"
    LessEqual = "NUMBER_LESS_THAN_EQ"
    Equal = "NUMBER_EQ"
    NotEqual = "NUMBER_NOT_EQ"
    Between = "NUMBER_BETWEEN"
    NotBetween = "NUMBER_NOT_BETWEEN"
    TextContains = "TEXT_CONTAINS"
    TextNotContains = "TEXT_NOT_CONTAINS"
    TextStartsWith = "TEXT_STARTS_WITH"
    TextEndsWith = "TEXT_ENDS_WITH"
    TextEquals = "TEXT_EQ"
    IsEmail = "TEXT_IS_EMAIL"
    IsUrl = "TEXT_IS_URL"
    DateEquals = "DATE_EQ"
    DateBefore = "DATE_BEFORE"
    DateAfter = "DATE_AFTER"
    DateOnOrBefore = "DATE_ON_OR_BEFORE"
    DateOnOrAfter = "DATE_ON_OR_AFTER"
    DateBetween = "DATE_BETWEEN"
    DateNotBetween = "DATE_NOT_BETWEEN"
    DateValid = "DATE_IS_VALID"
    OneOfRange = "ONE_OF_RANGE"
    OneOfList = "ONE_OF_LIST"
    Blank = "BLANK"
    NotBlank = "NOT_BLANK"
    Formula = "CUSTOM_FORMULA"
    Boolean = "BOOLEAN"
    TextNotEquals = "TEXT_NOT_EQ"
    DateNotEquals = "DATE_NOT_EQ"
    FilterExpr = "FILTER_EXPRESSION"

################################################################################
class RelativeDate(_FroggeEnum):

    Unspecified = "RELATIVE_DATE_UNSPECIFIED"
    PastYear = "PAST_YEAR"
    PastMonth = "PAST_MONTH"
    PastWeek = "PAST_WEEK"
    Yesterday = "YESTERDAY"
    Today = "TODAY"
    Tomorrow = "TOMORROW"

################################################################################
class NumberFormatType(_FroggeEnum):

    Unspecified = "NUMBER_FORMAT_TYPE_UNSPECIFIED"
    Text = "TEXT"
    Number = "NUMBER"
    Percent = "PERCENT"
    Currency = "CURRENCY"
    Date = "DATE"
    Time = "TIME"
    DateTime = "DATE_TIME"
    Scientific = "SCIENTIFIC"

################################################################################
class Style(_FroggeEnum):

    Unspecified = "STYLE_UNSPECIFIED"
    Dotted = "DOTTED"
    Dashed = "DASHED"
    Solid = "SOLID"
    SolidMedium = "SOLID_MEDIUM"
    SolidThick = "SOLID_THICK"
    NoneStyle = "NONE"
    Double = "DOUBLE"

################################################################################
class HorizontalAlign(_FroggeEnum):

    Unspecified = "HORIZONTAL_ALIGN_UNSPECIFIED"
    Left = "LEFT"
    Center = "CENTER"
    Right = "RIGHT"

################################################################################
class VerticalAlignment(_FroggeEnum):

    Unspecified = "VERTICAL_ALIGN_UNSPECIFIED"
    Top = "TOP"
    Middle = "MIDDLE"
    Bottom = "BOTTOM"

################################################################################
class WrapStrategy(_FroggeEnum):

    Unspecified = "WRAP_STRATEGY_UNSPECIFIED"
    Overflow = "OVERFLOW_CELL"
    LegacyWrap = "LEGACY_WRAP"
    Clip = "CLIP"
    Wrap = "WRAP"

################################################################################
class TextDirection(_FroggeEnum):

    Unspecified = "TEXT_DIRECTION_UNSPECIFIED"
    LeftToRight = "LEFT_TO_RIGHT"
    RightToLeft = "RIGHT_TO_LEFT"

################################################################################
class HyperlinkDisplayType(_FroggeEnum):

    Unspecified = "HYPERLINK_DISPLAY_TYPE_UNSPECIFIED"
    Linked = "LINKED"
    TextOnly = "PLAIN_TEXT"

################################################################################
class InterpolationPointType(_FroggeEnum):

    Unspecified = "INTERPOLATION_POINT_TYPE_UNSPECIFIED"
    Minimum = "MIN"
    Maximum = "MAX"
    Number = "NUMBER"
    Percent = "PERCENT"
    Percentile = "PERCENTILE"

################################################################################
class ChartHiddenDimensionStrategy(_FroggeEnum):

    Unspecified = "CHART_HIDDEN_DIMENSION_STRATEGY_UNSPECIFIED"
    SkipAllHidden = "SKIP_HIDDEN_ROWS_AND_COLUMNS"
    SkipHiddenRows = "SKIP_HIDDEN_ROWS"
    SkipHiddenColumns = "SKIP_HIDDEN_COLUMNS"
    ShowAll = "SHOW_ALL"

################################################################################
class BasicChartType(_FroggeEnum):

    Unspecified = "BASIC_CHART_TYPE_UNSPECIFIED"
    Bar = "BAR"
    Line = "LINE"
    Area = "AREA"
    Column = "COLUMN"
    Scatter = "SCATTER"
    Combo = "COMBO"
    SteppedArea = "STEPPED_AREA"

################################################################################
class BasicChartLegendPosition(_FroggeEnum):

    Unspecified = "BASIC_CHART_LEGEND_POSITION_UNSPECIFIED"
    Bottom = "BOTTOM_LEGEND"
    Left = "LEFT_LEGEND"
    Right = "RIGHT_LEGEND"
    Top = "TOP_LEGEND"
    NoLegend = "NO_LEGEND"

################################################################################
class BasicChartAxisPosition(_FroggeEnum):

    Unspecified = "BASIC_CHART_AXIS_POSITION_UNSPECIFIED"
    Bottom = "BOTTOM_AXIS"
    Left = "LEFT_AXIS"
    Right = "RIGHT_AXIS"

################################################################################
class ViewWindowMode(_FroggeEnum):

    Default = "DEFAULT_VIEW_WINDOW_MODE"
    Unsupported = "VIEW_WINDOW_MODE_UNSUPPORTED"
    Explicit = "EXPLICIT"
    Pretty = "PRETTY"

################################################################################
class DateTimeRuleType(_FroggeEnum):

    Unspecified = "DATE_TIME_RULE_TYPE_UNSPECIFIED"
    Second = "SECOND"
    Minute = "MINUTE"
    Hour = "HOUR"
    HourMinute = "HOUR_MINUTE"
    HourMinuteAmPm = "HOUR_MINUTE_AMPM"
    DayOfWeek = "DAY_OF_WEEK"
    DayOfYear = "DAY_OF_YEAR"
    DayOfMonth = "DAY_OF_MONTH"
    DayMonth = "DAY_MONTH"
    Month = "MONTH"
    Quarter = "QUARTER"
    Year = "YEAR"
    YearMonth = "YEAR_MONTH"
    YearQuarter = "YEAR_QUARTER"
    YearMonthDay = "YEAR_MONTH_DAY"

################################################################################
class ChartAggregateType(_FroggeEnum):

    Unspecified = "CHART_AGGREGATE_TYPE_UNSPECIFIED"
    Average = "AVERAGE"
    Count = "COUNT"
    Max = "MAX"
    Median = "MEDIAN"
    Min = "MIN"
    Sum = "SUM"

################################################################################
class LineDashType(_FroggeEnum):

    Unspecified = "LINE_DASH_TYPE_UNSPECIFIED"
    Invisible = "INVISIBLE"
    Custom = "CUSTOM"
    Solid = "SOLID"
    Dotted = "DOTTED"
    MedDash = "MEDIUM_DASHED"
    MedDashDot = "MEDIUM_DASHED_DOTTED"
    LongDash = "LONG_DASHED"
    LongDashDot = "LONG_DASHED_DOTTED"

################################################################################
class DataLabelType(_FroggeEnum):

    Unspecified = "DATA_LABEL_TYPE_UNSPECIFIED"
    NoneType = "NONE"
    Data = "DATA"
    Custom = "CUSTOM"

################################################################################
class DataLabelPlacement(_FroggeEnum):

    Unspecified = "DATA_LABEL_PLACEMENT_UNSPECIFIED"
    Center = "CENTER"
    Left = "LEFT"
    Right = "RIGHT"
    Above = "ABOVE"
    Below = "BELOW"
    InsideEnd = "INSIDE_END"
    InsideBase = "INSIDE_BASE"
    OutsideEnd = "OUTSIDE_END"

################################################################################
class PointShape(_FroggeEnum):

    Unspecified = "POINT_SHAPE_UNSPECIFIED"
    Circle = "CIRCLE"
    Diamond = "DIAMOND"
    Hexagon = "HEXAGON"
    Pentagon = "PENTAGON"
    Square = "SQUARE"
    Star = "STAR"
    Triangle = "TRIANGLE"
    XMark = "X_MARK"

################################################################################
class BasicChartStackedType(_FroggeEnum):

    Unspecified = "BASIC_CHART_STACKED_TYPE_UNSPECIFIED"
    NotStacked = "NOT_STACKED"
    Stacked = "STACKED"
    PercentStacked = "PERCENT_STACKED"

################################################################################
class BasicChartCompareMode(_FroggeEnum):

    Unspecified = "BASIC_CHART_COMPARE_MODE_UNSPECIFIED"
    Datum = "DATUM"
    Category = "CATEGORY"

################################################################################
class PieChartLegendPosition(_FroggeEnum):

    Unspecified = "PIE_CHART_LEGEND_POSITION_UNSPECIFIED"
    Bottom = "BOTTOM_LEGEND"
    Left = "LEFT_LEGEND"
    Right = "RIGHT_LEGEND"
    Top = "TOP_LEGEND"
    NoLegend = "NO_LEGEND"
    Labeled = "LABELED_LEGEND"

################################################################################
class BubbleChartLegendPosition(_FroggeEnum):

    Unspecified = "BUBBLE_CHART_LEGEND_POSITION_UNSPECIFIED"
    Bottom = "BOTTOM_LEGEND"
    Left = "LEFT_LEGEND"
    Right = "RIGHT_LEGEND"
    Top = "TOP_LEGEND"
    NoLegend = "NO_LEGEND"
    Inside = "INSIDE_LEGEND"

################################################################################
class OrgChartNodeSize(_FroggeEnum):

    Unspecified = "ORG_CHART_LABEL_SIZE_UNSPECIFIED"
    Small = "SMALL"
    Medium = "MEDIUM"
    Large = "LARGE"

################################################################################
class HistogramChartLegendPosition(_FroggeEnum):

    Unspecified = "HISTOGRAM_CHART_LEGEND_POSITION_UNSPECIFIED"
    Bottom = "BOTTOM_LEGEND"
    Left = "LEFT_LEGEND"
    Right = "RIGHT_LEGEND"
    Top = "TOP_LEGEND"
    NoLegend = "NO_LEGEND"
    Inside = "INSIDE_LEGEND"

################################################################################
class WaterfallChartStackedType(_FroggeEnum):

    Unspecified = "WATERFALL_STACKED_TYPE_UNSPECIFIED"
    Stacked = "STACKED"
    Sequential = "SEQUENTIAL"

################################################################################
class ComparisonType(_FroggeEnum):

    Unspecified = "COMPARISON_TYPE_UNDEFINED"
    Absolute = "ABSOLUTE_DIFFERENCE"
    Percentage = "PERCENTAGE_DIFFERENCE"

################################################################################
class ChartNumberFormatSource(_FroggeEnum):

    Unspecified = "CHART_NUMBER_FORMAT_SOURCE_UNDEFINED"
    Data = "FROM_DATA"
    Custom = "CUSTOM"

################################################################################
class DeveloperMetadataVisibility(_FroggeEnum):

    Unspecified = "DEVELOPER_METADATA_VISIBILITY_UNSPECIFIED"
    Document = "DOCUMENT"
    Project = "PROJECT"

################################################################################
class DeveloperMetadataLocationType(_FroggeEnum):

    Unspecified = "DEVELOPER_METADATA_LOCATION_TYPE_UNSPECIFIED"
    Row = "ROW"
    Column = "COLUMN"
    Sheet = "SHEET"
    Spreadsheet = "SPREADSHEET"

################################################################################
class Dimension(_FroggeEnum):

    Unspecified = "DIMENSION_UNSPECIFIED"
    Rows = "ROWS"
    Columns = "COLUMNS"

################################################################################
class RefreshCancellationState(_FroggeEnum):

    Unspecified = "REFRESH_CANCELLATION_STATE_UNSPECIFIED"
    Success = "CANCEL_SUCCEEDED"
    Failed = "CANCEL_FAILED"

################################################################################
class RefreshCancellationErrorCode(_FroggeEnum):

    Unspecified = "REFRESH_CANCELLATION_ERROR_CODE_UNSPECIFIED"
    NotFound = "EXECUTION_NOT_FOUND"
    Forbidden = "CANCEL_PERMISSION_DENIED"
    Completed = "QUERY_EXECUTION_COMPLETED"
    Concurrent = "CONCURRENT_CANCELLATION"
    Other = "CANCEL_OTHER_ERROR"

################################################################################
class ColumnType(_FroggeEnum):

    Unspecified = "COLUMN_TYPE_UNSPECIFIED"
    Double = "DOUBLE"
    Currency = "CURRENCY"
    Percent = "PERCENT"
    Date = "DATE"
    Time = "TIME"
    DateTime = "DATE_TIME"
    Text = "TEXT"
    Boolean = "BOOLEAN"
    Dropdown = "DROPDOWN"
    FilesChip = "FILES_CHIP"
    PeopleChip = "PEOPLE_CHIP"
    FinanceChip = "FINANCE_CHIP"
    PlaceChip = "PLACE_CHIP"
    RatingsChip = "RATINGS_CHIP"

################################################################################
class RecalculationInterval(_FroggeEnum):
    """An enumeration of the possible recalculation interval options.

    Members:
        - **Unspecified:** Default value, do not use.
        - **OnChange:** Volatile functions are updated on every change.
        - **Minute:** Volatile functions are updated on every change and every minute.
        - **Hour:** Volatile functions are updated on every change and hourly.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets#recalculationinterval>`_
    """
    Unspecified = "RECALCULATION_INTERVAL_UNSPECIFIED"
    OnChange = "ON_CHANGE"
    Minute = "MINUTE"
    Hour = "HOUR"

################################################################################
class DataSourceRefreshScope(_FroggeEnum):
    """The data source refresh scopes.

    Members:
        - **Unspecified:** Default value, do not use.
        - **All:** Refreshes all data sources and their associated data source objects in the spreadsheet.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets#datasourcerefreshscope>`_
    """
    Unspecified = "DATA_SOURCE_REFRESH_SCOPE_UNSPECIFIED"
    All = "ALL_DATA_SOURCES"

################################################################################
class DayOfWeek(_FroggeEnum):
    """An enumeration of the days of the week.

    Members:
        - **Unspecified:** Default value, do not use.
        - **Sunday:** Sunday
        - **Monday:** Monday
        - **Tuesday:** Tuesday
        - **Wednesday:** Wednesday
        - **Thursday:** Thursday
        - **Friday:** Friday
        - **Saturday:** Saturday

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets#dayofweek>`_
    """
    Unspecified = "DAY_OF_WEEK_UNSPECIFIED"
    Sunday = "SUNDAY"
    Monday = "MONDAY"
    Tuesday = "TUESDAY"
    Wednesday = "WEDNESDAY"
    Thursday = "THURSDAY"
    Friday = "FRIDAY"
    Saturday = "SATURDAY"

################################################################################
class DataSourceTableColumnSelectionType(_FroggeEnum):
    """The data source table column selection types.

    Members:
        - **Unspecified:** Default value, do not use.
        - **Selected:** Select columns specified by ``columns`` field.
        - **All:** Sync all current and future columns in the data source.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/cells#datasourcetablecolumnselectiontype`_
    """
    Unspecified = "DATA_SOURCE_TABLE_COLUMN_SELECTION_TYPE_UNSPECIFIED"
    Selected = "SELECTED"
    All = "SYNC_ALL"

################################################################################
class DisplayFormat(_FroggeEnum):
    """Preferred display format when available.

    Members:
        - **Unspecified:** Default value, do not use.
        - **Default:** 	Default display format.
        - **LastFirst:** Display name as "Last, First".
        - **Email:** Email display format.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/cells#displayformat>`_
    """
    Unspecified = "DISPLAY_FORMAT_UNSPECIFIED"
    Default = "DEFAULT"
    LastFirst = "LAST_NAME_COMMA_FIRST_NAME"
    Email = "EMAIL"

################################################################################
class ErrorType(_FroggeEnum):
    """The type of error.

    Members:
        - **Unspecified:** Default value, do not use.
        - **Error:** Corresponds to the ``#ERROR!`` error.
        - **Null:** Corresponds to the ``#NULL!`` error.
        - **Div0:** Corresponds to the ``#DIV/0!`` error.
        - **Value:** Corresponds to the ``#VALUE!`` error.
        - **Ref:** 	Corresponds to the ``#REF!`` error.
        - **Name:** Corresponds to the ``#NAME?`` error.
        - **Num:** 	Corresponds to the ``#NUM!`` error.
        - **NotFound:** Corresponds to the ``#N/A`` error.
        - **Loading:** 	Corresponds to the ``Loading...`` state.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/other#errortype>`_
    """
    Unspecified = "ERROR_TYPE_UNSPECIFIED"
    Error = "ERROR"
    Null = "NULL_VALUE"
    Div0 = "DIVIDE_BY_ZERO"
    Value = "VALUE"
    Ref = "REF"
    Name = "NAME"
    Num = "NUM"
    NotFound = "N_A"
    Loading = "LOADING"

################################################################################
class PivotValueSummarizeFunction(_FroggeEnum):
    """A function to summarize a pivot value.

    Members:
        - **Unspecified:** Default value, do not use.
        - **Sum:** 	Corresponds to the ``SUM`` function.
        - **CountA:** Corresponds to the ``COUNTA`` function.
        - **Count:** Corresponds to the ``COUNT`` function.
        - **CountUnique:** Corresponds to the ``COUNTUNIQUE`` function.
        - **Average:** Corresponds to the ``AVERAGE`` function.
        - **Max:** 	Corresponds to the ``MAX`` function.
        - **Min:** 	Corresponds to the ``MIN`` function.
        - **Median:** Corresponds to the ``MEDIAN`` function.
        - **Product:** Corresponds to the ``PRODUCT`` function.
        - **StdDev:** Corresponds to the ``STDDEV`` function.
        - **StdDevP:** Corresponds to the ``STDDEVP`` function.
        - **Var:** 	Corresponds to the ``VAR`` function.
        - **VarP:** Corresponds to the ``VARP`` function.
        - **Custom:** Indicates the formula should be used as-is. Only valid if ``PivotValue.formula`` was set.
        - **NoFormula:** Indicates that the value is already summarized, and the summarization function is not explicitly specified.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/pivot-tables#pivotvaluesummarizefunction>`_
    """
    Unspecified = "PIVOT_STANDARD_VALUE_FUNCTION_UNSPECIFIED"
    Sum = "SUM"
    CountA = "COUNTA"
    Count = "COUNT"
    CountUnique = "COUNTUNIQUE"
    Average = "AVERAGE"
    Max = "MAX"
    Min = "MIN"
    Median = "MEDIAN"
    Product = "PRODUCT"
    StdDev = "STDDEV"
    StdDevP = "STDDEVP"
    Var = "VAR"
    VarP = "VARP"
    Custom = "CUSTOM"
    NoFormula = "NONE"

################################################################################
class PivotValueCalculatedDisplayType(_FroggeEnum):
    """The possible ways that pivot values may be calculated for display.

    Members:
        - **Unspecified:** Default value, do not use.
        - **PctRowTotal:** Display the value as a percentage of the row total.
        - **PctColumnTotal:** Display the value as a percentage of the column total.
        - **PctGrandTotal:** Display the value as a percentage of the grand total.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/pivot-tables#pivotvaluecalculateddisplaytype>`_
    """
    Unspecified = "PIVOT_VALUE_CALCULATED_DISPLAY_TYPE_UNSPECIFIED"
    PctRowTotal = "PERCENT_OF_ROW_TOTAL"
    PctColumnTotal = "PERCENT_OF_COLUMN_TOTAL"
    PctGrandTotal = "PERCENT_OF_GRAND_TOTAL"

################################################################################
class PivotValueLayout(_FroggeEnum):
    """The layout of pivot values.

    Members:
        - **Horizontal:** Display pivot values horizontally (as columns).
        - **Vertical:** Display pivot values vertically (as rows).

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/pivot-tables#pivotvaluelayout>`_
    """
    Horizontal = "HORIZONTAL"
    Vertical = "VERTICAL"

################################################################################
class DeveloperMetadataLocationMatchingStrategy(_FroggeEnum):
    """An enumeration of strategies for matching developer metadata locations.

    Members:
        - **Unspecified:** Default value, do not use.
        - **Exact:** Indicates that a specified location should be matched exactly.
        - **Intersecting:** Indicates that a specified location should match that exact location as well as any intersecting locations.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/DataFilter#developermetadatalocationmatchingstrategy>`_
    """
    Unspecified = "DEVELOPER_METADATA_LOCATION_MATCHING_STRATEGY_UNSPECIFIED"
    Exact = "EXACT_LOCATION"
    Intersecting = "INTERSECTING_LOCATION"

################################################################################
class DateTimeRenderOption(_FroggeEnum):
    """Determines how dates should be rendered in the output.

    Members:
        - **Serial:** Instructs date, time, datetime, and duration fields to be output as doubles in "serial number" format, as popularized by Lotus 1-2-3.
        - **Formatted:** Instructs date, time, datetime, and duration fields to be output as strings in their given number format.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/DateTimeRenderOption>`_
    """
    Serial = "SERIAL_NUMBER"
    Formatted = "FORMATTED_STRING"

################################################################################
class ErrorCode(_FroggeEnum):
    """Specific error code indicating what went wrong.

    Copying the spreadsheet may fix the issue.

    Members:
        - **Unspecified:** Default value, do not use.
        - **CantEdit:** The document is too large to perform edit operations.
        - **CantLoad:** The document is too large to load.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/ErrorCode>`_
    """
    Unspecified = "ERROR_CODE_UNSPECIFIED"
    CantEdit = "DOCUMENT_TOO_LARGE_TO_EDIT"
    CantLoad = "DOCUMENT_TOO_LARGE_TO_LOAD"

################################################################################
class ValueInputOption(_FroggeEnum):
    """Determines how input data should be interpreted.

    Members:
        - **Unspecified:** Default value, do not use.
        - **Raw:** The values the user has entered will not be parsed and will be stored as-is.
        - **UserEntered:** The values will be parsed as if the user typed them into the Google Sheets UI.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/ValueInputOption>`_
    """
    Unspecified = "INPUT_VALUE_OPTION_UNSPECIFIED"
    Raw = "RAW"
    UserEntered = "USER_ENTERED"

################################################################################
class ValueRenderOption(_FroggeEnum):
    """Determines how values should be rendered in the output.

    Members:
        - **Formatted:** Values will be calculated & formatted in the response according to the cell's formatting.
        - **Unformatted:** Values will be calculated, but not formatted in the reply.
        - **Formula:** Values will not be calculated. The reply will include the formulas.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/ValueRenderOption>`_
    """
    Formatted = "FORMATTED_VALUE"
    Unformatted = "UNFORMATTED_VALUE"
    Formula = "FORMULA"

################################################################################
class PasteType(_FroggeEnum):
    """What kind of data should be pasted.

    Members:
        - **Normal:** Paste values, formulas, formats, and merges.
        - **Values:** Paste the values ONLY without formats, formulas, or merges.
        - **Format:** Paste the format and data validation only.
        - **NoBorders:** Like ``PASTE_NORMAL`` but without borders.
        - **Formula:** Only the formulas of the cells will be pasted.
        - **DataValidation:** Only the data validation rules of the cells will be pasted.
        - **ConditionalFormatting:** Only the conditional formatting rules of the cells will be pasted.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#pastetype>`_
    """
    Normal = "PASTE_NORMAL"
    Values = "PASTE_VALUES"
    Format = "PASTE_FORMAT"
    NoBorders = "PASTE_NO_BORDERS"
    Formula = "PASTE_FORMULA"
    DataValidation = "PASTE_DATA_VALIDATION"
    ConditionalFormatting = "PASTE_CONDITIONAL_FORMATTING"

################################################################################
class PasteOrientation(_FroggeEnum):
    """How a paste operation should be performed.

    Members:
        - **Normal:** Paste normally.
        - **Transpose:** Paste transposed, where all rows become columns and vice versa.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#pasteorientation>`_
    """
    Normal = "NORMAL"
    Transpose = "TRANSPOSE"

################################################################################
class MergeType(_FroggeEnum):
    """The type of merge to perform.

    Members:
        - **All:** Create a single merge from the range
        - **Horizontal:** Create a merge for each column in the range
        - **Vertical:** Create a merge for each row in the range

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#mergetype>`_
    """
    All = "MERGE_ALL"
    Horizontal = "MERGE_COLUMNS"
    Vertical = "MERGE_ROWS"

################################################################################
class DelimiterType(_FroggeEnum):
    """The delimiter to split on.

    Members:
        - **Unspecified:** Default value, do not use.
        - **Comma:** Comma (`,`)
        - **Semicolon:** Semicolon (`;`)
        - **Period:** Period (`.`)
        - **Space:** Space (` `)
        - **Custom:** A custom delimiter specified in the ``delimiter`` field.
        - **Auto:** Automatically detect the delimiter.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request#delimitertype>`_
    """
    Unspecified = "DELIMITER_TYPE_UNSPECIFIED"
    Comma = "COMMA"
    Semicolon = "SEMICOLON"
    Period = "PERIOD"
    Space = "SPACE"
    Custom = "CUSTOM"
    Auto = "AUTODETECT"

################################################################################
