import collections
from typing import *

import setdoc

from ..base.BaseDataList import BaseDataList
from .DataObject import DataObject

__all__ = ["DataList"]

Item = TypeVar("Item")


class DataList(DataObject, BaseDataList[Item], collections.abc.MutableSequence[Item]):
    data: tuple[Item, ...]
    __slots__ = ()

    @setdoc.setdoc(list.__delitem__.__doc__)
    def __delitem__(self: Self, key: SupportsIndex | slice, /) -> None:
        data: list[Item]
        data = list(self.data)
        data.__delitem__(key)
        self.data = tuple(data)

    @setdoc.setdoc(list.__iadd__.__doc__)
    def __iadd__(self: Self, value: Iterable[Item], /) -> list[Item]:
        ans: list[Item]
        data: list[Item]
        data = list(self.data)
        ans = data.__iadd__(value)
        self.data = tuple(data)
        return ans

    @setdoc.setdoc(list.__imul__.__doc__)
    def __imul__(self: Self, value: SupportsIndex, /) -> list[Item]:
        ans: Any
        data: list[Item]
        data = list(self.data)
        ans = data.__imul__(value)
        self.data = tuple(data)
        return ans

    @setdoc.basic
    def __init__(self: Self, data: Iterable[Item] = (), /) -> None:
        self.data = tuple(data)

    @setdoc.setdoc(list.__setitem__.__doc__)
    def __setitem__(self: Self, key: SupportsIndex | slice, value: Item, /) -> None:
        data: Any
        data = list(self.data)
        data.__setitem__(key, value)
        self.data = tuple(data)

    @setdoc.setdoc(list.append.__doc__)
    def append(self: Self, value: Item, /) -> None:
        data: list[Item]
        data = list(self.data)
        data.append(value)
        self.data = tuple(data)

    @setdoc.setdoc(list.clear.__doc__)
    def clear(self: Self, /) -> None:
        data: list[Item]
        data = list(self.data)
        data.clear()
        self.data = tuple(data)

    @setdoc.setdoc(list.extend.__doc__)
    def extend(self: Self, iterable: Iterable[Item], /) -> None:
        data: list[Item]
        data = list(self.data)
        data.extend(iterable)
        self.data = tuple(data)

    @setdoc.setdoc(list.insert.__doc__)
    def insert(self: Self, index: SupportsIndex, object: Item, /) -> None:
        data: list[Item]
        data = list(self.data)
        data.insert(index, object)
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
    def remove(self: Self, value: Item) -> None:
        data: list[Item]
        data = list(self.data)
        data.remove(value)
        self.data = tuple(data)

    @setdoc.setdoc(list.reverse.__doc__)
    def reverse(self: Self) -> None:
        data: list[Item]
        data = list(self.data)
        data.reverse()
        self.data = tuple(data)

    @setdoc.setdoc(list.sort.__doc__)
    def sort(self: Self, key: Optional[Callable] = None, reverse: bool = False) -> None:
        data: list[Item]
        data = list(self.data)
        data.sort(key=key, reverse=reverse)
        self.data = tuple(data)
