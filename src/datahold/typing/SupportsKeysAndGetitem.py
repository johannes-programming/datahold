"""Provide SupportsKeysAndGetitem."""

from collections.abc import Hashable, Iterable
from typing import Any, Protocol, Self, TypeVar

__all__ = ["SupportsKeysAndGetitem"]
Key = TypeVar("Key", bound=Hashable, covariant=True)
Value = TypeVar("Value", covariant=True)


class SupportsKeysAndGetitem(Protocol[Key, Value]):
    def __getitem__(self: Self, key: Any, /) -> Value: ...
    def keys(self: Self) -> Iterable[Key]: ...
