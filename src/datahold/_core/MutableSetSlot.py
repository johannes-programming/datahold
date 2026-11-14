from __future__ import annotations

__all__: list[str] = [
    "MutableSetSlot",
]

from collections import abc
from contextlib import contextmanager
from typing import Self

from datahold._core.MutableSetLike import MutableSetLike

###


class MutableSetSlot[Item: abc.Hashable](MutableSetLike[Item]):
    """Mutable set with transactional replacement of a frozenset slot."""

    __slots__ = ("_slot",)

    # __init__ is inherited from MutableSetLike.

    @contextmanager
    def __mutate__(self: Self, /) -> abc.Iterator[set[Item]]:
        mutable: set[Item]
        mutable = set(getattr(self, "_slot", ()))
        yield mutable
        self._slot = frozenset(mutable)
