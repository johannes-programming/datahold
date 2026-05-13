from abc import abstractmethod
from typing import *

from .BaseDataSet import BaseDataSet
from .FrozenDataObject import FrozenDataObject

__all__ = ["FrozenDataSet"]

Item = TypeVar("Item", covariant=True)


class FrozenDataSet(FrozenDataObject, BaseDataSet[Item]):

    __slots__ = ()

    @property
    @abstractmethod
    def data(self: Self) -> frozenset[Item]: ...
