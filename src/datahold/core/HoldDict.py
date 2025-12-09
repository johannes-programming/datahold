from typing import *
from .HoldObject import HoldObject
from .BaseHoldDict import BaseHoldDict
from .DataDict import DataDict
from frozendict import frozendict
import setdoc
__all__ = ["HoldDict"]

Key = TypeVar("Key")
Value = TypeVar("Value")

class HoldDict(HoldObject, BaseHoldDict[Key, Value], DataDict[Key, Value]):
    data:frozendict[Key, Value]
    __slots__ = ()
    @property
    @setdoc.basic
    def data(self:Self) -> frozendict[Key, Value]:
        return self._data
    @data.setter
    def data(self:Self, value:Any) -> None:
        self._data = frozendict[Key, Value](value)

