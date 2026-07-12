from ..base.BaseDataList import BaseDataList
from typing import TypeVar, Self
from collections.abc import Iterable
from .FrozenHoldFgettable import FrozenHoldFgettable
import setdoc

Item = TypeVar("Item", covariant=True)
class FrozenHoldSet(FrozenHoldFgettable[tuple[Item, ...]], BaseDataList[Item]):
    __slots__ = ()
    @setdoc.basic
    def __fset__(self:Self, data:Iterable[Item]) -> None:
        self._data = tuple(data)