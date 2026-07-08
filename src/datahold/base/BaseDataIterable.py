"""Provide BaseDataIterable."""

__all__ = ["BaseDataIterable"]

from abc import abstractmethod
from collections.abc import Iterable, Iterator
from typing import Protocol, Self, TypeVar, runtime_checkable

import setdoc

from .BaseDataObject import BaseDataObject

Item = TypeVar("Item", covariant=True)
DataItem = TypeVar("DataItem", covariant=True)


class BaseDataIterable(BaseDataObject, Iterable[Item]):
    __slots__ = ()

    @runtime_checkable
    class Data(
        BaseDataObject.Data, Iterable[DataItem], Protocol[DataItem]
    ): ...

    @setdoc.basic
    def __iter__(self: Self, /) -> Iterator[Item]:
        return iter(self.data)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data[Item]: ...
