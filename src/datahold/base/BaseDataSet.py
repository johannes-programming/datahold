"""Provide BaseDataSet."""

from __future__ import annotations

__all__: list[str] = ["BaseDataSet"]

from abc import abstractmethod
from collections import abc
from typing import Self

import setdoc

from .BaseDataAbstractSet import BaseDataAbstractSet


class BaseDataSet[Item: abc.Hashable](BaseDataAbstractSet[Item]):
    """Provide an easy abc for custom set-like."""

    __slots__ = ()

    type Data[DataItem] = frozenset[DataItem]
    type Init[InitItem] = abc.Iterable[InitItem]

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Init[Item] = (), /) -> None: ...

    @setdoc.basic
    def __repr__(self: Self, /) -> str:
        return f"{type(self).__name__}({set(self.__fget__())!r})"

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> frozenset[Item]: ...

    @setdoc.basic
    def difference(self: Self, /, *others: abc.Iterable[abc.Hashable]) -> Self:
        return type(self)(self.__fget__().difference(*others))

    @setdoc.basic
    def intersection(
        self: Self, /, *others: abc.Iterable[abc.Hashable]
    ) -> Self:
        return type(self)(self.__fget__().intersection(*others))

    @setdoc.basic
    def issubset(self: Self, other: abc.Iterable[abc.Hashable], /) -> bool:
        return self.__fget__().issubset(other)

    @setdoc.basic
    def issuperset(self: Self, other: abc.Iterable[abc.Hashable], /) -> bool:
        return self.__fget__().issuperset(other)

    @setdoc.basic
    def symmetric_difference(
        self: Self,
        other: abc.Iterable[Item],
        /,
    ) -> Self:
        return type(self)(self.__fget__().symmetric_difference(other))

    @setdoc.basic
    def union(self: Self, /, *others: abc.Iterable[Item]) -> Self:
        return type(self)(self.__fget__().union(*others))
