from __future__ import annotations

__all__: list[str] = [
    "MutableListSlot",
]

from collections import abc
from contextlib import contextmanager
from typing import Self

from datahold._core.MutableListLike import MutableListLike

###


class MutableListSlot[Item](MutableListLike[Item]):
    """Mutable sequence with transactional replacement of a tuple slot."""

    __slots__ = ("_slot",)

    # __init__ is inherited from MutableListLike.

    @contextmanager
    def __mutate__(self: Self, /) -> abc.Iterator[list[Item]]:
        mutable: list[Item]
        mutable = list(getattr(self, "_slot", ()))
        yield mutable
        self._slot = tuple(mutable)
