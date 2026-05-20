import collections
from abc import abstractmethod
from typing import *

import setdoc

from .BaseDataObject import BaseDataObject

__all__ = ["BaseDataSet"]

Item = TypeVar("Item", covariant=True)
Item_ = TypeVar("Item_")


class BaseDataSet(
    BaseDataObject,
    collections.abc.Set[Item],
):
    data: frozenset[Item]
    __slots__ = ()

    @staticmethod
    def Repr() -> type:
        return set

    @setdoc.setdoc(set.__and__.__doc__)
    def __and__(self: Self, value: Any, /) -> Any:
        return self.data.__and__(value)

    @abstractmethod
    @setdoc.setdoc(set.__init__.__doc__)
    def __init__(self: Self, data: Iterable[Item] = (), /) -> None: ...

    @setdoc.setdoc(set.__or__.__doc__)
    def __or__(self: Self, value: Any, /) -> set[Item]:
        return self.data.__or__(value)

    @setdoc.setdoc(set.__rand__.__doc__)
    def __rand__(self: Self, value: Any, /) -> Any:
        return self.data.__rand__(value)

    @setdoc.setdoc(set.__ror__.__doc__)
    def __ror__(self: Self, value: Any, /) -> Any:
        return self.data.__ror__(value)

    @setdoc.setdoc(set.__rsub__.__doc__)
    def __rsub__(self: Self, value: Any, /) -> Any:
        return self.data.__rsub__(value)

    @setdoc.setdoc(set.__rxor__.__doc__)
    def __rxor__(self: Self, value: Iterable, /) -> Any:
        return self.data.__rxor__(value)

    @setdoc.setdoc(set.__sub__.__doc__)
    def __sub__(self: Self, value: Iterable, /) -> frozenset[Item]:
        return self.data.__sub__(value)

    @setdoc.setdoc(set.__xor__.__doc__)
    def __xor__(self: Self, value: Iterable[Item_], /) -> frozenset[Item|Item_]:
        return self.data.__xor__(value)

    @setdoc.setdoc(set.difference.__doc__)
    def difference(self: Self, /, *others: Iterable) -> frozenset[Item]:
        return self.data.difference(*others)

    @setdoc.setdoc(set.intersection.__doc__)
    def intersection(self: Self, /, *others: Iterable) -> frozenset[Item]:
        return self.data.intersection(*others)

    @setdoc.setdoc(set.isdisjoint.__doc__)
    def isdisjoint(self: Self, other: Iterable, /) -> bool:
        return self.data.isdisjoint(other)

    @setdoc.setdoc(set.issubset.__doc__)
    def issubset(self: Self, other: Iterable, /) -> bool:
        return self.data.issubset(other)

    @setdoc.setdoc(set.issuperset.__doc__)
    def issuperset(self: Self, other: Iterable, /) -> bool:
        return self.data.issuperset(other)

    @setdoc.setdoc(set.symmetric_difference.__doc__)
    def symmetric_difference(
            self: Self, 
            other: Iterable[Item_], 
            /,
    ) -> frozenset[Item|Item_]:
        return self.data.symmetric_difference(other)

    @setdoc.setdoc(set.union.__doc__)
    def union(
            self: Self, 
            /, 
            *others: Iterable[Item_],
    ) -> frozenset[Item | Item_]:
        return self.data.union(*others)
