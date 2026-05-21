from typing import *

from ..base.BaseHoldObject import BaseHoldObject
from .FrozenDataObject import FrozenDataObject

__all__ = ["FrozenHoldObject"]


class FrozenHoldObject(FrozenDataObject, BaseHoldObject):

    _data: Hashable
    __slots__ = ()

    @property
    def data(self: Self) -> Hashable:
        return self._data
