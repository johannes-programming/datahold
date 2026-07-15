from __future__ import annotations
__all__:list[str]=["DataCopyable"]
from ..base.BaseDataCollection import BaseDataCollection
from typing import Protocol, Self
import setdoc
from abc import abstractmethod


class DataCopyable[Item](BaseDataCollection[Item]):
    """Act as base class for copyable implementation which only needs overriding of __data__ and of __init__ to work immediately."""

    __slots__ = ()
    
    @setdoc.basic
    class Data[DataItem](BaseDataCollection.Data[DataItem], Protocol[DataItem]):
        @setdoc.basic
        def copy(self:Self) -> DataCopyable.Data[DataItem]:
            ...
    
    type Init[InitItem] = BaseDataCollection.Data[InitItem]

    @abstractmethod
    @setdoc.basic
    def __data__(self:Self) -> Data[Item]:
        ...

    @abstractmethod
    @setdoc.basic
    def __init__(self:Self, data:Data[Item], /) -> None:
        ...
    
    @setdoc.basic
    def copy(self:Self) -> Self:
        return type(self)(self.__data__().copy())

