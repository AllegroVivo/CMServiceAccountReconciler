from __future__ import annotations

from typing import TYPE_CHECKING, TypedDict, Union, NotRequired, List, Optional

from .Enums import *

if TYPE_CHECKING:
    from .Sheets import Sheet
    from .Other import ColorStyle, GridRange, DataSourceColumn
    from .Cells import CellFormat
    from .DeveloperMetadata import DeveloperMetadata
################################################################################
class Spreadsheet(TypedDict):
    """Resource that represents a spreadsheet.

    Members:
        - **spreadsheetId** (str): The ID of the spreadsheet. This field is read-only.
        - **properties** (SpreadsheetProperties): Overall properties of the spreadsheet.
        - **sheets** (List[Sheet]): The sheets that are part of the spreadsheet.
        - **namedRanges** (List[NamedRange]): The named ranges defined in the spreadsheet.
        - **spreadsheetUrl** (str): The URL of the spreadsheet. This field is read-only.
        - **developerMetadata** (List[DeveloperMetadata]): The developer metadata associated with the spreadsheet.
        - **dataSources** (List[DataSource]): The external data sources associated with the spreadsheet.
        - **dataSourceSchedules** (List[DataSourceRefreshSchedule]): The data source refresh schedules associated with the spreadsheet. Output only.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets>`_
    """
    spreadsheetId: Optional[str]
    properties: Optional[SpreadsheetProperties]
    sheets: Optional[List[Sheet]]
    namedRanges: Optional[List[NamedRange]]
    spreadsheetUrl: Optional[str]
    developerMetadata: Optional[List[DeveloperMetadata]]
    dataSources: Optional[List[DataSource]]
    dataSourceSchedules: Optional[List[DataSourceRefreshSchedule]]

################################################################################
class SpreadsheetProperties(TypedDict):
    """Properties of a spreadsheet.

    Members:
        - **title** (str): The title of the spreadsheet.
        - **locale** (str): The locale of the spreadsheet in ISO 639-1 format. Can potentially be in other formats - consult documentation for more details.
        - **autoRecalc** (RecalculationInterval): The amount of time to wait before volatile functions are recalculated.
        - **timeZone** (str): The time zone of the spreadsheet, in CLDR format such as America/New_York. If the time zone isn't recognized, this may be a custom time zone such as GMT-07:00.
        - **defaultFormat** (CellFormat): The default format of all cells in the spreadsheet. CellData.effectiveFormat will not be set if the cell's format is equal to this default format. This field is read-only.
        - **iterativeCalculationSettings** (IterativeCalculationSettings): Determines whether and how circular references are resolved with iterative calculation. Absence of this field means that circular references result in calculation errors.
        - **spreadsheetTheme** (SpreadsheetTheme): The theme of the spreadsheet.
        - **importFunctionsExternalUrlAccessAllowed** (bool): Whether to allow external URL access for image and import functions. Read only when true. When false, you can set to true.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets#spreadsheetproperties>`_
    """
    title: str
    locale: str
    autoRecalc: RecalculationInterval
    timeZone: str
    defaultFormat: CellFormat
    iterativeCalculationSettings: IterativeCalculationSettings
    spreadsheetTheme: SpreadsheetTheme
    importFunctionsExternalUrlAccessAllowed: bool

################################################################################
class IterativeCalculationSettings(TypedDict):
    """Settings to control how circular dependencies are resolved with iterative calculation.

    Members:
        - **maxIterations** (int): When iterative calculation is enabled, the maximum number of calculation rounds to perform.
        - **convergenceThreshold** (float): When iterative calculation is enabled and successive results differ by less than this threshold value, the calculation rounds stop.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets#iterativecalculationsettings>`_
    """
    maxIterations: int
    convergenceThreshold: float

################################################################################
class SpreadsheetTheme(TypedDict):
    """Represents the theme of a spreadsheet.

    Members:
        - **primaryFontFamily** (str): The primary font family of the theme.
        - **themeColors** (List[ThemeColorPair]): The spreadsheet theme color pairs. To update you must provide all theme color pairs.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets#spreadsheettheme>`_
    """
    primaryFontFamily: str
    themeColors: List[ThemeColorPair]

################################################################################
class ThemeColorPair(TypedDict):
    """A pair mapping a spreadsheet theme color type to the concrete color it represents.

    Members:
        - **colorType** (ThemeColorType): The type of the spreadsheet theme color.
        - **color** (ColorStyle): The concrete color corresponding to the theme color type.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets#themecolorpair>`_
    """
    colorType: ThemeColorType
    color: ColorStyle

################################################################################
class NamedRange(TypedDict):
    """A named range.

    Members:
        - **namedRangeId** (str): The ID of the named range.
        - **name** (str): The name of the named range.
        - **range** (GridRange): The range that the named range refers to.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets#namedrange>`_
    """
    namedRangeId: str
    name: str
    range: GridRange

################################################################################
class DataSource(TypedDict):
    """Information about an external data source in the spreadsheet.

    Members:
        - **dataSourceId** (str): The spreadsheet-scoped unique ID that identifies the data source.
        - **spec** (DataSourceSpec): The DataSourceSpec for the data source connected with this spreadsheet.
        - **calculatedColumns** (List[DataSourceColumn]): All calculated columns in the data source.
        - **sheetId** (int): The ID of the Sheet connected with the data source. The field cannot be changed once set.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets#datasource>`_
    """
    dataSourceId: str
    spec: DataSourceSpec
    calculatedColumns: List[DataSourceColumn]
    sheetId: int

################################################################################
class _DataSourceSpecBase(TypedDict, total=False):
    parameters: List[DataSourceParameter]

class _DataSourceSpecBigQuery(_DataSourceSpecBase):
    bigQuery: BigQueryDataSourceSpec

class _DataSourceSpecCloudSQL(_DataSourceSpecBase):
    looker: LookerDataSourceSpec

DataSourceSpec = Union[_DataSourceSpecBigQuery, _DataSourceSpecCloudSQL]
"""This specifies the details of the data source.

Members:
    - **parameters** (List[DataSourceParameter]): The parameters of the data source, used when querying the data source.
    - **bigQuery** (BigQueryDataSourceSpec): A BigQuery data source.
    - **looker** (LookerDataSourceSpec): A Looker data source.

`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets#datasourcespec>`_
"""

################################################################################
class _BigQueryDataSourceSpecBase(TypedDict, total=False):
    projectId: str

class _BigQueryDataSourceSpecQuerySpec(_DataSourceSpecBase):
    querySpec: BigQueryQuerySpec

class _BigQueryDataSourceSpecTableSpec(_DataSourceSpecBase):
    tableSpec: BigQueryTableSpec

BigQueryDataSourceSpec = Union[
    _BigQueryDataSourceSpecQuerySpec,
    _BigQueryDataSourceSpecTableSpec,
]
"""The representation of a BigQuery data source that's connected to a sheet.

Members:
    - **projectId** (str): The ID of a BigQuery enabled Google Cloud project with a billing account attached. 
    - **querySpec** (BigQueryQuerySpec): A BigQueryQuerySpec.
    - **tableSpec** (BigQueryTableSpec): A BigQueryTableSpec.

`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets#bigquerydatasourcespec>`_
"""

################################################################################
class BigQueryQuerySpec(TypedDict):
    """Specifies a custom BigQuery query.

    Members:
        - **rawQuery** (str): The raw query string.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets#bigqueryqueryspec>`_
    """
    rawQuery: str

################################################################################
class BigQueryTableSpec(TypedDict):
    """Specifies a BigQuery table definition. Only native tables are allowed.

    Members:
        - **tableProjectId** (str): The ID of a BigQuery project the table belongs to. If not specified, the projectId is assumed.
        - **tableId** (str): The BigQuery table id.
        - **datasetId** (str): The BigQuery dataset id.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets#bigquerytablespec>`_
    """
    tableProjectId: str
    tableId: str
    datasetId: str

################################################################################
class LookerDataSourceSpec(TypedDict):
    """The representation of a Looker data source.

    Members:
        - **lookerInstanceUrl** (str): A Looker instance URL.
        - **model** (str): Name of a Looker model.
        - **explore** (str): Name of a Looker model explore.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets#lookerdatasourcespec>`_
    """
    instanceUrl: str
    model: str
    explore: str

################################################################################
class _DataSourceParameterBase(TypedDict, total=False):
    name: str

class _DataSourceParameterNamedRange(_DataSourceParameterBase):
    namedRangeId: str

class _DataSourceParameterRange(_DataSourceParameterBase):
    range: GridRange

DataSourceParameter = Union[_DataSourceParameterNamedRange, _DataSourceParameterRange]
"""A parameter in a data source's query. The parameter allows the user to pass in values from the spreadsheet into a query.

Members:
    - **name** (str): Named parameter. Must be a legitimate identifier for the DataSource that supports it.
    - **namedRangeId** (str): ID of a NamedRange. Its size must be 1x1.
    - **range** (GridRange): A range that contains the value of the parameter. Its size must be 1x1.

`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets#datasourceparameter>`_
"""

################################################################################
class _DataSourceRefreshScheduleBase(TypedDict, total=False):
    enabled: bool
    refreshScope: DataSourceRefreshScope
    nextRun: Interval

class _DataSourceRefreshScheduleDaily(_DataSourceRefreshScheduleBase):
    dailySchedule: DataSourceRefreshDailySchedule

class _DataSourceRefreshScheduleWeekly(_DataSourceRefreshScheduleBase):
    weeklySchedule: DataSourceRefreshWeeklySchedule

class _DataSourceRefreshScheduleMonthly(_DataSourceRefreshScheduleBase):
    monthlySchedule: DataSourceRefreshMonthlySchedule

DataSourceRefreshSchedule = Union[
    _DataSourceRefreshScheduleDaily,
    _DataSourceRefreshScheduleWeekly,
    _DataSourceRefreshScheduleMonthly,
]
"""Schedule for refreshing the data source.

Members:
    - **enabled** (bool): True if the refresh schedule is enabled, or false otherwise.
    - **refreshScope** (DataSourceRefreshScope): The scope of the refresh. Must be ALL_DATA_SOURCES.
    - **nextRun** (Interval): Output only. The time interval of the next run.
    - **dailySchedule** (DataSourceRefreshDailySchedule): A daily refresh schedule.
    - **weeklySchedule** (DataSourceRefreshWeeklySchedule): A weekly refresh schedule.
    - **monthlySchedule** (DataSourceRefreshMonthlySchedule): A monthly refresh schedule.

`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets#datasourcerefreshschedule>`_
"""

################################################################################
class DataSourceRefreshDailySchedule(TypedDict):
    """A schedule for data to refresh every day in a given time interval.

    Members:
        - **startTime** (TimeOfDay): The start time of a time interval in which a data source refresh is scheduled. Only hours part is used. The time interval size defaults to that in the Sheets editor.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets#datasourcerefreshdailyschedule>`_
    """
    startTime: TimeOfDay

################################################################################
class TimeOfDay(TypedDict):
    """Represents a time of day.

    Members:
        - **hours** (int): Hours of a day in 24 hour format. Must be greater than or equal to 0 and typically must be less than or equal to 23.
        - **minutes** (int): Minutes of an hour. Must be greater than or equal to 0 and less than or equal to 59.
        - **seconds** (int): Seconds of a minute. Must be greater than or equal to 0 and typically must be less than or equal to 59.
        - **nanos** (int): Fractions of seconds, in nanoseconds. Must be greater than or equal to 0 and less than or equal to 999,999,999.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets#timeofday>`_
    """
    hours: int
    minutes: int
    seconds: int
    nanos: int

################################################################################
class DataSourceRefreshWeeklySchedule(TypedDict):
    """A weekly schedule for data to refresh on specific days in a given time interval.

    Members:
        - **startTime** (TimeOfDay): The start time of a time interval in which a data source refresh is scheduled.
        - **daysOfWeek** (List[DayOfWeek]): Days of the week to refresh. At least one day must be specified.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets#datasourcerefreshweeklyschedule>`_
    """
    startTime: TimeOfDay
    daysOfWeek: List[DayOfWeek]

################################################################################
class DataSourceRefreshMonthlySchedule(TypedDict):
    """A monthly schedule for data to refresh on specific days in the month in a given time interval.

    Members:
        - **startTime** (TimeOfDay): The start time of a time interval in which a data source refresh is scheduled.
        - **daysOfMonth** (List[int]): Days of the month to refresh. Only 1-28 are supported, mapping to the 1st to the 28th day. At least one day must be specified.
    """
    startTime: TimeOfDay
    daysOfMonth: List[int]

################################################################################
class Interval(TypedDict):
    """Represents a time interval, encoded as a Timestamp start (inclusive) and
    a Timestamp end (exclusive).

    The start must be less than or equal to the end. When the start equals the
    end, the interval is empty (matches no time). When both start and end are
    unspecified, the interval matches any time.

    Members:
        - **startTime** (str): Inclusive. If specified, a Timestamp matching this interval will have to be the same or after the start.
        - **endTime** (str): Exclusive. If specified, a Timestamp matching this interval will have to be before the end.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets#interval>`_
    """
    startTime: NotRequired[str]
    endTime: NotRequired[str]

################################################################################
