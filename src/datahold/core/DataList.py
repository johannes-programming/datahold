from abc import abstractmethod
from collections.abc import Iterable, MutableSequence
from typing import Any, Self, SupportsIndex, TypeVar, overload

import setdoc

from ..base.BaseDataList import BaseDataList
from .DataObject import DataObject

__all__ = ["DataList"]

Item = TypeVar("Item")


class DataList(
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

    @setdoc.setdoc(list.append.__doc__)
    def append(self: Self, item: Item, /) -> None:
        self.data += (item,)

    @setdoc.setdoc(list.clear.__doc__)
    def clear(self: Self, /) -> None:
        self.data = ()

    @property
    @abstractmethod
    def data(self: Self) -> tuple[Item, ...]: ...

    @data.setter
    @abstractmethod
    def data(
        self: Self,
        value: Iterable[Item],
    ) -> None: ...

    @setdoc.setdoc(list.extend.__doc__)
    def extend(self: Self, iterable: Iterable[Item], /) -> None:
        self.data += tuple(iterable)

    @setdoc.setdoc(list.insert.__doc__)
    def insert(self: Self, index: SupportsIndex, item: Item, /) -> None:
        data: list[Item]
        data = list(self.data)
        data.insert(index, item)
        self.data = tuple(data)

    @setdoc.setdoc(list.pop.__doc__)
    def pop(self: Self, index: SupportsIndex = -1, /) -> Item:
        ans: Item
        data: list[Item]
        data = list(self.data)
        ans = data.pop(index)
        self.data = tuple(data)
        return ans

    @setdoc.setdoc(list.remove.__doc__)
    def remove(self: Self, item: object, /) -> None:
        data: list[Item]
        data = list(self.data)
        data.remove(item)  # type: ignore[arg-type]
        self.data = tuple(data)

    @setdoc.setdoc(list.reverse.__doc__)
    def reverse(self: Self) -> None:
        self.data = tuple(self.data[::-1])

    @setdoc.setdoc(list.sort.__doc__)
    def sort(self: Self, *, key: Any = None, reverse: bool = False) -> None:
        data: list[Item]
        data = list(self.data)
        data.sort(key=key, reverse=reverse)
        self.data = tuple(data)
