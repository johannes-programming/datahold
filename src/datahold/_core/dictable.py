from __future__ import annotations

__all__: list[str] = [
    "dictable",
]

from collections import abc

from datahold._core.DictInit import DictInit
from datahold._core.SupportsKeysAndGetItem import SupportsKeysAndGetItem

### HELPER ###


# circumvent the rare case that other has keys but not __getitem__
def dictable[Key: abc.Hashable, Value](
    other: DictInit[Key, Value],
    /,
) -> DictInit[Key, Value]:
    if isinstance(other, SupportsKeysAndGetItem):
        return other
    else:
        return (item for item in other)
