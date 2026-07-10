"""Provide BaseDataContainer."""

__all__ = ["BaseDataContainer"]

from abc import abstractmethod
from collections.abc import Container, Hashable
from typing import Protocol, Self, TypeVar

import setdoc

from .BaseDataObject import BaseDataObject

DataItem = TypeVar("DataItem", covariant=True)
Item = TypeVar("Item", covariant=True)


class BaseDataContainer(BaseDataObject, Container[Hashable]):
    __slots__ = ()

    class Data(
        BaseDataObject.Data,
        Container[Hashable],
        Protocol,
    ):
        """Provide container data protocol."""

    @setdoc.basic
    def __contains__(self: Self, other: Hashable, /) -> bool:
        return other in self.data

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data: ...
