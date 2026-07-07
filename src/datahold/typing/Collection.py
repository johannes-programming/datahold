"""Provide Collection."""

__all__: list[str] = ["Collection"]

from collections.abc import Collection as Collection_
from typing import TypeVar

from .Container import Container

Item = TypeVar("Item", covariant=True)


class Collection(Container, Collection_[Item]):
    __slots__ = ()
