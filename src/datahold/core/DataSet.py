"""Provide DataSet."""

from __future__ import annotations

__all__: list[str] = ["DataSet"]

from abc import abstractmethod
from collections.abc import Hashable, Iterable, MutableSet
from typing import Self

import setdoc

from ..base.BaseDataSet import BaseDataSet
from .DataCollection import DataCollection


class DataSet[Item: Hashable](
    BaseDataSet[Item],
    DataCollection[Item],
    MutableSet[Item],
):
    """Provide easy abc for custom mutable set-like."""

    __slots__ = ()

    @setdoc.basic
    def __init__(self: Self, data: Iterable[Item] = (), /) -> None:
        self.data = frozenset(data)

    @setdoc.basic
    def add(self: Self, item: Item, /) -> None:
        self.data |= {item}

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> DataSet.Data[Item]: ...

    @data.setter
    @abstractmethod
    @setdoc.basic
    def data(
        self: Self,
        value: DataSet.Init[Item],
    ) -> None: ...

    @setdoc.basic
    def difference_update(
        self: Self,
        /,
        *others: Iterable[Hashable],
    ) -> None:
        data: set[Item]
        data = set(self.data)
        data.difference_update(*others)
        self.data = frozenset(data)

    @setdoc.basic
    def discard(self: Self, item: Hashable, /) -> None:
        data: set[Item]
        data = set(self.data)
        data.discard(item)
        self.data = frozenset(data)

    @setdoc.basic
    def intersection_update(
        self: Self, /, *others: Iterable[Hashable]
    ) -> None:
        data: set[Item]
        data = set(self.data)
        data.intersection_update(*others)
        self.data = frozenset(data)

    @setdoc.basic
    def symmetric_difference_update(
        self: Self, other: Iterable[Item], /
    ) -> None:
        data: set[Item]
        data = set(self.data)
        data.symmetric_difference_update(other)
        self.data = frozenset(data)

    @setdoc.basic
    def update(self: Self, /, *others: Iterable[Item]) -> None:
        self.data = self.data.union(*others)
