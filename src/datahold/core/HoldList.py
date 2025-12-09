from typing import *
from .HoldObject import HoldObject
from .BaseHoldList import BaseHoldList
from .DataList import DataList
import setdoc
__all__ = ["HoldList"]

Item = TypeVar("Item")

class HoldList(HoldObject, BaseHoldList[Item, ...], DataList[Item, ...]):
    data:tuple[Item, ...]
    __slots__ = ()
    @property
    @setdoc.basic
    def data(self:Self) -> tuple[Item, ...]:
        return self._data
    @data.setter
    def data(self:Self, value:Any) -> None:
        self._data = tuple[Item, ...](value)

