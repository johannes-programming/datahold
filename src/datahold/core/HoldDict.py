from typing import Any, Self, TypeVar

import setdoc
from frozendict import frozendict

from ..base.BaseHoldDict import BaseHoldDict
from .DataDict import DataDict
from .HoldObject import HoldObject

__all__ = ["HoldDict"]

Key = TypeVar("Key")
Value = TypeVar("Value")


class HoldDict(HoldObject, DataDict[Key, Value], BaseHoldDict[Key, Value]):

    __slots__ = ()

    @property
    @setdoc.basic
    def data(self: Self) -> Any:
        return self._data

    @data.setter
    def data(
        self: Self,
        value: Any,
    ) -> None:
        self._data = frozendict(value)
