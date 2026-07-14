from __future__ import annotations

__all__: list[str] = ["DataSet"]
from collections.abc import Hashable, Iterable
from typing import Self, TypeVar

import setdoc

from ..base.BaseDataSet import BaseDataSet
from .DataAbstractSet import DataAbstractSet

Item = TypeVar("Item")


class DataSet(  # type: ignore[type-var]
    BaseDataSet[Item],
    DataAbstractSet[Item],
):
    """Act as base class for (abstract) mutable set implementation which only has to override __fget__ and __fset__ to work immediately."""

    __slots__ = ()

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self.__fget__())

    @setdoc.basic
    def difference_update(self: Self, *others: Iterable[Hashable]) -> None:
        data: set[Item]
        data = set(self.__fget__())
        data.difference_update(*others)
        self.__fset__(frozenset(data))

    @setdoc.basic
    def intersection_update(self: Self, *others: Iterable[Hashable]) -> None:
        data: set[Item]
        data = set(self.__fget__())
        data.intersection_update(*others)
        self.__fset__(frozenset(data))

    @setdoc.basic
    def symmetric_difference_update(
        self: Self, other: Iterable[Item], /
    ) -> None:
        data: set[Item]
        data = set(self.__fget__())
        data.symmetric_difference_update(*other)
        self.__fset__(frozenset(data))

    @setdoc.basic
    def update(self: Self, *others: Iterable[Item]) -> None:
        data: set[Item]
        data = set(self.__fget__())
        data.update(*others)
        self.__fset__(frozenset(data))
