"""Provide DataList."""

from __future__ import annotations

__all__: list[str] = ["DataList"]

from abc import abstractmethod
from collections import abc
from typing import Any, Self, SupportsIndex, overload

import setdoc

from .._utils.Slice import Slice
from ..base.BaseDataList import BaseDataList


class DataList[Item](
    BaseDataList[Item],
    abc.MutableSequence[Item],
):
    """Provide easy abc for custom mutable list-like."""

    __slots__ = ()

    @setdoc.basic
    def __delitem__(
        self: Self, other: SupportsIndex | Slice[SupportsIndex], /
    ) -> None:
        data: list[Item]
        data = list(self.__fget__())
        del data[other]
        self.__fset__(tuple(data))

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> DataList.Data[Item]: ...

    @abstractmethod
    @setdoc.basic
    def __fset__(
        self: Self,
        value: DataList.Init[Item],
        /,
    ) -> None: ...

    @setdoc.basic
    def __imul__(self: Self, other: SupportsIndex, /) -> Self:
        self.__fset__(self.__fget__() * other)
        return self

    @setdoc.basic
    def __init__(
        self: Self,
        data: abc.Iterable[Item] = (),
        /,
    ) -> None:
        self.__fset__(tuple(data))

    @overload
    @setdoc.basic
    def __setitem__(
        self: Self, key: SupportsIndex, value: Item, /
    ) -> None: ...

    @overload
    @setdoc.basic
    def __setitem__(
        self: Self,
        key: Slice[SupportsIndex],
        value: abc.Iterable[Item],
        /,
    ) -> None: ...

    @setdoc.basic
    def __setitem__(
        self: Self,
        key: SupportsIndex | Slice[SupportsIndex],
        value: Item | abc.Iterable[Item],
        /,
    ) -> None:
        data: Any
        data = list(self.__fget__())
        data[key] = value
        self.__fset__(tuple(data))

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self)

    @setdoc.basic
    def insert(self: Self, index: SupportsIndex, item: Item, /) -> None:
        data: list[Item]
        data = list(self.__fget__())
        data.insert(index, item)
        self.__fset__(tuple(data))

    @setdoc.basic
    def sort(self: Self, *, key: Any = None, reverse: bool = False) -> None:
        data: list[Item]
        data = list(self.__fget__())
        data.sort(key=key, reverse=reverse)
        self.__fset__(tuple(data))
