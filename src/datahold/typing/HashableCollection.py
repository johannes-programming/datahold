from collections.abc import Collection
from typing import Protocol, Self, TypeVar

__all__ = ["HashableCollection"]
Item = TypeVar("Item", covariant=True)


class HashableCollection(Collection[Item], Protocol[Item]):
    def __hash__(self: Self) -> int: ...
