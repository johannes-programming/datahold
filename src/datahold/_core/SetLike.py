from __future__ import annotations

__all__: list[str] = [
    "SetLike",
]

from abc import abstractmethod
from collections import abc
from reprlib import recursive_repr
from typing import Any, Self

from datahold._core.Collection import Collection

### SET-LIKE ###


class SetLike[Item: abc.Hashable](Collection[Item], abc.Set[Item]):
    """Shared read-only set API; construction and storage remain abstract."""

    type Frozen[FrozenItem: abc.Hashable] = frozenset[FrozenItem]

    __slots__ = ()

    # __and__ is inherited from abc.Set (via the overridable _from_iterable).
    # __contains__ is inherited
    # __eq__ is inherited from abc.Set.
    @abstractmethod
    def __frozen__(self: Self, /) -> frozenset[Item]:
        """Return a frozen snapshot of this set."""

    # __ge__ is inherited from abc.Set.
    # __gt__ is inherited from abc.Set.

    @abstractmethod
    def __init__(self: Self, other: abc.Iterable[Item] = (), /) -> None: ...

    # __iter__ is inherited

    # __le__ is inherited from abc.Set.
    # __len__ is inherited

    # __lt__ is inherited from abc.Set.
    # __ne__ is inherited from object (negates __eq__).
    # __or__ is inherited from abc.Set (via _from_iterable).
    # __rand__ is inherited from abc.Set (via _from_iterable).
    @recursive_repr()
    def __repr__(self: Self, /) -> str:
        return f"{type(self).__name__}({set(self.__frozen__())})"

    # __ror__ is inherited from abc.Set (via _from_iterable).
    # __rsub__ is inherited from abc.Set (via _from_iterable).
    # __rxor__ is inherited from abc.Set (via _from_iterable).
    # __sub__ is inherited from abc.Set (via _from_iterable).
    @classmethod
    def __type__[Item_: abc.Hashable](
        cls: type[Any], data: abc.Iterable[Item_], /
    ) -> SetLike[Item_]:
        return cls(data)  # type: ignore[no-any-return]

    # __xor__ is inherited from abc.Set (via _from_iterable).
    @classmethod
    def _from_iterable[Item_: abc.Hashable](
        cls: type[Any], data: abc.Iterable[Item_], /
    ) -> SetLike[Item_]:
        return cls.__type__(data)  # type: ignore[no-any-return]

    def difference(
        self: Self, /, *others: abc.Iterable[Item]
    ) -> SetLike[Item]:
        return type(self).__type__(self.__frozen__().difference(*others))

    def intersection(
        self: Self, /, *others: abc.Iterable[Item]
    ) -> SetLike[Item]:
        return type(self).__type__(self.__frozen__().intersection(*others))

    # isdisjoint is inherited from abc.Set.
    def issubset(self: Self, other: abc.Iterable[Item], /) -> bool:
        return self.__frozen__().issubset(other)

    def issuperset(self: Self, other: abc.Iterable[Item], /) -> bool:
        return self.__frozen__().issuperset(other)

    def symmetric_difference(
        self: Self, other: abc.Iterable[Item], /
    ) -> SetLike[Item]:
        return type(self).__type__(
            self.__frozen__().symmetric_difference(other)
        )

    def union(self: Self, /, *others: abc.Iterable[Item]) -> SetLike[Item]:
        return type(self).__type__(self.__frozen__().union(*others))
