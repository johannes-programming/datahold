__all__: list[str] = ["FrozenDataCollection"]
from abc import abstractmethod
from collections.abc import Hashable
from typing import Self, TypeVar

import setdoc

from ..base.BaseDataCollection import BaseDataCollection

DataKey = TypeVar("DataKey", covariant=True)
DataValue = TypeVar("DataValue", covariant=True)
Key = TypeVar("Key", covariant=True)
Value = TypeVar("Value", covariant=True)


class FrozenDataCollection(BaseDataCollection[Key, Value]):
    __slots__ = ()

    class Data(BaseDataCollection.Data[DataKey, DataValue], Hashable): ...

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> Data[Key, Value]: ...

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.__data__())
