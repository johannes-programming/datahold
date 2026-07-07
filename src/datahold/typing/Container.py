"""Provide Container."""

__all__: list[str] = ["Container"]

from collections.abc import Container as Container_
from collections.abc import Hashable


class Container(Container_[Hashable]):
    __slots__ = ()
