from collections.abc import Iterable
from typing import Self, TypeVar

import setdoc

from ..base.BaseHoldList import BaseHoldList
from .FrozenDataList import FrozenDataList
from .FrozenHoldObject import FrozenHoldObject

__all__ = ["FrozenHoldList"]

Item = TypeVar("Item", covariant=True)


class FrozenHoldList(
    FrozenHoldObject, FrozenDataList[Item], BaseHoldList[Item]
):

    __slots__ = ()

    @setdoc.basic
    def __init__(self: Self, data: Iterable[Item], /) -> None:
        self._data = tuple(data)
