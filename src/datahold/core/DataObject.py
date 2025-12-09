
from typing import *
from .BaseDataObject import BaseDataObject
import setdoc

__all__ = ["DataObject"]


class DataObject(BaseDataObject):
    data: Any
    __slots__ = ()


    __hash__ = None

    @setdoc.basic
    def copy(self:Self) -> Self:
        return type(self)(self)
