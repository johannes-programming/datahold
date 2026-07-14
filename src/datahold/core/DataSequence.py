# Concrete subclasses must provide __new__ or __init__,
# __getitem__, __setitem__, __delitem__, __len__, and insert().


from __future__ import annotations

__all__: list[str] = ["DataSequence"]

from collections.abc import MutableSequence
from typing import Self, SupportsIndex, TypeVar

import setdoc

from ..base.BaseDataSequence import BaseDataSequence

Item = TypeVar("Item")


class DataSequence(  # type: ignore[type-var]
    BaseDataSequence[Item],
    MutableSequence[Item],
):
    """Act as base class for mutable sequence implementation which only has to override __fget__ and __fset__ to work immediately."""

    __slots__ = ()

    @setdoc.basic
    def __delitem__(self: Self, index: SupportsIndex, /) -> None:
        data: list[Item]
        data = list(self.__fget__())
        del data[index]
        self.__fset__(data)

    @setdoc.basic
    def __setitem__(self: Self, index: SupportsIndex, item: Item, /) -> None:
        data: list[Item]
        data = list(self.__fget__())
        data[index] = item
        self.__fset__(data)

    @setdoc.basic
    def insert(self: Self, index: SupportsIndex, item: Item, /) -> None:
        data: list[Item]
        data = list(self.__fget__())
        data.insert(index, item)
        self.__fset__(data)
