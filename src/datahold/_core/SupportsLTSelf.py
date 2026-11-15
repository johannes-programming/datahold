from __future__ import annotations

__all__: list[str] = [
    "SupportsLTSelf",
]

from typing import Protocol, Self


class SupportsLTSelf(Protocol):
    def __lt__(self: Self, other: Self, /) -> bool: ...
