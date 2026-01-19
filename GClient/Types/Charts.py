from __future__ import annotations

from typing import TYPE_CHECKING, TypedDict, Union, NotRequired, List

from .Enums import *

if TYPE_CHECKING:
    from .Other import (
        EmbeddedObjectPosition, ColorStyle, TextFormat, FilterSpec,
        SortSpec, DataExecutionStatus,
    )
################################################################################
class EmbeddedChart(TypedDict):
    """A chart embedded in a sheet.

    Members:
        - **chartId** (int): The ID of the chart.
        - **spec** (ChartSpec): The specifications of the chart.
        - **position** (EmbeddedObjectPosition): The position of the chart.
        - **border** (EmbeddedObjectBorder): The border of the chart.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/charts#embeddedchart>`_
    """
    pass
    # chartId: int
    # spec: ChartSpec
    # position: EmbeddedObjectPosition
    # border: EmbeddedObjectBorder

################################################################################
class _ChartSpecBase(TypedDict, total=False):
    title: str
    altText: str
    titleTextFormat: TextFormat
    titleTextPosition: TextPosition
    subtitle: str
    subtitleTextFormat: TextFormat
    subtitleTextPosition: TextPosition
    fontName: str
    maximized: bool
    backgroundColorStyle: ColorStyle
    dataSourceChartProperties: NotRequired[DataSourceChartProperties]
    filterSpecs: List[FilterSpec]
    sortSpecs: List[SortSpec]
    hiddenDimensionStrategy: ChartHiddenDimensionStrategy

class _ChartSpecWithBasicChart(_ChartSpecBase):
    basicChart: BasicChart
    pieChart: NotRequired[None]
    bubbleChart: NotRequired[None]
    candlestickChart: NotRequired[None]
    orgChart: NotRequired[None]
    histogramChart: NotRequired[None]
    waterfallChart: NotRequired[None]
    treemapChart: NotRequired[None]
    scorecardChart: NotRequired[None]

class _ChartSpecWithPieChart(_ChartSpecBase):
    basicChart: NotRequired[None]
    pieChart: PieChart
    bubbleChart: NotRequired[None]
    candlestickChart: NotRequired[None]
    orgChart: NotRequired[None]
    histogramChart: NotRequired[None]
    waterfallChart: NotRequired[None]
    treemapChart: NotRequired[None]
    scorecardChart: NotRequired[None]

class _ChartSpecWithBubbleChart(_ChartSpecBase):
    basicChart: NotRequired[None]
    pieChart: NotRequired[None]
    bubbleChart: BubbleChart
    candlestickChart: NotRequired[None]
    orgChart: NotRequired[None]
    histogramChart: NotRequired[None]
    waterfallChart: NotRequired[None]
    treemapChart: NotRequired[None]
    scorecardChart: NotRequired[None]

class _ChartSpecWithCandlestickChart(_ChartSpecBase):
    basicChart: NotRequired[None]
    pieChart: NotRequired[None]
    bubbleChart: NotRequired[None]
    candlestickChart: CandlestickChart
    orgChart: NotRequired[None]
    histogramChart: NotRequired[None]
    waterfallChart: NotRequired[None]
    treemapChart: NotRequired[None]
    scorecardChart: NotRequired[None]

class _ChartSpecWithOrgChart(_ChartSpecBase):
    basicChart: NotRequired[None]
    pieChart: NotRequired[None]
    bubbleChart: NotRequired[None]
    candlestickChart: NotRequired[None]
    orgChart: OrgChart
    histogramChart: NotRequired[None]
    waterfallChart: NotRequired[None]
    treemapChart: NotRequired[None]
    scorecardChart: NotRequired[None]

class _ChartSpecWithHistogramChart(_ChartSpecBase):
    basicChart: NotRequired[None]
    pieChart: NotRequired[None]
    bubbleChart: NotRequired[None]
    candlestickChart: NotRequired[None]
    orgChart: NotRequired[None]
    histogramChart: HistogramChart
    waterfallChart: NotRequired[None]
    treemapChart: NotRequired[None]
    scorecardChart: NotRequired[None]

class _ChartSpecWithWaterfallChart(_ChartSpecBase):
    basicChart: NotRequired[None]
    pieChart: NotRequired[None]
    bubbleChart: NotRequired[None]
    candlestickChart: NotRequired[None]
    orgChart: NotRequired[None]
    histogramChart: NotRequired[None]
    waterfallChart: WaterfallChart
    treemapChart: NotRequired[None]
    scorecardChart: NotRequired[None]

class _ChartSpecWithTreemapChart(_ChartSpecBase):
    basicChart: NotRequired[None]
    pieChart: NotRequired[None]
    bubbleChart: NotRequired[None]
    candlestickChart: NotRequired[None]
    orgChart: NotRequired[None]
    histogramChart: NotRequired[None]
    waterfallChart: NotRequired[None]
    treemapChart: TreemapChart
    scorecardChart: NotRequired[None]

class _ChartSpecWithScorecardChart(_ChartSpecBase):
    basicChart: NotRequired[None]
    pieChart: NotRequired[None]
    bubbleChart: NotRequired[None]
    candlestickChart: NotRequired[None]
    orgChart: NotRequired[None]
    histogramChart: NotRequired[None]
    waterfallChart: NotRequired[None]
    treemapChart: NotRequired[None]
    scorecardChart: ScorecardChart

ChartSpec = Union[
    _ChartSpecWithBasicChart,
    _ChartSpecWithPieChart,
    _ChartSpecWithBubbleChart,
    _ChartSpecWithCandlestickChart,
    _ChartSpecWithOrgChart,
    _ChartSpecWithHistogramChart,
    _ChartSpecWithWaterfallChart,
    _ChartSpecWithTreemapChart,
    _ChartSpecWithScorecardChart,
]
"""The specifications of a chart.

Members:
    - **title** (str): The title of the chart.
    - **altText** (str): A description of the chart for accessibility.
    - **titleTextFormat** (TextFormat): The format of the chart title.
    - **titleTextPosition** (TextPosition): The position of the chart title.
    - **subtitle** (str): The subtitle of the chart.
    - **subtitleTextFormat** (TextFormat): The format of the chart subtitle.
    - **subtitleTextPosition** (TextPosition): The position of the chart subtitle.
    - **fontName** (str): The font name to use by default for all text in the chart.
    - **maximized** (bool): True to make the chart fill the entire space in which it's placed.
    - **backgroundColorStyle** (ColorStyle): The background color of the entire chart. Not applicable to Org charts.
    - **dataSourceChartProperties** (DataSourceChartProperties): If present, the field contains data source chart specific properties.
    - **filterSpecs** (List[FilterSpec]): The filters applied to the source data of the chart. Only supported for data source charts.
    - **sortSpecs** (List[SortSpec]): The order to sort the chart data by. Only a single sort spec is supported. Only supported for data source charts.
    - **hiddenDimensionStrategy** (ChartHiddenDimensionStrategy): Determines how the charts will use hidden rows or columns.
    - **basicChart** (BasicChart): A basic chart.
    - **pieChart** (PieChart): A pie chart.
    - **bubbleChart** (BubbleChart): A bubble chart.
    - **candlestickChart** (CandlestickChart): A candlestick chart.
    - **orgChart** (OrgChart): An organizational chart.
    - **histogramChart** (HistogramChart): A histogram chart.
    - **waterfallChart** (WaterfallChart): A waterfall chart.
    - **treemapChart** (TreemapChart): A treemap chart.
    - **scorecardChart** (ScorecardChart): A scorecard chart.

`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/charts#chartspec>`_
"""

################################################################################
class TextPosition(TypedDict):
    """Position settings for text.

    Members:
        - **horizontalAlignment** (HorizontalAlignment): The horizontal alignment of the text box within the chart.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/charts#textposition>`_
    """
    horizontalAlignment: HorizontalAlign

################################################################################
class DataSourceChartProperties(TypedDict):
    """Properties specific to data source charts.

    Members:
        - **dataSourceId** (str): The ID of the data source.
        - **dataExecutionStatus** (DataExecutionStatus): Output only. The data execution status.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/charts#datasourcechartproperties>`_
    """
    dataSourceId: str
    dataExecutionStatus: DataExecutionStatus

################################################################################
class BasicChartSpec(TypedDict):
    """The specification for a basic chart.

    See ``BasicChartType`` for the list of charts this supports.

    Members:
        - **chartType** (BasicChartType): The type of chart.
        - **legendPosition** (BasicChartLegendPosition): The position of the chart legend.
        - **axis** (List[BasicChartAxis]): The axis details of the chart.
        - **domains** (List[BasicChartDomain]): The domain of data this is charting. Only a single domain is supported.
        - **series** (List[BasicChartSeries]): The data this chart is visualizing.
        - **headerCount** (int): The number of rows or columns in the data that are "headers". If not set, Google Sheets will guess how many rows are headers based on the data.
        - **threeDimensional** (bool): True to make the chart 3D. Applies to Bar and Column charts.
        - **interpolateNulls** (bool): If some values in a series are missing, gaps may appear in the chart (e.g, segments of lines in a line chart will be missing). To eliminate these gaps set this to true. Applies to Line, Area, and Combo charts.
        - **stackedType** (BasicChartStackedType): The stacked type for charts that support vertical stacking. Applies to Area, Bar, Column, Combo, and Stepped Area charts.
        - **lineSmoothing** (bool): Gets whether all lines should be rendered smooth or straight by default. Applies to Line charts.
        - **compareMode** (BasicChartCompareMode): The behavior of tooltips and data highlighting when hovering on data and chart area.
        - **totalDataLabel** (DataLabel): Controls whether to display additional data labels on stacked charts which sum the total value of all stacked values at each value along the domain axis.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/charts#basicchartspec>`_
    """
    chartType: BasicChartType
    legendPosition: BasicChartLegendPosition
    axis: List[BasicChartAxis]
    domains: List[BasicChartDomain]
    series: List[BasicChartSeries]
    headerCount: int
    threeDimensional: bool
    interpolateNulls: bool
    stackedType: BasicChartStackedType
    lineSmoothing: bool
    compareMode: BasicChartCompareMode
    totalDataLabel: DataLabel

################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
