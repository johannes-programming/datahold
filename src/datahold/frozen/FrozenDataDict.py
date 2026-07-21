"""Provide FrozenDataDict."""

__all__: list[str] = ["FrozenDataDict"]

from ..base.BaseDataDict import BaseDataDict
from .FrozenDataCollection import FrozenDataCollection


class FrozenDataDict[Key, Value](
    BaseDataDict[Key, Value],
    FrozenDataCollection[Key | str],
):
    __slots__ = ()
