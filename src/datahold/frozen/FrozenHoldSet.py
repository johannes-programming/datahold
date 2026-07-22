"""Provide FrozenHoldSet."""

from __future__ import annotations

__all__: list[str] = ["FrozenHoldSet"]

from collections.abc import Hashable
from typing import Self

import setdoc

from ..base.BaseHoldSet import BaseHoldSet
from .FrozenDataSet import FrozenDataSet
from .FrozenHoldObject import FrozenHoldObject


class FrozenHoldSet[Item: Hashable](
    FrozenDataSet[Item],
    BaseHoldSet[Item],
    FrozenHoldObject,
):
    """Provide usable frozen set-like with slots."""

    __slots__ = ()

    @setdoc.basic
    def __init__(self: Self, data: FrozenHoldSet.Init[Item] = (), /) -> None:
        self._data: frozenset[Item] = frozenset(data)

    @property
    @setdoc.basic
    def data(self: Self) -> FrozenHoldSet.Data[Item]:
        return self._data
