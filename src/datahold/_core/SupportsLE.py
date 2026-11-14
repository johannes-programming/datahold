from __future__ import annotations

__all__: list[str] = [
    "SupportsLE",
]

from typing import Protocol, Self, TypeVar

Other = TypeVar("Other", contravariant=True)

### TYPING ###


class SupportsLE(Protocol[Other]):
    def __le__(self: Self, other: Other, /) -> bool: ...
