from __future__ import annotations

__all__: list[str] = [
    "MutableDictSlot",
]

from collections import abc
from contextlib import contextmanager
from typing import Generic, Self, TypeVar

from frozendict import frozendict

from datahold._core.MutableDictLike import MutableDictLike

Key = TypeVar("Key", bound=abc.Hashable)
Value = TypeVar("Value")

###


class MutableDictSlot(MutableDictLike[Key, Value], Generic[Key, Value]):
    """Mutable dictionary backed by a frozen dictionary slot."""

    __slots__ = ("_slot",)

    # __init__ is inherited from MutableDictLike.
    @contextmanager
    def __mutate__(self: Self, /) -> abc.Iterator[dict[Key, Value]]:
        mutable: dict[Key, Value]
        mutable = dict(getattr(self, "_slot", ()))
        yield mutable
        self._slot = frozendict(mutable)
