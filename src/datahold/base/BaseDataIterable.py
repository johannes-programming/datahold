"""Provide BaseDataCollection."""

__all__: list[str] = ["BaseDataCollection"]

from abc import abstractmethod
from collections.abc import Iterable, Iterator
from typing import Protocol, Self, TypeVar

import setdoc

from .BaseDataObject import BaseDataObject

DataItem = TypeVar("DataItem", covariant=True)
Item = TypeVar("Item", covariant=True)


class BaseDataIterable(BaseDataObject, Iterable[Item]):
    __slots__ = ()

    class Data(
        BaseDataObject.Data,
        Iterable[DataItem],
        Protocol[DataItem],
    ):
        """Provide collection data protocol."""

    @setdoc.basic
    def __iter__(self: Self, /) -> Iterator[Item]:
        return iter(self.data)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data[Item]: ...
