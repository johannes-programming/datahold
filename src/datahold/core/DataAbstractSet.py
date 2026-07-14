

from __future__ import annotations

__all__: list[str] = ["DataAbstractSet"]

from ..base.BaseDataAbstractSet import BaseDataAbstractSet
from collections.abc import MutableSet
from typing import Self, TypeVar

import setdoc

Item = TypeVar("Item")

class DataAbstractSet(  # type: ignore[type-var]
    BaseDataAbstractSet[Item],
    MutableSet[Item],
):
    __slots__ = ()

    @setdoc.basic
    def add(self:Self, item:Item, /) -> None:
        data:set[Item]
        data = set(self.__fget__())
        data.add(item)
        self.__fset__(data)
        


    @setdoc.basic
    def discard(self:Self, item:Item, /) -> None:
        data:set[Item]
        data = set(self.__fget__())
        data.discard(item)
        self.__fset__(data)


