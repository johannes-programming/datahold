
from .FrozenDataSet import FrozenDataSet
from .BaseHoldSet import BaseHoldSet
from .FrozenHoldObject import FrozenHoldObject
from typing import *
import setdoc

__all__ = ["FrozenHoldSet"]

Item = TypeVar("Item")

class FrozenHoldSet(BaseHoldSet[Item], FrozenDataSet, FrozenHoldObject):
    data:frozenset[Item]
    __slots__ = ()
    @setdoc.basic
    def __init__(self:Self, data:Iterable, /)->None:
        self._data = frozenset[Item](data)
