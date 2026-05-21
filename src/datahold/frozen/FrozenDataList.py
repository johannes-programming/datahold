from abc import abstractmethod
from typing import *

from ..base.BaseDataList import BaseDataList
from .FrozenDataObject import FrozenDataObject

__all__ = ["FrozenDataList"]

Item = TypeVar("Item", covariant=True)


class FrozenDataList(FrozenDataObject, BaseDataList[Item]):

    __slots__ = ()

    @property
    @abstractmethod
    def data(self: Self) -> tuple[Item, ...]: ...
