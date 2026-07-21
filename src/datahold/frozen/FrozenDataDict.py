"""Provide FrozenDataDict."""

__all__: list[str] = ["FrozenDataDict"]

from ..base.BaseDataDict import BaseDataDict
from collections.abc import Hashable
import setdoc
from typing import Self

class FrozenDataDict[Key, Value](
    BaseDataDict[Key, Value],
    Hashable,
):
    __slots__ = ()
    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.data)
