from collections.abc import Hashable
from typing import Self

import setdoc

from ..base.BaseDataObject import BaseDataObject

__all__ = ["FrozenDataObject"]


class FrozenDataObject(BaseDataObject, Hashable):

    __slots__ = ()

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.data)
