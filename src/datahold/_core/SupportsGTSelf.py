from __future__ import annotations

__all__: list[str] = [
    "SupportsGTSelf",
]

from typing import Protocol, Self

### TYPING ###


class SupportsGTSelf(Protocol):
    def __gt__(self: Self, other: Self, /) -> bool: ...
