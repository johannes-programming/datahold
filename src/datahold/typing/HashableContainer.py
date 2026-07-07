"""Provide HashableContainer."""

__all__: list[str] = ["HashableContainer"]

from collections.abc import Container as Container_
from collections.abc import Hashable
from typing import Protocol, Self

import setdoc


class HashableContainer(Container_[Hashable], Protocol):
    @setdoc.basic
    def __hash__(self: Self) -> int: ...
