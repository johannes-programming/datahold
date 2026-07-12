from __future__ import annotations

__all__: list[str] = ["BaseDataAbstractSet"]
from collections.abc import Set
from typing import TypeVar
from .BaseDataCollection import BaseDataCollection


DataItem = TypeVar("DataItem", covariant=True)
Item = TypeVar("Item", covariant=True)

class BaseDataAbstractSet(BaseDataCollection[Item], Set[Item]):
    """Act as a base class for concrete set implementations backed by a data attribute."""

    # this abc exists to provide the easiest possible template for a Set
    # a subclass must only override __fget__ and __fset__
    # and it is immediately non-abstract

    __slots__ = ()
