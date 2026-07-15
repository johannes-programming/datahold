__all__: list[str] = ["FrozenDataCollection"]
from abc import abstractmethod
from collections.abc import Hashable
from typing import Self, Protocol

import setdoc

from ..base.BaseDataCollection import BaseDataCollection



class FrozenDataCollection[Key, Value](BaseDataCollection[Key, Value]):
    """Act as base class for frozen collection implementation which only needs overriding of __data__ to work immediately."""

    __slots__ = ()

    @setdoc.basic
    class Data[DataKey, DataValue](
        BaseDataCollection.Data[DataKey, DataValue], 
        Hashable, 
        Protocol[DataKey, DataValue],
    ): ...

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> Data[Key, Value]: ...

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.__data__())
