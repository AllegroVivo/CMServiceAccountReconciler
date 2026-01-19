from __future__ import annotations

from typing import TYPE_CHECKING, TypedDict, Union, NotRequired, List

from .Enums import *

if TYPE_CHECKING:
    from .Other import (
        GridRange, DataExecutionStatus, DataSourceColumnReference,
        ExtendedValue, BooleanCondition,
    )
################################################################################
class _PivotTableBase(TypedDict, total=False):
    rows: List[PivotGroup]
    columns: List[PivotGroup]
    filterSpecs: List[PivotFilterSpec]
    values: List[PivotValue]
    valueLayout: PivotValueLayout
    dataExecutionStatus: DataExecutionStatus

class _PivotTableBySourceRange(_PivotTableBase):
    source: GridRange
    dataSourceId: NotRequired[None]

class _PivotTableByDataSourceId(_PivotTableBase):
    source: NotRequired[None]
    dataSourceId: str

PivotTable = Union[_PivotTableBySourceRange, _PivotTableByDataSourceId]
"""A pivot table.

Members:
    - **rows** (List[PivotGroup]): The row groups in the pivot table.
    - **columns** (List[PivotGroup]): The column groups in the pivot table.
    - **filterSpecs** (List[PivotFilterSpec]): The filters applied to the source columns before aggregating data for the pivot table.
    - **values** (List[PivotValue]): A list of values to include in the pivot table.
    - **valueLayout** (PivotValueLayout): Whether values should be listed horizontally (as columns) or vertically (as rows).
    - **dataExecutionStatus** (DataExecutionStatus): Output only. The data execution status for data source pivot tables.
    - **source** (GridRange): The range the pivot table is reading data from.
    - **dataSourceId** (str): The ID of the data source the pivot table is reading data from.

`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/pivot-tables#pivottable>`_
"""

################################################################################
class _PivotGroupBase(TypedDict, total=False):
    showTotals: bool
    valueMetadata: List[PivotGroupValueMetadata]
    sortOrder: SortOrder
    valueBucket: PivotGroupSortValueBucket
    repeatHeadings: bool
    label: str
    groupRule: PivotGroupRule
    groupLimit: PivotGroupLimit

class _PivotGroupBySourceColumn(_PivotGroupBase):
    sourceColumnOffset: int
    dataSourceColumnReference: NotRequired[None]

class _PivotGroupByDataSourceColumn(_PivotGroupBase):
    sourceColumnOffset: NotRequired[None]
    dataSourceColumnReference: DataSourceColumnReference

PivotGroup = Union[_PivotGroupBySourceColumn, _PivotGroupByDataSourceColumn]
"""A group in a pivot table.

Members:
    - **showTotals** (bool): True if the pivot table should include the totals for this grouping.
    - **valueMetadata** (List[PivotGroupValueMetadata]): Metadata about the values in this group.
    - **sortOrder** (SortOrder): The order in which items in this group should be sorted.
    - **valueBucket** (PivotGroupSortValueBucket): The bucket of the opposite pivot group to sort by. If not specified, sorting is alphabetical by this group's values.
    - **repeatHeadings** (bool): True if the headings in this pivot group should be repeated. This is only valid for row groupings and is ignored by columns.
    - **label** (str): The labels to use for the row/column groups which can be customized. 
    - **groupRule** (PivotGroupRule): The group rule to apply to this row/column group.
    - **groupLimit** (PivotGroupLimit): The count limit on rows or columns to apply to this pivot group.
    - **sourceColumnOffset** (int): The column offset of the source range that this grouping is based on. For example, if the source was ``C10:E15``, a sourceColumnOffset of ``0`` means this group refers to column ``C``, whereas the offset ``1`` would refer to column ``D``.
    - **dataSourceColumnReference** (DataSourceColumnReference): The reference to the data source column this grouping is based on.

`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/pivot-tables#pivotgroup>`_
"""

################################################################################
class PivotGroupValueMetadata(TypedDict):
    """Metadata about a value in a pivot grouping.

    Members:
        - **value** (ExtendedValue): The calculated value the metadata corresponds to. (Note that ``formulaValue`` is not valid, because the values will be calculated.)
        - **collapsed** (bool): True if the data corresponding to the value is collapsed.
    """
    value: ExtendedValue
    collapsed: bool

################################################################################
class PivotGroupSortValueBucket(TypedDict):
    """Information about which values in a pivot group should be used for sorting.

    Members:
        - **valuesIndex** (int): The offset in the ``PivotTable.values`` list which the values in this grouping should be sorted by.
        - **buckets** (List[ExtendedValue]): Determines the bucket from which values are chosen to sort.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/pivot-tables#pivotgroupsortvaluebucket>`_
    """
    valuesIndex: int
    buckets: List[ExtendedValue]

################################################################################
class _PivotGroupRuleManual(TypedDict):
    manualRule: ManualRule
    histogramRule: NotRequired[None]
    dateTimeRule: NotRequired[None]

class _PivotGroupRuleHistogram(TypedDict):
    manualRule: NotRequired[None]
    histogramRule: HistogramRule
    dateTimeRule: NotRequired[None]

class _PivotGroupRuleDateTime(TypedDict):
    manualRule: NotRequired[None]
    histogramRule: NotRequired[None]
    dateTimeRule: DateTimeRule

PivotGroupRule = Union[_PivotGroupRuleManual, _PivotGroupRuleHistogram, _PivotGroupRuleDateTime]
"""An optional setting on a PivotGroup that defines buckets for the values in the source data 
column rather than breaking out each individual value. 

Only one PivotGroup with a group rule may be added for each column in the source 
data, though on any given column you may add both a PivotGroup that has a rule 
and a PivotGroup that does not.

Members:
    - **manualRule** (ManualRule): A rule that buckets values based on a series of manual ranges.
    - **histogramRule** (HistogramRule): A rule that buckets values based on a histogram.
    - **dateTimeRule** (DateTimeRule): A rule that buckets date/time values based on a series of calendar units.

`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/pivot-tables#pivotgrouprule>`_
"""

################################################################################
class ManualRule(TypedDict):
    """Allows you to manually organize the values in a source data column into
    buckets with names of your choosing.

    Members:
        - **groups** (List[ManualGroupRule]): The list of group names and the corresponding items from the source data that map to each group name.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/pivot-tables#manualrule>`_
    """
    groups: List[ManualRuleGroup]

################################################################################
class ManualRuleGroup(TypedDict):
    """A group name and a list of items from the source data that should be
    placed in the group with this name.

    Members:
        - **groupName** (ExtendedValue): The group name, which must be a string. Each group in a given ``ManualRule`` must have a unique group name.
        - **items** (List[ExtendedValue]): The items in the source data that should be placed into this group. Each item may be a string, number, or boolean. Items may appear in at most one group within a given ``ManualRule``. Items that do not appear in any group will appear on their own.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/pivot-tables#manualrulegroup>`_
    """
    groupName: ExtendedValue
    items: List[ExtendedValue]

################################################################################
class HistogramRule(TypedDict):
    """Allows you to organize the numeric values in a source data column into
    buckets of a constant size.

    Members:
        - **interval** (float): The size of the buckets that are created. Must be positive.
        - **start** (float): The minimum value at which items are placed into buckets of constant size. Values below start are lumped into a single bucket. This field is optional.
        - **end** (float): The maximum value at which items are placed into buckets of constant size. Values above end are lumped into a single bucket. This field is optional.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/pivot-tables#histogramrule>`_
    """
    interval: float
    start: NotRequired[float]
    end: NotRequired[float]

################################################################################
class DateTimeRule(TypedDict):
    """Allows you to organize the date-time values in a source data column
    into buckets based on selected parts of their date or time values.

    Members:
        - **type** (DateTimeRuleType): The type of date-time grouping to apply.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/pivot-tables#datetimerule>`_
    """
    type: DateTimeRuleType

################################################################################
class PivotGroupLimit(TypedDict):
    """The count limit on rows or columns in the pivot group.

    Members:
        - **countLimit** (int): The maximum number of rows or columns to show from this group.
        - **applyOrder** (int): The order in which the limit is applied to the pivot table.

    `Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/pivot-tables#pivotgrouplimit>`_
    """
    countLimit: int
    applyOrder: int

################################################################################
class PivotFilterCriteria(TypedDict):
    """Criteria for showing/hiding rows in a pivot table.

    Members:
        - **visibleValues** (List[str]): Values that should be included. Values not listed here are excluded.
        - **condition** (BooleanCondition): A condition that must be true for values to be shown.
        - **visibleByDefault** (bool): Whether values are visible by default. If true, the ``visibleValues`` are ignored, all values that meet ``condition`` (if specified) are shown. If false, values that are both in ``visibleValues`` and meet ``condition`` are shown.
    """
    visibleValues: List[str]
    condition: BooleanCondition
    visibleByDefault: bool

################################################################################
class _PivotFilterSpecBase(TypedDict, total=False):
    filterCriteria: PivotFilterCriteria

class _PivotFilterSpecByColumnOffset(_PivotFilterSpecBase):
    columnOffsetIndex: int
    dataSourceColumnReference: NotRequired[None]

class _PivotFilterSpecByDataSourceColumn(_PivotFilterSpecBase):
    columnOffsetIndex: NotRequired[None]
    dataSourceColumnReference: DataSourceColumnReference

PivotFilterSpec = Union[_PivotFilterSpecByColumnOffset, _PivotFilterSpecByDataSourceColumn]
"""The pivot table filter criteria associated with a specific source column offset.

Members:
    - **filterCriteria** (PivotFilterCriteria): The criteria for filtering the column.
    - **columnOffsetIndex** (int): The zero-based column offset of the source range.
    - **dataSourceColumnReference** (DataSourceColumnReference): The reference to the data source column.
    
`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/pivot-tables#pivotfilterspec>`_
"""

################################################################################
class _PivotValueBase(TypedDict, total=False):
    summarizeFunction: PivotValueSummarizeFunction
    name: str
    calculatedDisplayType: PivotValueCalculatedDisplayType

class _PivotValueBySourceColumn(_PivotValueBase):
    sourceColumnOffset: int
    formula: NotRequired[None]
    dataSourceColumnReference: NotRequired[None]

class _PivotValueByFormula(_PivotValueBase):
    sourceColumnOffset: NotRequired[None]
    formula: str
    dataSourceColumnReference: NotRequired[None]

class _PivotValueByDataSourceColumn(_PivotValueBase):
    sourceColumnOffset: NotRequired[None]
    formula: NotRequired[None]
    dataSourceColumnReference: DataSourceColumnReference

PivotValue = Union[
    _PivotValueBySourceColumn,
    _PivotValueByFormula,
    _PivotValueByDataSourceColumn
]
"""The definition of how a value in a pivot table should be calculated.

Members:
    - **summarizeFunction** (PivotValueSummarizeFunction): A function to summarize the value. If ``formula`` is set, the only supported values are ``SUM`` and ``CUSTOM``. If ``sourceColumnOffset`` is set, then ``CUSTOM`` is not supported.
    - **name** (str): A name to use for the value. This is used when displaying the value in the UI.
    - **calculatedDisplayType** (PivotValueCalculatedDisplayType): If specified, indicates that pivot values should be displayed as the result of a calculation with another pivot value. 
    - **sourceColumnOffset** (int): The column offset of the source range that this value reads from.
    - **formula** (str): A custom formula to calculate the value. The formula must start with an equals sign ('=').
    - **dataSourceColumnReference** (DataSourceColumnReference): The reference to the data source column this value is based on.
    
`Google API reference <https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/pivot-tables#pivotvalue>`_
"""

################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
