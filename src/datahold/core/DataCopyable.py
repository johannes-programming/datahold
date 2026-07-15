from __future__ import annotations
__all__:list[str]=["DataCopyable"]
from ..base.BaseDataCollection import BaseDataCollection
from typing import Protocol, Self
import setdoc
from abc import abstractmethod


class DataCopyable[Item](BaseDataCollection[Item]):
    __slots__ = ()
    class Data[DataItem](BaseDataCollection.Data[DataItem], Protocol[DataItem]):
        @setdoc.basic
        def copy(self:Self) -> DataCopyable.Data[DataItem]:
            ...
    
    Init = Data

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

