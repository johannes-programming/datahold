from __future__ import annotations

from types import GenericAlias
from typing import TypeAlias, TypeVar

Index = TypeVar("Index")

__all__: list[str] = [
    "Slice",
]


### TYPING ###

Slice: TypeAlias = GenericAlias(slice, (Index, Index, Index))
