"""Provide HashableCollection."""

__all__: list[str] = ["HashableCollection"]

from collections.abc import Sized, Iterable, Container, Hashable, Collection
from typing import Protocol, Self, TypeVar

import setdoc

Item = TypeVar("Item", covariant=True)


class HashableCollection(
    Sized, 
    Iterable[Item], 
    Container[Hashable], 
    Collection[Item],
    Protocol[Item],
):
    @setdoc.basic
    def __hash__(self: Self) -> int: ...
