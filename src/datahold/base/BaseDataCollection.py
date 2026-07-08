"""Provide BaseDataCollection."""

__all__ = ["BaseDataCollection"]

from abc import abstractmethod
from collections.abc import Collection, Hashable, Iterator
from typing import Protocol, Self, TypeVar, runtime_checkable

import setdoc

from .BaseDataObject import BaseDataObject

Item = TypeVar("Item", covariant=True)
DataItem = TypeVar("DataItem", covariant=True)


class BaseDataCollection(BaseDataObject, Collection[Item]):
    __slots__ = ()

    @runtime_checkable
    class Data(Collection[DataItem], BaseDataObject.Data, Protocol[DataItem]):
        @abstractmethod
        @setdoc.basic
        def __hash__(self: Self) -> int: ...
        @abstractmethod
        @setdoc.basic
        def __init__(self: Self, data: Self, /) -> None: ...

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
