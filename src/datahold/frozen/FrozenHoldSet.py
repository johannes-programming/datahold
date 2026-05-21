from collections.abc import Iterable
from typing import Self, TypeVar

import setdoc

from ..base.BaseHoldSet import BaseHoldSet
from .FrozenDataSet import FrozenDataSet
from .FrozenHoldObject import FrozenHoldObject

__all__ = ["FrozenHoldSet"]

Item = TypeVar("Item")


class FrozenHoldSet(FrozenHoldObject, FrozenDataSet, BaseHoldSet[Item]):

    __slots__ = ()

    @setdoc.basic
    def __init__(self: Self, data: Iterable[Item], /) -> None:
        self._data = frozenset[Item](data)
