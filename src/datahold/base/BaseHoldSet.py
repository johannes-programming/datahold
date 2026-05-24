import typing
from abc import abstractmethod

from .BaseDataSet import BaseDataSet
from .BaseHoldObject import BaseHoldObject

__all__ = ["BaseHoldSet"]

Item = typing.TypeVar("Item")


class BaseHoldSet(BaseHoldObject, BaseDataSet[Item]):
    __slots__ = ()

    @property
    @abstractmethod
    def data(self: typing.Self) -> frozenset[Item]: ...
