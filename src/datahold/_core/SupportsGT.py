from __future__ import annotations

__all__: list[str] = [
    "SupportsGT",
]

from typing import Protocol, Self

### TYPING ###


class SupportsGT[Other](Protocol):
    def __gt__(self: Self, other: Other, /) -> bool: ...
