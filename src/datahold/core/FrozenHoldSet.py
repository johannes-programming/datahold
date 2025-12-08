import collections
from typing import *

import setdoc

from datahold.core.FrozenDataSet import FrozenDataSet
from datahold.core.FrozenHoldBase import FrozenHoldBase

__all__ = ["FrozenHoldSet"]

Item = TypeVar("Item")


class FrozenHoldSet(
    FrozenHoldBase,
    FrozenDataSet[Item],
):

    __slots__ = ()

    data: frozenset[Item]

    @setdoc.basic
    def __init__(self: Self, data: Any, /) -> None:
        self._data = frozenset(data)
