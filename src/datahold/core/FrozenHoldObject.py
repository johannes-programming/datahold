from typing import *

import setdoc

from .BaseHoldObject import BaseHoldObject
from .FrozenDataObject import FrozenDataObject

__all__ = ["FrozenHoldObject"]


class FrozenHoldObject(FrozenDataObject, BaseHoldObject):
    __slots__ = ()

    @property
    @setdoc.basic
    def data(self: Self) -> Any:
        return self._data
