from __future__ import annotations

__all__: list[str] = ["BaseDataSet"]

from typing import TypeVar, Self
from .BaseDataAbstractSet import BaseDataAbstractSet
from .BaseDataFgettable import BaseDataFgettable
from collections.abc import Iterable, Hashable
import setdoc

Item = TypeVar("Item", covariant=True)


class BaseDataSet(BaseDataAbstractSet[Item]):

    __slots__ = ()

    Data = frozenset

    __fget__ = BaseDataFgettable[frozenset[Item]].__fget__

    @setdoc.basic
    def difference(self:Self, *others:Iterable[Hashable]) -> Self:
        return type(self)(self.__fget__().difference(*others))
    @setdoc.basic
    def intersection(self:Self, *others:Iterable[Hashable]) -> Self:
        return type(self)(self.__fget__().intersection(*others))
    @setdoc.basic
    def issubset(self:Self, other:Iterable[Hashable], /) -> bool:
        return self.__fget__().issubset(other)
    @setdoc.basic
    def issubset(self:Self, other:Iterable[Hashable], /) -> bool:
        return self.__fget__().issuperset(other)
    @setdoc.basic
    def symmetric_difference(self:Self, other:Iterable[Item], /) -> Self:
        return type(self)(self.__fget__().symmetric_difference(other))
    @setdoc.basic
    def union(self:Self, *others:Iterable[Item]) -> Self:
        return type(self)(self.__fget__().union(*others))