from __future__ import annotations

__all__: list[str] = ["BaseDataSet"]

from abc import abstractmethod
from collections.abc import Hashable, Iterable
from typing import Protocol, Self

import setdoc

from .BaseDataAbstractSet import BaseDataAbstractSet


class BaseDataSet[Item](BaseDataAbstractSet[Item]):
    """Act as base class for set-like implementation which only needs overriding of __data__ and of __init__ to work immediately."""

    __slots__ = ()

    @setdoc.basic
    class Data[DataItem](
        BaseDataAbstractSet.Data[DataItem],
        Protocol[DataItem],
    ):
        @setdoc.basic
        def difference(
            self: Self, *others: Iterable[Hashable]
        ) -> Iterable[DataItem]: ...
        @setdoc.basic
        def intersection(
            self: Self, *others: Iterable[Hashable]
        ) -> Iterable[DataItem]: ...
        @setdoc.basic
        def issubset(self: Self, other: Iterable[Hashable], /) -> bool: ...
        @setdoc.basic
        def issuperset(self: Self, other: Iterable[Hashable], /) -> bool: ...
        @setdoc.basic
        def symmetric_difference(
            self: Self, other: Iterable[DataItem], /
        ) -> Iterable[DataItem]: ...
        @setdoc.basic
        def union(
            self: Self, *others: Iterable[DataItem]
        ) -> Iterable[DataItem]: ...

    type Init[InitItem] = Iterable[InitItem]

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> Data[Item]: ...

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Iterable[Item] = (), /) -> None: ...

    @setdoc.basic
    def difference(self: Self, *others: Iterable[Hashable]) -> Self:
        return type(self)(self.__data__().difference(*others))

    @setdoc.basic
    def intersection(self: Self, *others: Iterable[Hashable]) -> Self:
        return type(self)(self.__data__().intersection(*others))

    @setdoc.basic
    def issubset(self: Self, other: Iterable[Hashable], /) -> bool:
        return self.__data__().issubset(other)

    @setdoc.basic
    def issuperset(self: Self, other: Iterable[Hashable], /) -> bool:
        return self.__data__().issuperset(other)

    @setdoc.basic
    def symmetric_difference(self: Self, other: Iterable[Item], /) -> Self:
        return type(self)(self.__data__().symmetric_difference(other))

    @setdoc.basic
    def union(self: Self, *others: Iterable[Item]) -> Self:
        return type(self)(self.__data__().union(*others))
