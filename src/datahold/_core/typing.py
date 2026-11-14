from __future__ import annotations

__all__: list[str] = [
    "ContextManager",
    "DictInit",
    "Slice",
    "SupportsGE",
    "SupportsGT",
    "SupportsGTSelf",
    "SupportsKeysAndGetItem",
    "SupportsLE",
    "SupportsLT",
    "SupportsLTSelf",
]

from collections import abc
from types import TracebackType
from typing import Protocol, Self, runtime_checkable

### TYPING ###


# the dublication is a concession to mypy mistyping Mapping.__getitem__ and frozendict.__getitem__
@runtime_checkable
class SupportsKeysAndGetItem[Key: abc.Hashable, Value](Protocol):
    def __getitem__(self: Self, key: abc.Hashable, /) -> Value: ...
    def keys(self: Self, /) -> abc.Iterable[Key]: ...


type DictInit[Key, Value] = SupportsKeysAndGetItem[Key, Value] | abc.Iterable[
    tuple[Key, Value]
]
type Slice[Index] = slice[Index, Index, Index]


class SupportsGE[Other](Protocol):
    def __ge__(self: Self, other: Other, /) -> bool: ...
class SupportsGT[Other](Protocol):
    def __gt__(self: Self, other: Other, /) -> bool: ...
class SupportsLE[Other](Protocol):
    def __le__(self: Self, other: Other, /) -> bool: ...
class SupportsLT[Other](Protocol):
    def __lt__(self: Self, other: Other, /) -> bool: ...


class SupportsGTSelf(Protocol):
    def __gt__(self: Self, other: Self, /) -> bool: ...
class SupportsLTSelf(Protocol):
    def __lt__(self: Self, other: Self, /) -> bool: ...


class ContextManager[Enter](Protocol):
    def __enter__(self: Self, /) -> Enter: ...

    def __exit__(
        self: Self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
        /,
    ) -> object: ...
