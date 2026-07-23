"""Provide FrozenHoldSet."""

from __future__ import annotations

__all__: list[str] = ["FrozenHoldSet"]

from collections.abc import Hashable
from typing import Self

import setdoc

from ..base.BaseHoldCollection import BaseHoldCollection
from .FrozenDataSet import FrozenDataSet


class FrozenHoldSet[Item: Hashable](
    FrozenDataSet[Item],
    BaseHoldCollection[Item],
):
    """Provide usable frozen set-like with slots."""

    __slots__ = ()

    @setdoc.basic
    def __fget__(self: Self) -> FrozenHoldSet.Data[Item]:
        return self._data

    @setdoc.basic
    def __fset__(self: Self, data: FrozenHoldSet.Data[Item], /) -> None:
        self._data: FrozenHoldSet.Data[Item] = data

    @setdoc.basic
    def __init__(self: Self, data: FrozenHoldSet.Init[Item] = (), /) -> None:
        self.__fset__(frozenset(data))
