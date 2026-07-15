# Concrete subclasses must provide __new__ or __init__,
# __getitem__, __setitem__, __delitem__, __len__, and insert().


from __future__ import annotations

__all__: list[str] = ["DataSequence"]

from abc import abstractmethod
from collections.abc import MutableSequence, Iterable
from typing import Optional, Self, SupportsIndex, overload

import setdoc

from ..base.BaseDataSequence import BaseDataSequence

Slice = slice[Optional[int], Optional[int], Optional[int]]


class DataSequence[Item](
    BaseDataSequence[Item],
    MutableSequence[Item],
):
    """Act as base class for mutable sequence implementation which only has to override __fget__ and __fset__ to work immediately."""

    __slots__ = ()

    @setdoc.basic
    class Data[DataItem](BaseDataSequence.Data[DataItem]):
        @overload
        @setdoc.basic
        def __delitem__(self: Self, key: SupportsIndex, /) -> None: 
            ...
        @overload
        @setdoc.basic
        def __delitem__(self: Self, key: Slice, /) -> None: 
            ...
        @setdoc.basic
        def __delitem__(self: Self, key: SupportsIndex | Slice, /) -> None:
            ...
        @overload
        @setdoc.basic
        def __setitem__(
            self: Self, key: SupportsIndex, value: Item, /
        ) -> None: 
            ...
        @overload
        @setdoc.basic
        def __setitem__(self: Self, key: Slice, value: Iterable[Item], /) -> None:
            ...
        @setdoc.basic
        def __setitem__(
            self: Self, key: SupportsIndex | Slice, value: Item | Iterable[Item], /
        ) -> None:
            ...

    @abstractmethod
    @setdoc.basic
    def __data__(self:Self) -> Data[Item]:
        ...

    @overload
    @setdoc.basic
    def __delitem__(self: Self, key: SupportsIndex, /) -> None: 
        ...
    @overload
    @setdoc.basic
    def __delitem__(self: Self, key: Slice, /) -> None: 
        # def __delitem__(self, slice[int | None, int | None, int | None], /) -> None
        ...
    @setdoc.basic
    def __delitem__(self: Self, key: SupportsIndex | Slice, /) -> None:
        del self.__data__()[key]

    @overload
    @setdoc.basic
    def __setitem__(
        self: Self, key: SupportsIndex, value: Item, /
    ) -> None: 
        # def [_T] (list[_T], typing.SupportsIndex, _T)
        ...

    @overload
    @setdoc.basic
    def __setitem__(self: Self, key: Slice, value: Iterable[Item], /) -> None:
        # def [_T] (list[_T], slice[typing.SupportsIndex | None, typing.SupportsIndex | None, typing.SupportsIndex | None], typing.Iterable[_T])
        ...

    @setdoc.basic
    def __setitem__(
        self: Self, key: SupportsIndex | Slice, value: Item | Iterable[Item], /
    ) -> None:
        self.__data__()[key] = value

    @setdoc.basic
    def insert(self: Self, index: SupportsIndex, item: Item, /) -> None:
        self.__data__().insert(index, item)
