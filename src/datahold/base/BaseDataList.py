from __future__ import annotations

__all__: list[str] = ["BaseDataList"]

from typing import TypeVar, Self, SupportsIndex
from .BaseDataSequence import BaseDataSequence
from .BaseDataFgettable import BaseDataFgettable
import setdoc

Item = TypeVar("Item", covariant=True)
Fget = tuple[Item, ...]


class BaseDataList(BaseDataSequence[Item]):

    __slots__ = ()

    Data = Fget

    @setdoc.basic
    def __add__(self:Self, other: BaseDataList[Item], /) -> Self:
        return type(self)(self.data + tuple(other))

    __fget__ = BaseDataFgettable[frozenset[Item]].__fget__

    @setdoc.basic
    def __mul__(self:Self, other: SupportsIndex, /) -> Self:
        return type(self)(self.data * other)
    
    __rmul__ = __mul__