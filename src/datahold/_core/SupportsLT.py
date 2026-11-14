from __future__ import annotations

__all__: list[str] = [
    "SupportsLT",
]

from typing import Protocol, Self

### TYPING ###


class SupportsLT[Other](Protocol):
    def __lt__(self: Self, other: Other, /) -> bool: ...
