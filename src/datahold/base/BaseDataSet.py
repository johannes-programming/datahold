from abc import abstractmethod
from collections.abc import Iterable
from collections.abc import Set as AbstractSet
from typing import Any, Self, TypeVar, overload

import setdoc

from .BaseDataObject import BaseDataObject

__all__ = ["BaseDataSet"]

Item = TypeVar("Item", covariant=True)
Item_ = TypeVar("Item_")


class BaseDataSet(BaseDataObject, AbstractSet[Item]):
    __slots__ = ()

    @setdoc.setdoc(set.__and__.__doc__)
    def __and__(
        self: Self,
        value: frozenset[object] | set[object],
        /,
    ) -> set[Item]:
        return set(self.data).__and__(value)

    @setdoc.setdoc(set.__contains__.__doc__)
    def __contains__(self: Self, value: object, /) -> bool:
        return set(self.data).__contains__(value)

    @abstractmethod
    @setdoc.setdoc(set.__init__.__doc__)
    def __init__(self: Self, data: Iterable[Item] = (), /) -> None: ...

    @setdoc.setdoc(set.__iter__.__doc__)
    def __iter__(self: Self, /) -> Iterable[Item]:
        return set(self.data).__iter__()

    @setdoc.setdoc(set.__len__.__doc__)
    def __len__(self: Self, /) -> int:
        return set(self.data).__len__()

    @setdoc.setdoc(set.__or__.__doc__)
    def __or__(
        self: Self,
        value: frozenset[Item_] | set[Item_],
        /,
    ) -> set[Item | Item_]:
        return set(self.data).__or__(value)

    @overload
    @setdoc.setdoc(set.__rand__.__doc__)
    def __rand__(
        self: Self,
        value: frozenset[object],
        /,
    ) -> frozenset[Item]: ...

    @overload
    @setdoc.setdoc(set.__rand__.__doc__)
    def __rand__(
        self: Self,
        value: set[object],
        /,
    ) -> set[Item]: ...
    @setdoc.setdoc(set.__rand__.__doc__)
    def __rand__(
        self: Self,
        value: frozenset[object] | set[object],
        /,
    ) -> frozenset[object] | set[object]:
        other: Any
        return set(self.data).__rand__(other)

    @setdoc.setdoc(set.__repr__.__doc__)
    def __repr__(self: Self, /) -> str:
        return set(self.data).__repr__()

    @overload
    @setdoc.setdoc(set.__ror__.__doc__)
    def __ror__(
        self: Self,
        value: frozenset[Item_],
        /,
    ) -> frozenset[Item | Item_]: ...
    @overload
    @setdoc.setdoc(set.__ror__.__doc__)
    def __ror__(
        self: Self,
        value: set[Item_],
        /,
    ) -> set[Item | Item_]: ...
    @setdoc.setdoc(set.__ror__.__doc__)
    def __ror__(
        self: Self,
        value: frozenset[Item_] | set[Item_],
        /,
    ) -> frozenset[Item | Item_] | set[Item | Item_]:
        return set(self.data).__ror__(value)

    @overload
    @setdoc.setdoc(set.__rsub__.__doc__)
    def __rsub__(
        self: Self,
        value: frozenset[object],
        /,
    ) -> frozenset[Item]: ...
    @overload
    @setdoc.setdoc(set.__rsub__.__doc__)
    def __rsub__(
        self: Self,
        value: set[object],
        /,
    ) -> set[Item]: ...

    @setdoc.setdoc(set.__rsub__.__doc__)
    def __rsub__(
        self: Self,
        value: frozenset[object] | set[object],
        /,
    ) -> frozenset[Item] | set[Item]:
        return set(self.data).__rsub__(value)

    @overload
    @setdoc.setdoc(set.__rxor__.__doc__)
    def __rxor__(
        self: Self,
        value: frozenset[Item_],
        /,
    ) -> frozenset[Item | Item_]: ...

    @overload
    @setdoc.setdoc(set.__rxor__.__doc__)
    def __rxor__(
        self: Self,
        value: set[Item_],
        /,
    ) -> set[Item | Item_]: ...

    @setdoc.setdoc(set.__rxor__.__doc__)
    def __rxor__(
        self: Self,
        value: frozenset[Item_] | set[Item_],
        /,
    ) -> frozenset[Item | Item_] | set[Item | Item_]:
        return set(self.data).__rxor__(value)

    @setdoc.setdoc(set.__sub__.__doc__)
    def __sub__(
        self: Self,
        value: frozenset[object] | set[object],
        /,
    ) -> set[Item]:
        return set(self.data).__sub__(value)

    @setdoc.setdoc(set.__xor__.__doc__)
    def __xor__(
        self: Self,
        value: frozenset[Item_] | set[Item_],
        /,
    ) -> set[Item | Item_]:
        return set(self.data).__xor__(value)

    @setdoc.setdoc(set.difference.__doc__)
    def difference(self: Self, /, *others: Iterable[object]) -> set[Item]:
        return set(self.data).difference(*others)

    @setdoc.setdoc(set.intersection.__doc__)
    def intersection(self: Self, /, *others: Iterable[object]) -> set[Item]:
        return set(self.data).intersection(*others)

    @setdoc.setdoc(set.isdisjoint.__doc__)
    def isdisjoint(self: Self, other: Iterable[object], /) -> bool:
        return set(self.data).isdisjoint(other)

    @setdoc.setdoc(set.issubset.__doc__)
    def issubset(self: Self, other: Iterable[object], /) -> bool:
        return set(self.data).issubset(other)

    @setdoc.setdoc(set.issuperset.__doc__)
    def issuperset(self: Self, other: Iterable[object], /) -> bool:
        return set(self.data).issuperset(other)

    @setdoc.setdoc(set.symmetric_difference.__doc__)
    def symmetric_difference(
        self: Self,
        other: Iterable[Item_],
        /,
    ) -> set[Item | Item_]:
        return set(self.data).symmetric_difference(other)

    @setdoc.setdoc(set.union.__doc__)
    def union(self: Self, /, *others: Iterable[Item_]) -> set[Item | Item_]:
        return set(self.data).union(*others)
