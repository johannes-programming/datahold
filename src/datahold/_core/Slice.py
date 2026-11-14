from __future__ import annotations

__all__: list[str] = [
    "Slice",
]

from types import GenericAlias
from typing import TypeAlias, TypeVar

Index = TypeVar("Index")


### TYPING ###

Slice: TypeAlias = GenericAlias(slice, (Index, Index, Index))
