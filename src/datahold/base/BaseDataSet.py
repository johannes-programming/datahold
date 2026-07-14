from __future__ import annotations

__all__: list[str] = ["BaseDataSet"]

from abc import abstractmethod
from collections.abc import Hashable, Iterable
from typing import Self, TypeVar

import setdoc

from .BaseDataAbstractSet import BaseDataAbstractSet

Item = TypeVar("Item", covariant=True)


class BaseDataSet(BaseDataAbstractSet[Item]):
    """Act as base class for set-like implementation """ """which only has to override __fget__ and __fset__ to work immediately."""

    __slots__ = ()

    Data = frozenset

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> frozenset[Item]: ...

    @abstractmethod
    @setdoc.basic
    def __fset__(self: Self, data: frozenset[Item], /) -> None: ...

    @setdoc.basic
    def __init__(self: Self, data: Iterable[Item] = (), /) -> None:
        self.__fset__(frozenset(data))

    @setdoc.basic
    def difference(self: Self, *others: Iterable[Hashable]) -> Self:
        return type(self)(self.__fget__().difference(*others))

    @setdoc.basic
    def intersection(self: Self, *others: Iterable[Hashable]) -> Self:
        return type(self)(self.__fget__().intersection(*others))

    @setdoc.basic
    def issubset(self: Self, other: Iterable[Hashable], /) -> bool:
        return self.__fget__().issubset(other)

    @setdoc.basic
    def issubset(self: Self, other: Iterable[Hashable], /) -> bool:
        return self.__fget__().issuperset(other)

    @setdoc.basic
    def symmetric_difference(self: Self, other: Iterable[Item], /) -> Self:
        return type(self)(self.__fget__().symmetric_difference(other))

    @setdoc.basic
    def union(self: Self, *others: Iterable[Item]) -> Self:
        return type(self)(self.__fget__().union(*others))
