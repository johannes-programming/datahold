"""Provide HoldSet."""

__all__ = ["HoldSet"]

from collections.abc import Hashable, Iterable
from typing import Self, TypeVar

import setdoc

from ..base.BaseHoldSet import BaseHoldSet
from .DataSet import DataSet
from .HoldObject import HoldObject

Item = TypeVar("Item", bound=Hashable)


class HoldSet(HoldObject, DataSet[Item], BaseHoldSet[Item]):

    __slots__ = ()

    @property
    @setdoc.basic
    def data(self: Self) -> frozenset[Item]:
        return self._data

    @data.setter
    @setdoc.basic
    def data(self: Self, value: Iterable[Item]) -> None:
        self._data = frozenset(value)
