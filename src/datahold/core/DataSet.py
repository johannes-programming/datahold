

from __future__ import annotations

__all__: list[str] = ["DataSet"]
from ..base.BaseDataSet import BaseDataSet
from .DataAbstractSet import DataAbstractSet
from .DataCopyable import DataCopyable
from typing import Self, TypeVar
from collections.abc import Iterable, Hashable

import setdoc

Item = TypeVar("Item")

class DataSet(  # type: ignore[type-var]
    BaseDataSet[Item],
    DataAbstractSet[Item],
    DataCopyable,
):
    __slots__ = ()
    
    @setdoc.basic
    def difference_update(self:Self, *others: Iterable[Hashable]) -> None:
        data: set[Item]
        data = set(self.__fget__())
        data.difference_update(*others)
        self.__fset__(data)

    @setdoc.basic
    def intersection_update(self:Self, *others:Iterable[Hashable]) -> None:
        data: set[Item]
        data = set(self.__fget__())
        data.intersection_update(*others)
        self.__fset__(data)
        
    @setdoc.basic
    def symmetric_difference_update(self:Self, other:Iterable[Item], /) -> None:
        data: set[Item]
        data = set(self.__fget__())
        data.symmetric_difference_update(*other)
        self.__fset__(data) 

    @setdoc.basic
    def update(self:Self, *others:Iterable[Item]) -> None:
        data: set[Item]
        data = set(self.__fget__())
        data.update(*others)
        self.__fset__(data)


