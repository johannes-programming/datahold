from __future__ import annotations

__all__: list[str] = [
    "FrozenDictSlot",
]

from collections import abc
from typing import Any, Self, overload

from frozendict import frozendict

from datahold._core.dictable import dictable
from datahold._core.DictInit import DictInit
from datahold._core.DictLike import DictLike
from datahold._core.FrozenDictLike import FrozenDictLike

###


class FrozenDictSlot[Key: abc.Hashable, Value](FrozenDictLike[Key, Value]):
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
    def __init__[Key_: abc.Hashable](
        self: DictLike[Key_ | str, Value],
        other: DictInit[Key_ | str, Value] = (),
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
