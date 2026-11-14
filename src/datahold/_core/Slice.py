from __future__ import annotations

__all__: list[str] = [
    "Slice",
]

from typing import TypeVar

from typing_extensions import TypeAliasType

Index = TypeVar("Index", covariant=True)

Slice: TypeAliasType = TypeAliasType(
    "Slice",
    slice[Index, Index, Index],
    type_params=(Index,),
)
