from typing import *

import setdoc

from .BaseHoldSet import BaseHoldSet
from .FrozenDataSet import FrozenDataSet
from .FrozenHoldObject import FrozenHoldObject

__all__ = ["FrozenHoldSet"]

Item = TypeVar("Item", covariant=True)


class FrozenHoldSet(FrozenHoldObject, FrozenDataSet, BaseHoldSet[Item]):
    data: frozenset[Item]
    __slots__ = ()

    @setdoc.basic
    def __init__(self: Self, data: Iterable[Item], /) -> None:
        self._data = frozenset[Item](data)
