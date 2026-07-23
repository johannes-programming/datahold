"""Provide HoldList."""

from __future__ import annotations

__all__: list[str] = ["HoldList"]

from collections.abc import Iterable
from typing import Self

import setdoc

from ..base.BaseHoldCollection import BaseHoldCollection
from .DataList import DataList


class HoldList[Item](
    DataList[Item],
    BaseHoldCollection[Item],
):
    """Provide usable mutable list-like with slots."""

    __slots__ = ()

    @setdoc.basic
    def __fget__(self: Self) -> HoldList.Data[Item]:
        return self._data

    @setdoc.basic
    def __fset__(self: Self, value: Iterable[Item], /) -> None:
        self._data: HoldList.Data[Item] = tuple(value)
