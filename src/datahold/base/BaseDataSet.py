"""Provide BaseDataSet."""

from __future__ import annotations

__all__: list[str] = ["BaseDataSet"]

from abc import abstractmethod
from collections.abc import Hashable, Iterable, Set
from typing import Protocol, Self, TypeVar

import setdoc

from .BaseDataAbstractSet import BaseDataAbstractSet

Item = TypeVar("Item", bound=Hashable, covariant=True)


class Data(Set[Item], Protocol[Item]):
    """Provide hashable abstract set protocol."""

    @setdoc.basic
    def __hash__(self: Self) -> int: ...


class BaseDataSet(BaseDataAbstractSet[Item]):
    __slots__ = ()

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
