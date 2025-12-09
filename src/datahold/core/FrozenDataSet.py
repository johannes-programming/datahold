from .BaseDataSet import BaseDataSet
from .FrozenDataObject import FrozenDataObject
from typing import *

__all__ = ["FrozenDataSet"]

Item = TypeVar("Item")

class FrozenDataSet(FrozenDataObject, BaseDataSet[Item]):
    __slots__ = ()
    data:frozenset[Item]
    




