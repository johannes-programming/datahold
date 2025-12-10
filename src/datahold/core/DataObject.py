from typing import *

import setdoc

from .BaseDataObject import BaseDataObject

__all__ = ["DataObject"]


class DataObject(BaseDataObject):
    data: Any
    __slots__ = ()

    __hash__ = None

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self.data)
