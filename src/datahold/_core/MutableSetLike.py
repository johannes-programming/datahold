from __future__ import annotations

__all__: list[str] = [
    "MutableSetLike",
]

from abc import abstractmethod
from collections import abc
from typing import Any, Self

from datahold._core.SetLike import SetLike
from datahold._core.typing import ContextManager

###


class MutableSetLike[Item: abc.Hashable](SetLike[Item], abc.MutableSet[Item]):
    """Mutable set operations committed through a context manager."""

    type Mutable[MutableItem: abc.Hashable] = set[MutableItem]

    __slots__ = ()

    def __frozen__(self: Self, /) -> frozenset[Item]:
        mutable: set[Item]
        with self.__mutate__() as mutable:
            return frozenset(mutable)

    __hash__ = None  # type: ignore[assignment]

    def __iand__(  # type: ignore[misc, unused-ignore]
        self: Self,
        other: abc.Set[Item],
        /,
    ) -> MutableSetLike[Item]:
        mutable: set[Item]
        if not isinstance(other, abc.Set):
            return NotImplemented
        with self.__mutate__() as mutable:
            mutable.intersection_update(other)
        return self

    def __init__(self: Self, other: abc.Iterable[Item] = (), /) -> None:
        self.update(other)

    def __ior__(  # type: ignore[misc,override]
        self: Self,
        other: abc.Set[Item],
        /,
    ) -> MutableSetLike[Item]:
        mutable: set[Item]
        if not isinstance(other, abc.Set):
            return NotImplemented
        with self.__mutate__() as mutable:
            mutable.update(other)
        return self

    def __isub__(  # type: ignore[misc, unused-ignore]
        self: Self,
        other: abc.Set[Item],
        /,
    ) -> MutableSetLike[Item]:
        mutable: set[Item]
        if not isinstance(other, abc.Set):
            return NotImplemented
        with self.__mutate__() as mutable:
            mutable.difference_update(other)
        return self

    def __ixor__(  # type: ignore[misc,override]
        self: Self,
        other: abc.Set[Item],
        /,
    ) -> MutableSetLike[Item]:
        mutable: set[Item]
        if not isinstance(other, abc.Set):
            return NotImplemented
        with self.__mutate__() as mutable:
            mutable.symmetric_difference_update(other)
        return self

    @abstractmethod
    def __mutate__(self: Self, /) -> ContextManager[set[Item]]:
        """Yield a mutable working set and commit on successful exit."""

    @classmethod
    def __type__[Item_: abc.Hashable](
        cls: type[Any], data: abc.Iterable[Item_], /
    ) -> MutableSetLike[Item_]:
        # redoing the same method is necessary because copy must return MutableSetLike[Item]
        return cls(data)  # type: ignore[no-any-return]

    def add(self: Self, item: Item, /) -> None:
        mutable: set[Item]
        with self.__mutate__() as mutable:
            mutable.add(item)

    # clear is inherited from abc.MutableSet.
    def copy(self: Self, /) -> MutableSetLike[Item]:
        return type(self).__type__(self.__frozen__())

    def difference_update(self: Self, /, *others: abc.Iterable[Item]) -> None:
        mutable: set[Item]
        with self.__mutate__() as mutable:
            mutable.difference_update(*others)

    def discard(self: Self, item: abc.Hashable, /) -> None:
        mutable: set[Item]
        with self.__mutate__() as mutable:
            mutable.discard(item)

    def intersection_update(
        self: Self, /, *others: abc.Iterable[Item]
    ) -> None:
        mutable: set[Item]
        with self.__mutate__() as mutable:
            mutable.intersection_update(*others)

    def pop(self: Self, /) -> Item:
        mutable: set[Item]
        with self.__mutate__() as mutable:
            return mutable.pop()

    # remove is inherited from abc.MutableSet.
    def symmetric_difference_update(
        self: Self, other: abc.Iterable[Item], /
    ) -> None:
        mutable: set[Item]
        with self.__mutate__() as mutable:
            mutable.symmetric_difference_update(other)

    def update(self: Self, /, *others: abc.Iterable[Item]) -> None:
        mutable: set[Item]
        with self.__mutate__() as mutable:
            mutable.update(*others)
