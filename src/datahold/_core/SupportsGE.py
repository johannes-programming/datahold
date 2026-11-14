from __future__ import annotations

__all__: list[str] = [
    "SupportsGE",
]

from typing import Protocol, Self, TypeVar

Other = TypeVar("Other", contravariant=True)

### TYPING ###


class SupportsGE(Protocol[Other]):
    def __ge__(self: Self, other: Other, /) -> bool: ...
