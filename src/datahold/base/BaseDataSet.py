from __future__ import annotations

from abc import abstractmethod
from collections.abc import Hashable, Iterable, Set
from typing import Generic, Self, TypeVar

import setdoc

from .BaseDataCollection import BaseDataCollection

__all__ = ["BaseDataSet"]

Item = TypeVar("Item", bound=Hashable, covariant=True)


class BaseDataSet(BaseDataCollection[Item], Generic[Item]):
    __slots__ = ()

    @setdoc.basic
    def __and__(
        self: Self,
        other: BaseDataSet[Hashable],
        /,
    ) -> Self:
        return type(self)(self.data & other.data)

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Iterable[Item] = (), /) -> None: ...

    @setdoc.basic
    def __or__(
        self: Self,
        other: BaseDataSet[Item],
        /,
    ) -> Self:
        return type(self)(self.data | other.data)

    @setdoc.setdoc(set.__repr__.__doc__)
    def __repr__(self: Self, /) -> str:
        return f"{type(self).__name__}({set(self.data)})"

    @setdoc.basic
    def __sub__(
        self: Self,
        other: BaseDataSet[Hashable],
        /,
    ) -> Self:
        return type(self)(self.data - other.data)

    @setdoc.basic
    def __xor__(
        self: Self,
        other: BaseDataSet[Item],
        /,
    ) -> Self:
        return type(self)(self.data ^ other.data)

    @property
    @abstractmethod
    def data(self: Self) -> frozenset[Item]: ...

    @setdoc.setdoc(set.difference.__doc__)
    def difference(self: Self, /, *others: Iterable[Hashable]) -> Self:
        return type(self)(self.data.difference(*others))

    @setdoc.setdoc(set.intersection.__doc__)
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

    @setdoc.setdoc(set.symmetric_difference.__doc__)
    def symmetric_difference(
        self: Self,
        other: Iterable[Item],
        /,
    ) -> Self:
        return type(self)(self.data.symmetric_difference(other))

    @setdoc.setdoc(set.union.__doc__)
    def union(self: Self, /, *others: Iterable[Item]) -> Self:
        return type(self)(self.data.union(*others))


Set.register(BaseDataSet)  # type: ignore[type-abstract]
