"""Provide HashableCollection."""

__all__: list[str] = ["HashableCollection"]

from collections.abc import Collection
from collections.abc import Container as Container_
from collections.abc import Hashable
from typing import Protocol, Self, TypeVar

import setdoc


class Container(Container_[Hashable], Protocol): ...


Item = TypeVar("Item", covariant=True)


class HashableCollection(Container, Collection[Item], Protocol[Item]):
    @setdoc.basic
    def __hash__(self: Self) -> int: ...
