"""Provide BaseDataCollection."""

__all__ = ["BaseDataCollection"]

from abc import abstractmethod
from collections.abc import Container, Iterable, Iterator, Sized
from typing import Protocol, Self, TypeVar

import setdoc

from .BaseDataObject import BaseDataObject

DataItem = TypeVar("DataItem", covariant=True)
Item = TypeVar("Item", covariant=True)


class BaseDataCollection(
    BaseDataObject,
    Sized,
    Iterable[Item],
    Container[object],
):
    __slots__ = ()

    class Data(
        Sized,
        Iterable[DataItem],
        Container[object],
        BaseDataObject.Data,
        Protocol[DataItem],
    ):
        """Provide collection data protocol."""

    @setdoc.basic
    def __contains__(self: Self, other: object, /) -> bool:
        try:
            return other in self.data
        except TypeError:
            pass
        for x in self:
            if x is other and x == other:
                return True
        return False

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
