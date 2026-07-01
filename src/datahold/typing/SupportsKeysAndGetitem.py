"""Provide SupportsKeysAndGetitem."""

__all__: list[str] = ["SupportsKeysAndGetitem"]

from collections.abc import Hashable, Iterable
from typing import Any, Protocol, Self, TypeVar

import setdoc

Key = TypeVar("Key", bound=Hashable, covariant=True)
Value = TypeVar("Value", covariant=True)


class SupportsKeysAndGetitem(Protocol[Key, Value]):

    @setdoc.basic
    def __getitem__(self: Self, key: Any, /) -> Value: ...

    @setdoc.basic
    def keys(self: Self) -> Iterable[Key]: ...
