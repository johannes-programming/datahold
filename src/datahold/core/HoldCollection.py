"""Provide HoldCollection."""

__all__: list[str] = ["HoldCollection"]

from ..base.BaseHoldCollection import BaseHoldCollection
from .DataCollection import DataCollection


class HoldCollection[Item](DataCollection[Item], BaseHoldCollection[Item]):
    __slots__ = ()
