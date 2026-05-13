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

    @setdoc.basic
    def __ge__(self: Self, other: object) -> types.NotImplementedType | bool:
        if isinstance(other, BaseDataObject):
            return self.data.__ge__(other.data)
        else:
            return NotImplemented

    @setdoc.basic
    def __gt__(self: Self, other: object) -> types.NotImplementedType | bool:
        if isinstance(other, BaseDataObject):
            return self.data.__gt__(other.data)
        else:
            return NotImplemented

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Any, /) -> None: ...

    @setdoc.basic
    def __le__(self: Self, other: object) -> types.NotImplementedType | bool:
        if isinstance(other, BaseDataObject):
            return self.data.__le__(other.data)
        else:
            return NotImplemented

    @setdoc.basic
    def __lt__(self: Self, other: object) -> types.NotImplementedType | bool:
        if isinstance(other, BaseDataObject):
            return self.data.__lt__(other.data)
        else:
            return NotImplemented

    @setdoc.basic
    def __ne__(self: Self, other: object) -> types.NotImplementedType | bool:
        if isinstance(other, BaseDataObject):
            return self.data.__ne__(other.data)
        else:
            return NotImplemented

    @property
    @abstractmethod
    def data(self: Self) -> Any: ...
