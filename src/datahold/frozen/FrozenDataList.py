"""Provide FrozenDataList."""

__all__: list[str] = ["FrozenDataList"]

from ..base.BaseDataList import BaseDataList
from collections.abc import Hashable
import setdoc
from typing import Self

class FrozenDataList[Item](
    BaseDataList[Item],
    Hashable,
):

    __slots__ = ()
    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.data)
