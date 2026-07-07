"""Provide DataList."""

__all__: list[str] = ["DataList"]

from abc import abstractmethod
from collections.abc import Iterable, MutableSequence
from typing import Any, Self, SupportsIndex, TypeVar, overload

import setdoc

from ..base.BaseDataList import BaseDataList
from .DataObject import DataObject

Item = TypeVar("Item")


class DataList(  # type: ignore[misc]
    DataObject,
    BaseDataList[Item],
    MutableSequence[Item],
):
    __slots__ = ()

    @setdoc.basic
    def __delitem__(self: Self, other: SupportsIndex | slice, /) -> None:
        data: list[Item]
        data = list(self.data)
        del data[other]
        self.data = tuple(data)

    @setdoc.basic
    def __iadd__(self: Self, other: Iterable[Item], /) -> Self:
        self.data += tuple(other)
        return self

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
        key: slice,
        value: Iterable[Item],
        /,
    ) -> None: ...

    @setdoc.basic
    def __setitem__(
        self: Self,
        key: SupportsIndex | slice,
        value: Item | Iterable[Item],
        /,
    ) -> None:
        data: Any
        data = list(self.data)
        data[key] = value
        self.data = tuple(data)

    @setdoc.basic
    def append(self: Self, item: Item, /) -> None:
        self.data += (item,)

    @setdoc.basic
    def clear(self: Self, /) -> None:
        self.data = ()

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> tuple[Item, ...]: ...

    @data.setter
    @abstractmethod
    @setdoc.basic
    def data(
        self: Self,
        value: Iterable[Item],
    ) -> None: ...

    @setdoc.basic
    def extend(self: Self, iterable: Iterable[Item], /) -> None:
        self.data += tuple(iterable)

    @setdoc.basic
    def insert(self: Self, index: SupportsIndex, item: Item, /) -> None:
        data: list[Item]
        data = list(self.data)
        data.insert(index, item)
        self.data = tuple(data)

    @setdoc.basic
    def pop(self: Self, index: SupportsIndex = -1, /) -> Item:
        ans: Item
        data: list[Item]
        data = list(self.data)
        ans = data.pop(index)
        self.data = tuple(data)
        return ans

    @setdoc.basic
    def remove(self: Self, item: object, /) -> None:
        data: list[Item]
        data = list(self.data)
        data.remove(item)  # type: ignore[arg-type]
        self.data = tuple(data)

    @setdoc.basic
    def reverse(self: Self) -> None:
        self.data = tuple(self.data[::-1])

    @setdoc.basic
    def sort(self: Self, *, key: Any = None, reverse: bool = False) -> None:
        data: list[Item]
        data = list(self.data)
        data.sort(key=key, reverse=reverse)
        self.data = tuple(data)
