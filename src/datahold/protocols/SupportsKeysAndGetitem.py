from typing import *

__all__ = ["SupportsKeyAndGetitem"]

Key = TypeVar("Key")
Value = TypeVar("Value")

class SupportsKeyAndGetitem(Protocol, Generic[Key,Value]):
    def __getitem__(self:Self, key:Key) -> Value:
        ...
    def keys(self:Self) -> Iterable[Key]:
        ...