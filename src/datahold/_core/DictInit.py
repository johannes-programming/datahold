from __future__ import annotations

__all__: list[str] = [
    "DictInit",
]

from collections import abc

from datahold._core.SupportsKeysAndGetItem import SupportsKeysAndGetItem

### TYPING ###


type DictInit[Key, Value] = SupportsKeysAndGetItem[Key, Value] | abc.Iterable[
    tuple[Key, Value]
]
