from __future__ import annotations

__all__: list[str] = [
    "FrozenDictLike",
]

from collections import abc
from typing import Any, Self, TypeVar

from frozendict import frozendict

from datahold._core.DictInit import DictInit
from datahold._core.DictLike import DictLike

Key = TypeVar("Key", bound=abc.Hashable, covariant=True)
Value = TypeVar("Value", covariant=True)
OrKey = TypeVar("OrKey", bound=abc.Hashable)
OrValue = TypeVar("OrValue")
TypeKey = TypeVar("TypeKey", bound=abc.Hashable)
TypeValue = TypeVar("TypeValue")


class FrozenDictLike(DictLike[Key, Value]):
    """Hashable abstract mapping specialization."""

    __slots__ = ()

    # __frozen__ is inherited as an abstract requirement from DictLike.
    def __hash__(self: Self, /) -> int:
        return hash(self.__frozen__())

    # __init__ is inherited as an abstract requirement from DictLike.

    def __or__(
        self: Self, other: DictLike[OrKey, OrValue], /
    ) -> FrozenDictLike[Key | OrKey, Value | OrValue]:
        other_: frozendict[Key | OrKey, Value | OrValue]
        if not isinstance(other, DictLike):
            return NotImplemented
        other_ = self.__frozen__() | other.__frozen__()
        return type(self).__type__(
            other_,  # type: ignore[arg-type]
        )

    @classmethod
    def __type__(
        cls: type[Any], other: DictInit[TypeKey, TypeValue], /
    ) -> FrozenDictLike[TypeKey, TypeValue]:
        return cls(other)  # type: ignore[no-any-return]
