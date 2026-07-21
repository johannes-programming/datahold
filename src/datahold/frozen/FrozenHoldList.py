"""Provide FrozenHoldList."""

__all__: list[str] = ["FrozenHoldList"]

from collections.abc import Iterable
from typing import Self

import setdoc

from ..base.BaseHoldList import BaseHoldList
from .FrozenDataList import FrozenDataList
from .FrozenHoldCollection import FrozenHoldCollection


class FrozenHoldList[Item](
    FrozenDataList[Item],
    BaseHoldList[Item],
    FrozenHoldCollection[Item],
):

    __slots__ = ()

    @setdoc.basic
    def __init__(self: Self, data: Iterable[Item] = (), /) -> None:
        self._data: tuple[Item, ...] = tuple(data)

    @property
    @setdoc.basic
    def data(self: Self) -> tuple[Item, ...]:
        return self._data
