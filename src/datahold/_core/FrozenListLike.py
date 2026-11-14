from __future__ import annotations

__all__: list[str] = [
    "FrozenListLike",
]

from typing import Self

from datahold._core.ListLike import ListLike

###


class FrozenListLike[Item](ListLike[Item]):
    """Hashable abstract sequence specialization."""

    __slots__ = ()

    # __frozen__ is inherited as an abstract requirement from ListLike.
    def __hash__(self: Self, /) -> int:
        return hash(self.__frozen__())

    # __init__ is inherited as an abstract requirement from ListLike.
