# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from enum import Enum
from typing import Any, List, Optional, Union

from grafanapy.utils import MyBaseModel
from pydantic import Field, confloat, conint


class HideSeriesConfig(MyBaseModel):
    tooltip: bool
    legend: bool
    viz: bool


class HideableFieldConfig(MyBaseModel):
    hideFrom: Optional[HideSeriesConfig] = None


class LegendDisplayMode(Enum):
    list = "list"
    table = "table"
    hidden = "hidden"


class LegendPlacement(Enum):
    bottom = "bottom"
    right = "right"


class SortOrder(Enum):
    asc = "asc"
    desc = "desc"
    none = "none"


class PanelFieldConfig(HideableFieldConfig):
    lineWidth: Optional[conint(ge=0, le=10)] = 1
    fillOpacity: Optional[conint(ge=0, le=100)] = 70


class TimeZoneEnum(Enum):
    utc = "utc"


class TimeZone(MyBaseModel):
    __root__: Optional[Union[TimeZoneEnum, Any]] = Field(
        "browser",
        description="A specific timezone from https://en.wikipedia.org/wiki/Tz_database",
    )


class TooltipDisplayMode(Enum):
    single = "single"
    multi = "multi"
    none = "none"


class VisibilityMode(Enum):
    auto = "auto"
    never = "never"
    always = "always"


class VizLegendOptions(MyBaseModel):
    displayMode: LegendDisplayMode
    placement: LegendPlacement
    showLegend: bool
    asTable: Optional[bool] = None
    isVisible: Optional[bool] = None
    sortBy: Optional[str] = None
    sortDesc: Optional[bool] = None
    width: Optional[float] = None
    calcs: List[str]


class VizTooltipOptions(MyBaseModel):
    mode: TooltipDisplayMode
    sort: SortOrder


class OptionsWithLegend(MyBaseModel):
    legend: VizLegendOptions


class OptionsWithTimezones(MyBaseModel):
    timezone: Optional[List[TimeZone]] = None


class OptionsWithTooltip(MyBaseModel):
    tooltip: VizTooltipOptions


class PanelOptions(OptionsWithLegend, OptionsWithTooltip, OptionsWithTimezones):
    rowHeight: confloat(ge=0.0, le=1.0) = Field(
        ..., description="Set the height of the rows"
    )
    showValue: VisibilityMode = Field(..., description="Show values on the columns")
    colWidth: Optional[confloat(le=1.0)] = Field(
        0.9, description="Controls the column width"
    )


class StatusHistoryPanelCfg(MyBaseModel):
    PanelOptions: PanelOptions
    PanelFieldConfig: PanelFieldConfig
