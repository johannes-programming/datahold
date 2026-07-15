from __future__ import annotations

__all__: list[str] = ["DataAbstractSet"]

from abc import abstractmethod
from collections.abc import MutableSet
from typing import Protocol, Self, TypeVar

import setdoc

from ..base.BaseDataAbstractSet import BaseDataAbstractSet



class DataAbstractSet[Item](  # type: ignore[type-var]
    BaseDataAbstractSet[Item],
    MutableSet[Item],
):
    """Act as base class for (abstract) mutable set implementation which only has to override __fget__ and __fset__ to work immediately."""

    __slots__ = ()

    class Data[DataItem](BaseDataAbstractSet.Data[DataItem], Protocol[DataItem]):
        @setdoc.basic
        def add(self: Self, item: DataItem, /) -> None: ...
        @setdoc.basic
        def discard(self: Self, item: DataItem, /) -> None: ...

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> Data[Item]: ...

    @setdoc.basic
    def add(self: Self, item: Item, /) -> None:
        self.__data__().add(item)

    @setdoc.basic
    def discard(self: Self, item: Item, /) -> None:
        self.__data__().discard((item,))
