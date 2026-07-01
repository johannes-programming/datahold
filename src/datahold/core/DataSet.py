"""Provide DataSet."""

__all__: list[str] = ["DataSet"]

from abc import abstractmethod
from collections.abc import Hashable, Iterable, MutableSet, Set
from typing import Self, TypeVar

import setdoc

from ..base.BaseDataSet import BaseDataSet
from .DataObject import DataObject

Item = TypeVar("Item", bound=Hashable)


class DataSet(DataObject, BaseDataSet[Item], MutableSet[Item]):
    __slots__ = ()

    @setdoc.basic
    def __iand__(self: Self, other: Set[Hashable], /) -> Self:
        self.data &= frozenset(other)
        return self

    @setdoc.basic
    def __init__(self: Self, data: Iterable[Item] = (), /) -> None:
        self.data = frozenset(data)

    @setdoc.basic
    def __ior__(self: Self, other: Set[Item], /) -> Self:  # type: ignore[override]
        self.data |= frozenset(other)
        return self

    @setdoc.basic
    def __isub__(self: Self, other: Set[Hashable], /) -> Self:
        self.data -= frozenset(other)
        return self

    @setdoc.basic
    def __ixor__(self: Self, other: Set[Item], /) -> Self:  # type: ignore[override]
        self.data ^= frozenset(other)
        return self

    @setdoc.basic
    def add(self: Self, item: Item, /) -> None:
        self.data |= {item}

    @setdoc.basic
    def clear(self: Self) -> None:
        self.data = frozenset()

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> frozenset[Item]: ...

    @data.setter
    @abstractmethod
    @setdoc.basic
    def data(
        self: Self,
        value: Iterable[Item],
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
    def pop(self: Self, /) -> Item:
        ans: Item
        data: set[Item]
        data = set(self.data)
        ans = data.pop()
        self.data = frozenset(data)
        return ans

    @setdoc.basic
    def remove(self: Self, item: Hashable, /) -> None:
        data: set[Item]
        data = set(self.data)
        data.remove(item)  # type: ignore[arg-type]
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
