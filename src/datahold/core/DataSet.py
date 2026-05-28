from collections.abc import MutableSet
from typing import Any, Self, TypeVar

import setdoc

from ..base.BaseDataSet import BaseDataSet
from .DataObject import DataObject

__all__ = ["DataSet"]

Item = TypeVar("Item")


class DataSet(DataObject, BaseDataSet[Item]):
    __slots__ = ()

    @setdoc.setdoc(set.__iand__.__doc__)
    def __iand__(self: Self, value: Any, /) -> Any:
        ans: set[Item]
        data: set[Item]
        data = set(self.data)
        ans = data.__iand__(value)
        self.data = frozenset(data)
        return ans

    @setdoc.basic
    def __init__(self: Self, data: Any = (), /) -> None:
        self.data = frozenset(data)

    @setdoc.setdoc(set.__ior__.__doc__)
    def __ior__(
        self: Self,
        value: Any,
        /,
    ) -> Any:
        ans: Any
        data: Any
        data = set(self.data)
        ans = data.__ior__(value)
        self.data = frozenset(data)
        return ans

    @setdoc.setdoc(set.__isub__.__doc__)
    def __isub__(
        self: Self,
        value: Any,
        /,
    ) -> Any:
        ans: set[Item]
        data: set[Item]
        data = set(self.data)
        ans = data.__isub__(value)
        self.data = frozenset(data)
        return ans

    @setdoc.setdoc(set.__ixor__.__doc__)
    def __ixor__(self: Self, value: Any, /) -> Any:
        ans: Any
        data: Any
        data = set(self.data)
        ans = data.__ixor__(value)
        self.data = frozenset(data)
        return ans

    @setdoc.setdoc(set.add.__doc__)
    def add(self: Self, item: Any, /) -> None:
        data: set[Item]
        data = set(self.data)
        data.add(item)
        self.data = frozenset(data)

    @setdoc.setdoc(set.clear.__doc__)
    def clear(self: Self) -> None:
        data: set[Item]
        data = set(self.data)
        data.clear()
        self.data = frozenset(data)

    @setdoc.setdoc(set.difference_update.__doc__)
    def difference_update(self: Self, /, *others: Any) -> None:
        data: set[Item]
        data = set(self.data)
        data.difference_update(*others)
        self.data = frozenset(data)

    @setdoc.setdoc(set.discard.__doc__)
    def discard(self: Self, item: Any, /) -> None:
        data: set[Item]
        data = set(self.data)
        data.discard(item)
        self.data = frozenset(data)

    @setdoc.setdoc(set.intersection_update.__doc__)
    def intersection_update(self: Self, /, *others: Any) -> None:
        data: set[Item]
        data = set(self.data)
        data.intersection_update(*others)
        self.data = frozenset(data)

    @setdoc.setdoc(set.pop.__doc__)
    def pop(self: Self, /) -> Item:
        ans: Item
        data: set[Item]
        data = set(self.data)
        ans = data.pop()
        self.data = frozenset(data)
        return ans

    @setdoc.setdoc(set.remove.__doc__)
    def remove(self: Self, item: Any, /) -> None:
        data: set[Item]
        data = set(self.data)
        data.remove(item)
        self.data = frozenset(data)

    @setdoc.setdoc(set.symmetric_difference_update.__doc__)
    def symmetric_difference_update(self: Self, other: Any, /) -> None:
        data: set[Item]
        data = set(self.data)
        data.symmetric_difference_update(other)
        self.data = frozenset(data)

    @setdoc.setdoc(set.update.__doc__)
    def update(self: Self, /, *others: Any) -> None:
        data: set[Item]
        data = set(self.data)
        data.update(*others)
        self.data = frozenset(data)


MutableSet.register(DataSet)
