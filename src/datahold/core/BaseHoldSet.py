from abc import abstractmethod
from typing import *

from .BaseDataSet import BaseDataSet
from .BaseHoldObject import BaseHoldObject

__all__ = ["BaseHoldSet"]

Item = TypeVar("Item")


class BaseHoldSet(BaseHoldObject, BaseDataSet[Item]):
    __slots__ = ()

    @property
    @abstractmethod
    def data(self: Self) -> frozenset[Item]: ...
