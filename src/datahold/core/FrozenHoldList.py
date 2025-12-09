
from .FrozenDataList import FrozenDataList
from .BaseHoldList import BaseHoldList
from .FrozenHoldObject import FrozenHoldObject
from typing import *
import setdoc

__all__ = ["FrozenHoldList"]

Item = TypeVar("Item")

class FrozenHoldList(BaseHoldList[Item], FrozenDataList, FrozenHoldObject):
    data:tuple[Item, ...]
    __slots__ = ()
    @setdoc.basic
    def __init__(self:Self, data:Iterable, /)->None:
        self._data = tuple[Item, ...](data)
