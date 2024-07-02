"""Panda-Helper is a simple data-profiling utility for Pandas' DataFrames and Series."""

from __future__ import annotations
from pandahelper.reports import DataFrameProfile, SeriesProfile, frequency_table


__version__ = "0.0.3"
__all__ = ["DataFrameProfile", "SeriesProfile", "frequency_table"]
