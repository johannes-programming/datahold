from __future__ import annotations

__all__: list[str] = ["DataAbstractSet"]

from collections.abc import MutableSet
from typing import Self, TypeVar

import setdoc

from ..base.BaseDataAbstractSet import BaseDataAbstractSet

Item = TypeVar("Item")


class DataAbstractSet(  # type: ignore[type-var]
    BaseDataAbstractSet[Item],
    MutableSet[Item],
):
    """Act as base class for (abstract) mutable set implementation """ """which only has to override __fget__ and __fset__ to work immediately."""

    __slots__ = ()

    @setdoc.basic
    def add(self: Self, item: Item, /) -> None:
        self.__fset__(self.__fget__().union((item,)))

    @setdoc.basic
    def discard(self: Self, item: Item, /) -> None:
        self.__fset__(self.__fget__().difference((item,)))
