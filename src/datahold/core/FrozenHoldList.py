import collections
from typing import *

import setdoc

from datahold.core.FrozenDataList import FrozenDataList
from datahold.core.FrozenHoldABC import FrozenHoldABC

__all__ = ["FrozenHoldList"]

Item = TypeVar("Item")


class FrozenHoldList(
    FrozenHoldABC,
    FrozenDataList[Item],
    collections.abc.MutableSequence[Item],
):

    __slots__ = ()

    data: tuple[Item, ...]

    @setdoc.basic
    def __init__(self: Self, data: Any, /) -> None:
        self._data = tuple(data)
