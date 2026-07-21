"""Provide BaseHoldDict."""

__all__: list[str] = ["BaseHoldDict"]

from .BaseDataDict import BaseDataDict
from .BaseHoldCollection import BaseHoldCollection


class BaseHoldDict[Key, Value](
    BaseDataDict[Key, Value],
    BaseHoldCollection[Key],
):
    __slots__ = ()
