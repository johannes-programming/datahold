from __future__ import annotations

__all__: list[str] = [
    "SupportsLE",
]

from typing import Protocol, Self

### TYPING ###


class SupportsLE[Other](Protocol):
    def __le__(self: Self, other: Other, /) -> bool: ...
