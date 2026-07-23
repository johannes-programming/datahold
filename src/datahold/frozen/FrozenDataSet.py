"""Provide FrozenDataSet."""

__all__: list[str] = ["FrozenDataSet"]

from collections import abc
from typing import Self

import setdoc

from ..base.BaseDataSet import BaseDataSet


class FrozenDataSet[Item: abc.Hashable](BaseDataSet[Item], abc.Hashable):
    """Provide easy abc for custom frozen set-like."""

    __slots__ = ()

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.__fget__())
