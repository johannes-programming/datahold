from __future__ import annotations

__all__: list[str] = [
    "FrozenDictLike",
]

from collections import abc
from typing import Any, Self

from datahold._core.DictLike import DictLike
from datahold._core.typing import DictInit

###


class FrozenDictLike[Key: abc.Hashable, Value](DictLike[Key, Value]):
    """Hashable abstract mapping specialization."""

    __slots__ = ()

    # __frozen__ is inherited as an abstract requirement from DictLike.
    def __hash__(self: Self, /) -> int:
        return hash(self.__frozen__())

    # __init__ is inherited as an abstract requirement from DictLike.

    def __or__[Key_: abc.Hashable, Value_](
        self: Self, other: DictLike[Key_, Value_], /
    ) -> FrozenDictLike[Key | Key_, Value | Value_]:
        if not isinstance(other, DictLike):
            return NotImplemented
        return type(self).__type__(
            self.__frozen__() | other.__frozen__()  # type: ignore[arg-type]
        )

    @classmethod
    def __type__[Key_: abc.Hashable, Value_](
        cls: type[Any], data: DictInit[Key_, Value_], /
    ) -> FrozenDictLike[Key_, Value_]:
        return cls(data)  # type: ignore[no-any-return]
