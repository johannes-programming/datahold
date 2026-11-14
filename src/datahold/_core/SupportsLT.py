from __future__ import annotations

__all__: list[str] = [
    "SupportsLT",
]

from typing import Protocol, Self, TypeVar

Other = TypeVar("Other", contravariant=True)

### TYPING ###


class SupportsLT(Protocol[Other]):
    def __lt__(self: Self, other: Other, /) -> bool: ...
