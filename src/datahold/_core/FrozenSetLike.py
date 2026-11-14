from __future__ import annotations

__all__: list[str] = [
    "FrozenSetLike",
]

from collections import abc
from typing import Self

from datahold._core.SetLike import SetLike

###


class FrozenSetLike[Item: abc.Hashable](SetLike[Item]):
    """Hashable abstract set specialization."""

    __slots__ = ()

    # __frozen__ is inherited as an abstract requirement from SetLike.
    def __hash__(self: Self, /) -> int:
        return hash(self.__frozen__())

    # __init__ is inherited as an abstract requirement from SetLike.
