from collections.abc import Iterable
from typing import Any, Protocol, TypeVar

Key = TypeVar("Key", covariant=True)
Value = TypeVar("Value", covariant=True)

__all__ = ["SupportsKeysAndGetitem"]


class SupportsKeysAndGetitem(Protocol[Key, Value]):
    def keys(self) -> Iterable[Key]: ...

    def __getitem__(self, key: Any, /) -> Value: ...
