"""Provide HoldList."""

__all__: list[str] = ["HoldList"]

from collections.abc import Iterable
from typing import Self, TypeVar

import setdoc

from ..base.BaseHoldList import BaseHoldList
from .DataList import DataList
from .HoldObject import HoldObject

Item = TypeVar("Item")


class HoldList(DataList[Item], BaseHoldList[Item], HoldObject):

    __slots__ = ()

    @property
    @setdoc.basic
    def data(self: Self) -> tuple[Item, ...]:
        return self._data

    @data.setter
    @setdoc.basic
    def data(self: Self, value: Iterable[Item]) -> None:
        self._data = tuple(value)
