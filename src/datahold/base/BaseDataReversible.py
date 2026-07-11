"""Provide BaseDataReversible."""

from __future__ import annotations

__all__: list[str] = ["BaseDataReversible"]

from abc import abstractmethod
from collections.abc import Iterator, Reversible
from typing import Protocol, Self, TypeVar

import setdoc

from .BaseDataIterable import BaseDataIterable

DataItem = TypeVar("DataItem", covariant=True)
Item = TypeVar("Item", covariant=True)


class BaseDataReversible(
    BaseDataIterable[Item],
    Reversible[Item],
):
    __slots__ = ()

    class Data(
        BaseDataIterable.Data[DataItem],
        Reversible[DataItem],
        Protocol[DataItem],
    ):
        """Provide reversible data protocol."""

    @setdoc.basic
    def __reversed__(self: Self, /) -> Iterator[Item]:
        return reversed(self.data)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data[Item]: ...
