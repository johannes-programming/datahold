"""Provide HashableCollection."""

__all__: list[str] = ["HashableCollection"]

from typing import Protocol, Self, TypeVar

import setdoc

from .Collection import Collection

Item = TypeVar("Item", covariant=True)


class HashableCollection(Collection[Item], Protocol[Item]):
    @setdoc.basic
    def __hash__(self: Self) -> int: ...
