from __future__ import annotations

from abc import abstractmethod
from collections.abc import Hashable, Iterable, Set
from typing import Self, TypeVar, cast

import setdoc

from .BaseDataCollection import BaseDataCollection

__all__ = ["BaseDataSet"]

Item = TypeVar("Item", bound=Hashable, covariant=True)


class BaseDataSet(BaseDataCollection[Item], Set[Item]):
    __slots__ = ()

    @setdoc.basic
    def __and__(
        self: Self,
        other: Set[Hashable],
        /,
    ) -> Self:
        return type(self)(self.data & frozenset(other))

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Iterable[Item] = (), /) -> None: ...

    @setdoc.basic
    def __or__(self: Self, other: Set[Item], /) -> Self:  # type: ignore[override]
        return type(self)(self.data | frozenset(other))

    @setdoc.basic
    def __rand__(
        self: Self,
        other: Set[Hashable],
        /,
    ) -> Self:
        return type(self)(cast(frozenset[Item], frozenset(other) & self.data))

    @setdoc.basic
    def __repr__(self: Self, /) -> str:
        return "%s(%r)" % (type(self).__name__, set(self.data))

    @setdoc.basic
    def __ror__(
        self: Self,
        other: Set[Item],
        /,
    ) -> Self:
        return type(self)(frozenset(other) | self.data)

    @setdoc.basic
    def __rsub__(
        self: Self,
        other: Set[Hashable],
        /,
    ) -> Self:
        return type(self)(cast(frozenset[Item], frozenset(other) - self.data))

    @setdoc.basic
    def __rxor__(
        self: Self,
        other: Set[Item],
        /,
    ) -> Self:
        return type(self)(frozenset(other) ^ self.data)

    @setdoc.basic
    def __sub__(
        self: Self,
        other: Set[Hashable],
        /,
    ) -> Self:
        return type(self)(self.data - frozenset(other))

    @setdoc.basic
    def __xor__(self: Self, other: Set[Item], /) -> Self:  # type: ignore[override]
        return type(self)(self.data ^ frozenset(other))

    @property
    @abstractmethod
    def data(self: Self) -> frozenset[Item]: ...

    @setdoc.basic
    def difference(self: Self, /, *others: Iterable[Hashable]) -> Self:
        return type(self)(self.data.difference(*others))

    @setdoc.basic
    def intersection(self: Self, /, *others: Iterable[Hashable]) -> Self:
        return type(self)(self.data.intersection(*others))

    @setdoc.setdoc(set.isdisjoint.__doc__)
    def isdisjoint(self: Self, other: Iterable[Hashable], /) -> bool:
        return self.data.isdisjoint(other)

    @setdoc.setdoc(set.issubset.__doc__)
    def issubset(self: Self, other: Iterable[Hashable], /) -> bool:
        return self.data.issubset(other)

    @setdoc.setdoc(set.issuperset.__doc__)
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
