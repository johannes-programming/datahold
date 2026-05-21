from typing import *

import setdoc
import types
from .BaseHoldDict import BaseHoldDict
from .DataDict import DataDict
from .HoldObject import HoldObject

__all__ = ["HoldDict"]

Key = TypeVar("Key")
Value = TypeVar("Value")


class HoldDict(HoldObject, DataDict[Key, Value], BaseHoldDict[Key, Value]):

    __slots__ = ()

    @property
    @setdoc.basic
    def data(self: Self) -> types.MappingProxyType[Key, Value]:
        return self._data

    @data.setter
    def data(self: Self, value: Any) -> None:
        self._data = types.MappingProxyType[Key, Value](value)
