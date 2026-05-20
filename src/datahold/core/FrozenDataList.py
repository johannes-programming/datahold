from typing import *

from .BaseDataList import BaseDataList
from .FrozenDataObject import FrozenDataObject

__all__ = ["FrozenDataList"]

Item = TypeVar("Item", covariant=True)


class FrozenDataList(FrozenDataObject, BaseDataList[Item]):
    data: tuple[Item, ...]
    __slots__ = ()
