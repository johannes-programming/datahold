"""Provide BaseDataSet."""

from __future__ import annotations

__all__: list[str] = ["BaseDataSet"]

from abc import abstractmethod
from collections.abc import Hashable, Iterable
from typing import Self, cast

import setdoc

from .BaseDataAbstractSet import BaseDataAbstractSet


class BaseDataSet[Item](BaseDataAbstractSet[Item]):
    __slots__ = ()

    Data = frozenset

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Iterable[Item] = (), /) -> None: ...

    @setdoc.basic
    def __repr__(self: Self, /) -> str:
        return f"{type(self).__name__}({set(self.data)!r})"

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> frozenset[Item]: ...

    @setdoc.basic
    def difference(self: Self, /, *others: Iterable[Hashable]) -> Self:
        return type(self)(self.data.difference(*others))

    @setdoc.basic
    def intersection(self: Self, /, *others: Iterable[Hashable]) -> Self:
        return type(self)(self.data.intersection(*others))

    @setdoc.basic
    def issubset(self: Self, other: Iterable[Hashable], /) -> bool:
        return self.data.issubset(other)

    @setdoc.basic
    def issuperset(self: Self, other: Iterable[Hashable], /) -> bool:
        return self.data.issuperset(other)

    @setdoc.basic
    def symmetric_difference(
        self: Self,
        other: Iterable[Item],
        /,
    ) -> Self:
        return type(self)(self.data.symmetric_difference(other))

    @setdoc.basic
    def union(self: Self, /, *others: Iterable[Item]) -> Self:
        return type(self)(self.data.union(*others))
