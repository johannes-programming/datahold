from typing import *
from .BaseHoldObject import BaseHoldObject
from .BaseDataSet import BaseDataSet

__all__ = ["BaseHoldSet"]

Item = TypeVar("Item")

class BaseHoldSet(BaseDataSet[Item], BaseHoldObject):
    data:frozenset[Item]
    __slots__ = ()

