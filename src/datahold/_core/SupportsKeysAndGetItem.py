from __future__ import annotations

__all__: list[str] = [
    "SupportsKeysAndGetItem",
]

from collections import abc
from typing import Protocol, Self, runtime_checkable

### TYPING ###


# the dublication is a concession to mypy mistyping Mapping.__getitem__ and frozendict.__getitem__
@runtime_checkable
class SupportsKeysAndGetItem[Key: abc.Hashable, Value](Protocol):
    def __getitem__(self: Self, key: abc.Hashable, /) -> Value: ...
    def keys(self: Self, /) -> abc.Iterable[Key]: ...
