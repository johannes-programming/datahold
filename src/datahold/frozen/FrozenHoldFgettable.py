
from typing import TypeVar, Self
import setdoc
from .FrozenDataFgettable import FrozenDataFgettable

Data = TypeVar("Data", covariant=True)
class FrozenHoldFgettable(FrozenDataFgettable[Data]):
    __slots__ = ("_data",)
    @setdoc.basic
    def __fget__(self:Self) -> Data:
        return self._data