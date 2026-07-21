"""Provide FrozenHoldList."""

from __future__ import annotations

__all__: list[str] = ["FrozenHoldList"]

from typing import Self

import setdoc

from .FrozenDataList import FrozenDataList
from ..base.BaseHoldCollection import BaseHoldCollection


class FrozenHoldList[Item](
    FrozenDataList[Item],
    BaseHoldCollection[Item],
):

    __slots__ = ()

    @setdoc.basic
    def __init__(self: Self, data: FrozenHoldList.Init[Item] = (), /) -> None:
        self._data: FrozenHoldList.Data[Item] = tuple(data)

    @property
    @setdoc.basic
    def data(self: Self) -> FrozenHoldList.Data[Item]:
        return self._data
