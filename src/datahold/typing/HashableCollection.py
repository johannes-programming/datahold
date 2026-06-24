"""Provide HashableCollection."""

from collections.abc import Collection
from typing import Protocol, Self, TypeVar

import setdoc

__all__ = ["HashableCollection"]
Item = TypeVar("Item", covariant=True)


class HashableCollection(Collection[Item], Protocol[Item]):
    @setdoc.basic
    def __hash__(self: Self) -> int: ...
