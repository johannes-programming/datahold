"""Provide HoldList."""

from __future__ import annotations

__all__: list[str] = ["HoldList"]

from collections.abc import Iterable
from typing import Self

import setdoc

from ..base.BaseHoldList import BaseHoldList
from .DataList import DataList


class HoldList[Item](
    DataList[Item],
    BaseHoldList[Item],
):

    __slots__ = ()

    @property
    @setdoc.basic
    def data(self: Self) -> HoldList.Data[Item]:
        return self._data

    @data.setter
    @setdoc.basic
    def data(self: Self, value: Iterable[Item]) -> None:
        self._data: HoldList.Data[Item] = tuple(value)
