from typing import *

from .BaseDataList import BaseDataList
from .FrozenDataObject import FrozenDataObject

__all__ = ["FrozenDataList"]

Item = TypeVar("Item")


class FrozenDataList(FrozenDataObject, BaseDataList[Item]):
    __slots__ = ()
    data: tuple[Item, ...]
