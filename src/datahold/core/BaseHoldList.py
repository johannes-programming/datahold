from typing import *
from .BaseHoldObject import BaseHoldObject
from .BaseDataList import BaseDataList

__all__ = ["BaseHoldList"]

Item = TypeVar("Item")

class BaseHoldList(BaseDataList[Item], BaseHoldObject):
    data:tuple[Item, ...]
    __slots__ = ()

