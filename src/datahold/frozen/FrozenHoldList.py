"""Provide FrozenHoldList."""

from __future__ import annotations

__all__: list[str] = ["FrozenHoldList"]

from typing import Self

import setdoc

from ..base.BaseHoldCollection import BaseHoldCollection
from .FrozenDataList import FrozenDataList


class FrozenHoldList[Item](
    FrozenDataList[Item],
    BaseHoldCollection[Item],
):
    """Provide usable frozen list-like with slots."""

    __slots__ = ()

    @setdoc.basic
    def __fget__(self: Self) -> FrozenHoldList.Data[Item]:
        return self._data

    @setdoc.basic
    def __fset__(self: Self, data: FrozenHoldList.Data[Item], /) -> None:
        self._data: FrozenHoldList.Data[Item] = data

    @setdoc.basic
    def __init__(self: Self, data: FrozenHoldList.Init[Item] = (), /) -> None:
        self.__fset__(tuple(data))
