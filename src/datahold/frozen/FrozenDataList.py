"""Provide FrozenDataList."""

__all__: list[str] = ["FrozenDataList"]

from collections.abc import Hashable
from typing import Self

import setdoc

from ..base.BaseDataList import BaseDataList


class FrozenDataList[Item](
    BaseDataList[Item],
    Hashable,
):

    __slots__ = ()

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.data)
