import collections
from typing import *

import setdoc

from datahold.core.FrozenDataList import FrozenDataList
from datahold.core.FrozenHoldBase import FrozenHoldBase

__all__ = ["FrozenHoldList"]

Item = TypeVar("Item")


class FrozenHoldList(
    FrozenHoldBase,
    FrozenDataList[Item],
):

    __slots__ = ()

    data: tuple[Item, ...]

    @setdoc.basic
    def __init__(self: Self, data: Any, /) -> None:
        self._data = tuple(data)
