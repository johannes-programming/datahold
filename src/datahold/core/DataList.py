"""Provide DataList."""

from __future__ import annotations

__all__: list[str] = ["DataList"]

from abc import abstractmethod
from collections.abc import Iterable, MutableSequence
from typing import Any, Self, SupportsIndex, overload

import setdoc

from ..base.BaseDataList import BaseDataList, Slice
from .DataCollection import DataCollection


class DataList[Item](
    BaseDataList[Item],
    DataCollection[Item],
    MutableSequence[Item],
):
    __slots__ = ()

    @setdoc.basic
    def __delitem__(self: Self, other: SupportsIndex | Slice[SupportsIndex], /) -> None:
        data: list[Item]
        data = list(self.data)
        del data[other]
        self.data = tuple(data)

    @setdoc.basic
    def __imul__(self: Self, other: SupportsIndex, /) -> Self:
        self.data *= other
        return self

    @setdoc.basic
    def __init__(
        self: Self,
        data: Iterable[Item] = (),
        /,
    ) -> None:
        self.data = tuple(data)

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
        value: Iterable[Item],
        /,
    ) -> None: ...

    @setdoc.basic
    def __setitem__(
        self: Self,
        key: SupportsIndex | Slice[SupportsIndex],
        value: Item | Iterable[Item],
        /,
    ) -> None:
        data: Any
        data = list(self.data)
        data[key] = value
        self.data = tuple(data)

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self)
    
    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> DataList.Data[Item]: ...

    @data.setter
    @abstractmethod
    @setdoc.basic
    def data(
        self: Self,
        value: Iterable[Item],
    ) -> None: ...

    @setdoc.basic
    def insert(self: Self, index: SupportsIndex, item: Item, /) -> None:
        data: list[Item]
        data = list(self.data)
        data.insert(index, item)
        self.data = tuple(data)

    @setdoc.basic
    def sort(self: Self, *, key: Any = None, reverse: bool = False) -> None:
        data: list[Item]
        data = list(self.data)
        data.sort(key=key, reverse=reverse)
        self.data = tuple(data)
