from __future__ import annotations

__all__: list[str] = [
    "MutableDictSlot",
]

from collections import abc
from contextlib import contextmanager
from typing import Self

from frozendict import frozendict

from datahold._core.MutableDictLike import MutableDictLike

###


class MutableDictSlot[Key: abc.Hashable, Value](MutableDictLike[Key, Value]):
    """Mutable dictionary backed by a frozen dictionary slot."""

    __slots__ = ("_slot",)

    # __init__ is inherited from MutableDictLike.
    @contextmanager
    def __mutate__(self: Self, /) -> abc.Iterator[dict[Key, Value]]:
        mutable: dict[Key, Value]
        mutable = dict(getattr(self, "_slot", ()))
        yield mutable
        self._slot = frozendict(mutable)
