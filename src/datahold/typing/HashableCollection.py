"""Provide HashableCollection."""

__all__: list[str] = ["HashableCollection"]

from collections.abc import Collection
from typing import Protocol, TypeVar

from .HashableContainer import HashableContainer

Item = TypeVar("Item", covariant=True)


class HashableCollection(
    HashableContainer, Collection[Item], Protocol[Item]
): ...
