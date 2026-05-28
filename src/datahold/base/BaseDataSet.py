from abc import abstractmethod
from collections.abc import Iterable, Iterator
from collections.abc import Set as AbstractSet
from typing import Any, Generic, Self, TypeVar, cast, overload

import setdoc

from .BaseDataObject import BaseDataObject

__all__ = ["BaseDataSet"]

Item = TypeVar("Item", covariant=True)
Item_ = TypeVar("Item_")


class BaseDataSet(BaseDataObject, Generic[Item]):
    __slots__ = ()

    @overload
    @setdoc.basic
    def __and__(self: Self, other: frozenset[object], /) -> set[Item]: ...

    @overload
    @setdoc.basic
    def __and__(self: Self, other: set[object], /) -> set[Item]: ...

    @setdoc.basic
    def __and__(
        self: Self,
        other: frozenset[object] | set[object],
        /,
    ) -> set[Item]:
        return set(self.data).__and__(other)

    @setdoc.basic
    def __contains__(self: Self, other: object, /) -> bool:
        return set(self.data).__contains__(other)

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Iterable[Item_] = (), /) -> None: ...

    @setdoc.basic
    def __iter__(self: Self, /) -> Iterator[Item]:
        return set(self.data).__iter__()

    @setdoc.basic
    def __len__(self: Self, /) -> int:
        return set(self.data).__len__()

    @overload
    @setdoc.basic
    def __or__(
        self: Self, other: frozenset[Item_], /
    ) -> set[Item | Item_]: ...

    @overload
    @setdoc.basic
    def __or__(self: Self, other: set[Item_], /) -> set[Item | Item_]: ...

    @setdoc.basic
    def __or__(
        self: Self,
        other: Any,
        /,
    ) -> Any:
        return set(self.data).__or__(other)

    @overload
    @setdoc.basic
    def __rand__(
        self: Self, other: frozenset[object], /
    ) -> frozenset[Item]: ...

    @overload
    @setdoc.basic
    def __rand__(self: Self, other: set[object], /) -> set[Item]: ...

    @setdoc.basic
    def __rand__(
        self: Self,
        other: Any,
        /,
    ) -> Any:
        return set(self.data).__rand__(other)  # type: ignore[attr-defined]

    @setdoc.setdoc(set.__repr__.__doc__)
    def __repr__(self: Self, /) -> str:
        return set(self.data).__repr__()

    @overload
    @setdoc.basic
    def __ror__(
        self: Self,
        other: frozenset[Item_],
        /,
    ) -> frozenset[Item | Item_]: ...

    @overload
    @setdoc.basic
    def __ror__(
        self: Self,
        other: set[Item_],
        /,
    ) -> set[Item | Item_]: ...

    @setdoc.basic
    def __ror__(
        self: Self,
        other: Any,
        /,
    ) -> Any:
        return set(self.data).__ror__(other)  # type: ignore[attr-defined]

    @overload
    @setdoc.basic
    def __rsub__(
        self: Self,
        other: frozenset[Item_],
        /,
    ) -> frozenset[Item_]: ...

    @overload
    @setdoc.basic
    def __rsub__(
        self: Self,
        other: set[Item_],
        /,
    ) -> set[Item_]: ...

    @setdoc.basic
    def __rsub__(
        self: Self,
        other: Any,
        /,
    ) -> Any:
        return set(self.data).__rsub__(other)  # type: ignore[attr-defined]

    @overload
    @setdoc.basic
    def __rxor__(
        self: Self, other: frozenset[Item_], /
    ) -> frozenset[Item | Item_]: ...

    @overload
    @setdoc.basic
    def __rxor__(self: Self, other: set[Item_], /) -> set[Item | Item_]: ...

    @setdoc.basic
    def __rxor__(self: Self, other: Any, /) -> Any:
        return set(self.data).__rxor__(other)  # type: ignore[attr-defined]

    @setdoc.basic
    def __sub__(
        self: Self,
        other: frozenset[object] | set[object],
        /,
    ) -> set[Item]:
        return set(self.data).__sub__(other)

    @setdoc.basic
    def __xor__(
        self: Self,
        other: frozenset[Item_] | set[Item_],
        /,
    ) -> set[Item | Item_]:
        return set(self.data).__xor__(other)

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


AbstractSet.register(BaseDataSet)  # type: ignore[type-abstract]
