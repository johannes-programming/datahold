"""Provide FrozenHoldList."""

from __future__ import annotations

__all__: list[str] = ["FrozenHoldList"]

from typing import Self

import setdoc

from ..base.BaseHoldList import BaseHoldList
from .FrozenDataList import FrozenDataList
from .FrozenHoldObject import FrozenHoldObject


class FrozenHoldList[Item](
    FrozenDataList[Item],
    BaseHoldList[Item],
    FrozenHoldObject,
):
    """Provide usable frozen list-like with slots."""

    __slots__ = ()

    @setdoc.basic
    def __init__(self: Self, data: FrozenHoldList.Init[Item] = (), /) -> None:
        self._data: FrozenHoldList.Data[Item] = tuple(data)

    @property
    @setdoc.basic
    def data(self: Self) -> FrozenHoldList.Data[Item]:
        return self._data
