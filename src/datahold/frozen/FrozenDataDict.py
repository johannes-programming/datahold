"""Provide FrozenDataDict."""

__all__: list[str] = ["FrozenDataDict"]

from collections.abc import Hashable
from typing import Self

import setdoc

from ..base.BaseDataDict import BaseDataDict


class FrozenDataDict[Key, Value](
    BaseDataDict[Key, Value],
    Hashable,
):
    __slots__ = ()

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.data)
