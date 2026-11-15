from __future__ import annotations

__all__: list[str] = [
    "FrozenSetSlot",
]

from collections import abc
from typing import Self, TypeVar

from datahold._core.FrozenSetLike import FrozenSetLike

Item = TypeVar("Item", bound=abc.Hashable, covariant=True)


class FrozenSetSlot(FrozenSetLike[Item]):
    """A frozenset held in one instance slot."""

    __slots__ = ("_slot",)

    def __frozen__(self: Self, /) -> frozenset[Item]:
        return self._slot

    # __hash__ is inherited from FrozenSetLike.
    def __init__(self: Self, other: abc.Iterable[Item] = (), /) -> None:
        self._slot = frozenset(other)
