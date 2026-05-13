from abc import abstractmethod
from typing import *

from .BaseDataList import BaseDataList
from .BaseHoldObject import BaseHoldObject

__all__ = ["BaseHoldList"]

Item = TypeVar("Item", covariant=True)


class BaseHoldList(BaseHoldObject, BaseDataList[Item]):
    __slots__ = ()

    @property
    @abstractmethod
    def data(self: Self) -> tuple[Item, ...]: ...
