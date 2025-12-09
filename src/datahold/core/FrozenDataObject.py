
from typing import *
import collections
from .BaseDataObject import BaseDataObject

import setdoc

__all__ = ["FrozenDataObject"]


class FrozenDataObject(BaseDataObject, collections.abc.Hashable):
    __slots__ = ()

    data: Any

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.data)
        