from typing import *
from .HoldObject import HoldObject
from .BaseHoldSet import BaseHoldSet
from .DataSet import DataSet
import setdoc
__all__ = ["HoldSet"]

Item = TypeVar("Item")

class HoldSet(HoldObject, BaseHoldSet[Item], DataSet[Item]):
    data:frozenset[Item]
    __slots__ = ()
    @property
    @setdoc.basic
    def data(self:Self) -> frozenset[Item]:
        return self._data
    @data.setter
    def data(self:Self, value:Any) -> None:
        self._data = frozenset[Item](value)

