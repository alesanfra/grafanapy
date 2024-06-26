# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from enum import Enum

from grafanapy.utils import MyBaseModel


class LogsDedupStrategy(Enum):
    none = "none"
    exact = "exact"
    numbers = "numbers"
    signature = "signature"


class LogsSortOrder(Enum):
    Descending = "Descending"
    Ascending = "Ascending"


class PanelOptions(MyBaseModel):
    showLabels: bool
    showCommonLabels: bool
    showTime: bool
    wrapLogMessage: bool
    prettifyLogMessage: bool
    enableLogDetails: bool
    sortOrder: LogsSortOrder
    dedupStrategy: LogsDedupStrategy


class LogsPanelCfg(MyBaseModel):
    PanelOptions: PanelOptions
