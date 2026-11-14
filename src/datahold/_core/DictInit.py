from __future__ import annotations

__all__: list[str] = [
    "DictInit",
]

from collections import abc

from typing_extensions import TypeAliasType, TypeVar

from datahold._core.SupportsKeysAndGetItem import SupportsKeysAndGetItem

Key = TypeVar("Key", covariant=True)
Value = TypeVar("Value", covariant=True)

DictInit: TypeAliasType = TypeAliasType(
    "DictInit",
    SupportsKeysAndGetItem[Key, Value] | abc.Iterable[tuple[Key, Value]],
    type_params=(Key, Value),
)
