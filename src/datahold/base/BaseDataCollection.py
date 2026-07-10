"""Provide BaseDataCollection."""

__all__ = ["BaseDataCollection"]

from abc import abstractmethod
from collections.abc import Collection, Hashable, Iterator
from typing import Protocol, Self, TypeVar

import setdoc

from .BaseDataObject import BaseDataObject

DataItem = TypeVar("DataItem", covariant=True)
Item = TypeVar("Item", covariant=True)


class BaseDataCollection(BaseDataObject, Collection[Item]):
    __slots__ = ()

    class Data(Collection[DataItem], Protocol[DataItem]):
        @setdoc.basic
        def __hash__(self: Self) -> int: ...

    @setdoc.basic
    def __contains__(self: Self, other: Hashable, /) -> bool:
        return other in self.data

    @setdoc.basic
    def __iter__(self: Self, /) -> Iterator[Item]:
        return iter(self.data)

    @setdoc.basic
    def __len__(self: Self, /) -> int:
        return len(self.data)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data[Item]: ...
