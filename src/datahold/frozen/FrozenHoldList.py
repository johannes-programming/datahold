"""Provide FrozenHoldList."""

__all__: list[str] = ["FrozenHoldList"]

from collections.abc import Iterable
from typing import Self, TypeVar

import setdoc

from ..base.BaseHoldList import BaseHoldList
from .FrozenDataList import FrozenDataList
from .FrozenHoldObject import FrozenHoldObject

Item = TypeVar("Item", covariant=True)


class FrozenHoldList(  # type: ignore[misc]
    FrozenHoldObject, FrozenDataList[Item], BaseHoldList[Item]
):

    __slots__ = ()

    @setdoc.basic
    def __init__(self: Self, data: Iterable[Item], /) -> None:
        self._data = tuple(data)
