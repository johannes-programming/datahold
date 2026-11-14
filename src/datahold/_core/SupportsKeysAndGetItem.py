from __future__ import annotations

__all__: list[str] = [
    "SupportsKeysAndGetItem",
]

from collections import abc
from typing import Protocol, Self, TypeVar, runtime_checkable

Key = TypeVar("Key", bound=abc.Hashable, covariant=True)
Value = TypeVar("Value", covariant=True)

### TYPING ###


# the dublication is a concession to mypy mistyping Mapping.__getitem__ and frozendict.__getitem__
@runtime_checkable
class SupportsKeysAndGetItem(Protocol[Key, Value]):
    def __getitem__(self: Self, key: abc.Hashable, /) -> Value: ...
    def keys(self: Self, /) -> abc.Iterable[Key]: ...
