"""Provide FrozenDataDict."""

__all__: list[str] = ["FrozenDataDict"]

from collections import abc
from typing import Self

import setdoc

from ..base.BaseDataDict import BaseDataDict


class FrozenDataDict[Key: abc.Hashable, Value](
    BaseDataDict[Key, Value],
    abc.Hashable,
):
    """Provide easy abc for custom frozen dict-like."""

    __slots__ = ()

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.__fget__())
