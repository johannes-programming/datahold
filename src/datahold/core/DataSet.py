"""Provide DataSet."""

from __future__ import annotations

__all__: list[str] = ["DataSet"]

from abc import abstractmethod
from collections import abc
from typing import Self

import setdoc

from ..base.BaseDataSet import BaseDataSet


class DataSet[Item: abc.Hashable](
    BaseDataSet[Item],
    abc.MutableSet[Item],
):
    """Provide easy abc for custom mutable set-like."""

    __slots__ = ()

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> DataSet.Data[Item]: ...

    @abstractmethod
    @setdoc.basic
    def __fset__(
        self: Self,
        value: DataSet.Init[Item],
        /,
    ) -> None: ...

    @setdoc.basic
    def __init__(self: Self, data: abc.Iterable[Item] = (), /) -> None:
        self.__fset__(frozenset(data))

    @setdoc.basic
    def add(self: Self, item: Item, /) -> None:
        self.__fset__(self.__fget__() | {item})

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self)

    @setdoc.basic
    def difference_update(
        self: Self,
        /,
        *others: abc.Iterable[abc.Hashable],
    ) -> None:
        data: set[Item]
        data = set(self.__fget__())
        data.difference_update(*others)
        self.__fset__(frozenset(data))

    @setdoc.basic
    def discard(self: Self, item: abc.Hashable, /) -> None:
        data: set[Item]
        data = set(self.__fget__())
        data.discard(item)
        self.__fset__(frozenset(data))

    @setdoc.basic
    def intersection_update(
        self: Self, /, *others: abc.Iterable[abc.Hashable]
    ) -> None:
        data: set[Item]
        data = set(self.__fget__())
        data.intersection_update(*others)
        self.__fset__(frozenset(data))

    @setdoc.basic
    def symmetric_difference_update(
        self: Self, other: abc.Iterable[Item], /
    ) -> None:
        data: set[Item]
        data = set(self.__fget__())
        data.symmetric_difference_update(other)
        self.__fset__(frozenset(data))

    @setdoc.basic
    def update(self: Self, /, *others: abc.Iterable[Item]) -> None:
        self.__fset__(self.__fget__().union(*others))
