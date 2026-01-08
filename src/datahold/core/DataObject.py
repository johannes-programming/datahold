from typing import *

import setdoc

from .BaseDataObject import BaseDataObject

__all__ = ["DataObject"]


class DataObject(BaseDataObject):
    data: Any

    __hash__ = None
    __slots__ = ()

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self.data)
