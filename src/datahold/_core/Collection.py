from __future__ import annotations

__all__: list[str] = [
    "Collection",
]

from abc import abstractmethod
from collections import abc
from typing import Generic, Never, Protocol, Self, TypeVar

Item = TypeVar("Item", covariant=True)
FrozenItem = TypeVar("FrozenItem", covariant=True)

### BASE ###


class Collection(
    abc.Sized, abc.Iterable[Item], abc.Container[object], Generic[Item]
):
    class Frozen(
        abc.Sized,
        abc.Iterable[FrozenItem],
        abc.Container[Never],
        abc.Hashable,
        Protocol[FrozenItem],
    ): ...

    __slots__ = ()

    def __contains__(self: Self, other: object, /) -> bool:
        try:
            return other in self.__frozen__()
        except TypeError:
            return False

    @abstractmethod
    def __frozen__(self: Self, /) -> Collection.Frozen[Item]: ...
    def __iter__(self: Self, /) -> abc.Iterator[Item]:
        return iter(self.__frozen__())

    def __len__(self: Self, /) -> int:
        return len(self.__frozen__())
