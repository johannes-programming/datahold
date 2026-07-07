"""Provide HashableContainer."""

__all__: list[str] = ["HashableContainer"]

from collections.abc import Container, Hashable
from typing import Protocol, Self

import setdoc



class HashableContainer(Container[Hashable], Protocol):
    @setdoc.basic
    def __hash__(self: Self) -> int: ...
