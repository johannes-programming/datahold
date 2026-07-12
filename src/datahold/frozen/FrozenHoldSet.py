from ..base.BaseDataSet import BaseDataSet
from typing import TypeVar, Self
from collections.abc import Iterable
from .FrozenHoldFgettable import FrozenHoldFgettable
import setdoc

Item = TypeVar("Item", covariant=True)
class FrozenHoldSet(FrozenHoldFgettable[frozenset[Item]], BaseDataSet[Item]):
    __slots__ = ()
    @setdoc.basic
    def __fset__(self:Self, data:Iterable[Item]) -> None:
        self._data = frozenset(data)