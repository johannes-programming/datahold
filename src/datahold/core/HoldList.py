from typing import Self, TypeVar
from collections.abc import Iterable

import setdoc

from ..base.BaseHoldList import BaseHoldList
from .DataList import DataList
from .HoldObject import HoldObject

__all__ = ["HoldList"]

Item = TypeVar("Item")


class HoldList(HoldObject, DataList[Item], BaseHoldList[Item]):

    __slots__ = ()

    @property
    @setdoc.basic
    def data(self: Self) -> tuple[Item, ...]:
        return self._data

    @data.setter
    def data(self: Self, value: Iterable[Item]) -> None:
        self._data = tuple(value)
