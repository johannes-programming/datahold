from __future__ import annotations

__all__: list[str] = [
    "FrozenListSlot",
]

from collections import abc
from typing import Self

from datahold._core.FrozenListLike import FrozenListLike

###


class FrozenListSlot[Item](FrozenListLike[Item]):
    """A tuple stored in one instance slot."""

    __slots__ = ("_slot",)

    def __frozen__(self: Self, /) -> tuple[Item, ...]:
        return self._slot

    # __hash__ is inherited from FrozenListLike.
    def __init__(self: Self, other: abc.Iterable[Item] = (), /) -> None:
        self._slot = tuple(other)
