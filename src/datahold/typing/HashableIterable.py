"""Provide HashableIterable."""

__all__: list[str] = ["HashableIterable"]

from collections.abc import Iterable
from typing import Protocol, Self, TypeVar

import setdoc

Item = TypeVar("Item", covariant=True)


class HashableIterable(Iterable[Item], Protocol[Item]):
    @setdoc.basic
    def __hash__(self: Self) -> int: ...
