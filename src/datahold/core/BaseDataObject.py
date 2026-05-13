import types
from abc import ABCMeta, abstractmethod
from typing import *

import setdoc

__all__ = ["BaseDataObject"]


class BaseDataObject(metaclass=ABCMeta):

    __slots__ = ()

    @setdoc.basic
    def __eq__(self: Self, other: object) -> types.NotImplementedType | bool:
        if isinstance(other, BaseDataObject):
            return self.data.__eq__(other.data)
        else:
            return NotImplemented

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Any: ...
