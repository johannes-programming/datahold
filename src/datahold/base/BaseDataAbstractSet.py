from __future__ import annotations

__all__: list[str] = ["BaseDataAbstractSet"]
from collections.abc import Set
from typing import TypeVar

from .BaseDataCollection import BaseDataCollection

Item = TypeVar("Item", covariant=True)


class BaseDataAbstractSet(BaseDataCollection[Item], Set[Item]):
    """Act as base class for (abstract) set implementation which only has to override __fget__ and __fset__ to work immediately."""

    __slots__ = ()
