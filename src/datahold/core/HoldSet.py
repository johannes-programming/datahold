"""Provide HoldSet."""

from __future__ import annotations

__all__: list[str] = ["HoldSet"]

from collections.abc import Hashable, Iterable
from typing import Self

import setdoc

from ..base.BaseHoldSet import BaseHoldSet
from .DataSet import DataSet
from .HoldObject import HoldObject


class HoldSet[Item: Hashable](
    DataSet[Item],
    BaseHoldSet[Item],
    HoldObject,
):
    """Provide usable mutable set-like with slots."""

    __slots__ = ()

    @property
    @setdoc.basic
    def data(self: Self) -> HoldSet.Data[Item]:
        return self._data

    @data.setter
    @setdoc.basic
    def data(self: Self, value: Iterable[Item]) -> None:
        self._data: HoldSet.Data[Item] = frozenset(value)
