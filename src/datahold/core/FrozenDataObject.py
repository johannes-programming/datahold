import collections
from typing import *

import setdoc

from .BaseDataObject import BaseDataObject

__all__ = ["FrozenDataObject"]


class FrozenDataObject(BaseDataObject, collections.abc.Hashable):
    __slots__ = ()

    data: Any

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.data)
