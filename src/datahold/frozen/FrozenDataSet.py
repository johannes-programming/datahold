"""Provide FrozenDataSet."""

__all__: list[str] = ["FrozenDataSet"]


from collections.abc import Hashable
from typing import Self

import setdoc

from ..base.BaseDataSet import BaseDataSet


class FrozenDataSet[Item](BaseDataSet[Item], Hashable):

    __slots__ = ()

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.data)
