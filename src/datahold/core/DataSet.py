from __future__ import annotations

__all__: list[str] = ["DataSet"]
from collections.abc import Hashable, Iterable
from typing import Self

import setdoc

from ..base.BaseDataSet import BaseDataSet
from .DataAbstractSet import DataAbstractSet
from .DataCopyable import DataCopyable
from abc import abstractmethod


class DataSet[Item](  # type: ignore[type-var]
    BaseDataSet[Item],
    DataAbstractSet[Item],
    DataCopyable[Item],
):
    """Act as base class for (abstract) mutable set implementation which only has to override __data__ and __fset__ to work immediately."""

    __slots__ = ()

    class Data[DataItem](BaseDataSet[DataItem], DataAbstractSet[DataItem]):
        @setdoc.basic
        def difference_update(
            self: Self, *others: Iterable[Hashable]
        ) -> None: ...
        @setdoc.basic
        def intersection_update(
            self: Self, *others: Iterable[Hashable]
        ) -> None: ...
        @setdoc.basic
        def symmetric_difference_update(
            self: Self, other: Iterable[DataItem], /
        ) -> None: ...
        @setdoc.basic
        def update(self: Self, *others: Iterable[DataItem]) -> None: ...
    
    @abstractmethod
    @setdoc.basic
    def __data__(self:Self) -> Data[Item]:
        ...

    @setdoc.basic
    def difference_update(self: Self, *others: Iterable[Hashable]) -> None:
        self.__data__().difference_update(*others)

    @setdoc.basic
    def intersection_update(self: Self, *others: Iterable[Hashable]) -> None:
        self.__data__().intersection_update(*others)

    @setdoc.basic
    def symmetric_difference_update(
        self: Self, other: Iterable[Item], /
    ) -> None:
        self.__data__().symmetric_difference_update(other)

    @setdoc.basic
    def update(self: Self, *others: Iterable[Item]) -> None:
        self.__data__().update(*others)
