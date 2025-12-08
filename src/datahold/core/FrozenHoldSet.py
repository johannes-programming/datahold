import collections
from typing import *

import setdoc

from datahold.core.FrozenDataSet import FrozenDataSet
from datahold.core.FrozenHoldABC import FrozenHoldABC

__all__ = ["FrozenHoldSet"]

Item = TypeVar("Item")


class FrozenHoldSet(
    FrozenHoldABC,
    FrozenDataSet[Item],
    collections.abc.MutableSet[Item],
):

    __slots__ = ()

    data: frozenset[Item]

    @setdoc.basic
    def __init__(self: Self, data: Any, /) -> None:
        self._data = frozenset(data)
