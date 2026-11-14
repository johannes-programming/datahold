from __future__ import annotations

__all__: list[str] = [
    "SupportsGT",
]

from typing import Protocol, Self, TypeVar

Other = TypeVar("Other", contravariant=True)

### TYPING ###


class SupportsGT(Protocol[Other]):
    def __gt__(self: Self, other: Other, /) -> bool: ...
