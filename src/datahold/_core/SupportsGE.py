from __future__ import annotations

__all__: list[str] = [
    "SupportsGE",
]

from typing import Protocol, Self

### TYPING ###


class SupportsGE[Other](Protocol):
    def __ge__(self: Self, other: Other, /) -> bool: ...
