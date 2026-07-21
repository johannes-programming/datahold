"""Provide HoldSet."""

from __future__ import annotations

__all__: list[str] = ["HoldSet"]

from collections.abc import Hashable, Iterable
from typing import Self, TypeVar

import setdoc

from ..base.BaseHoldCollection import BaseHoldCollection
from .DataSet import DataSet

Item = TypeVar("Item", bound=Hashable)


class HoldSet[Item: Hashable](
    DataSet[Item],
    BaseHoldCollection[Item],
):

    __slots__ = ()

    @property
    @setdoc.basic
    def data(self: Self) -> HoldSet.Data[Item]:
        return self._data

    @data.setter
    @setdoc.basic
    def data(self: Self, value: Iterable[Item]) -> None:
        self._data: HoldSet.Data[Item] = frozenset(value)
