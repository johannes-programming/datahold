"""Provide FrozenDataSet."""

__all__: list[str] = ["FrozenDataSet"]


from ..base.BaseDataSet import BaseDataSet
from collections.abc import Hashable
import setdoc
from typing import Self

class FrozenDataSet[Item](BaseDataSet[Item], Hashable):

    __slots__ = ()
    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.data)
