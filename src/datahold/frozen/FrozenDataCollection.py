"""Provide FrozenDataCollection."""

__all__: list[str] = ["FrozenDataCollection"]

from collections.abc import Hashable
from typing import Self

import setdoc

from ..base.BaseDataCollection import BaseDataCollection


class FrozenDataCollection[Item](BaseDataCollection[Item], Hashable):

    __slots__ = ()

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.data)
