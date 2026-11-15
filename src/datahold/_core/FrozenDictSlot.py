from __future__ import annotations

__all__: list[str] = [
    "FrozenDictSlot",
]

from collections import abc
from typing import Any, Self, TypeVar, overload

from frozendict import frozendict

from datahold._core.dictable import dictable
from datahold._core.DictInit import DictInit
from datahold._core.DictLike import DictLike
from datahold._core.FrozenDictLike import FrozenDictLike

Key = TypeVar("Key", bound=abc.Hashable, covariant=True)
Value = TypeVar("Value", covariant=True)
InitKey = TypeVar("InitKey", bound=abc.Hashable, covariant=True)


class FrozenDictSlot(FrozenDictLike[Key, Value]):
    """A frozendict held in one instance slot."""

    __slots__ = ("_slot",)

    def __frozen__(self: Self, /) -> frozendict[Key, Value]:
        return self._slot

    # __hash__ is inherited from FrozenDictLike.

    @overload
    def __init__(
        self: Self,
        other: DictInit[Key, Value] = (),
        /,
    ) -> None: ...

    @overload
    def __init__(
        self: DictLike[InitKey | str, Value],
        other: DictInit[InitKey | str, Value] = (),
        /,
        **kwargs: Value,
    ) -> None: ...

    def __init__(
        self: Any,
        other: Any = (),
        /,
        **kwargs: Any,
    ) -> None:
        self._slot = frozendict(
            dictable(other),  # type: ignore[arg-type]
            **kwargs,
        )
