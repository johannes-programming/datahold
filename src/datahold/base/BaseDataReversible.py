"""Provide BaseDataCollection."""

__all__ = ["BaseDataCollection"]

from abc import abstractmethod
from collections.abc import Iterator, Reversible
from typing import Protocol, Self, TypeVar, runtime_checkable

import setdoc

from .BaseDataIterable import BaseDataIterable

Item = TypeVar("Item", covariant=True)
DataItem = TypeVar("DataItem", covariant=True)


class BaseDataReversible(
    BaseDataIterable[Item],
    Reversible[Item],
):
    __slots__ = ()

    @runtime_checkable
    class Data(
        BaseDataIterable.Data[DataItem],
        Reversible[DataItem],
        Protocol[DataItem],
    ): ...

    @setdoc.basic
    def __reversed__(self: Self, /) -> Iterator[Item]:
        return reversed(self.data)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data[Item]: ...
