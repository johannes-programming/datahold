from typing import *

from .BaseDataSet import BaseDataSet
from .FrozenDataObject import FrozenDataObject

__all__ = ["FrozenDataSet"]

Item = TypeVar("Item")


class FrozenDataSet(FrozenDataObject, BaseDataSet[Item]):
    __slots__ = ()
    data: frozenset[Item]
