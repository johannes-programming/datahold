__all__: list[str] = ["DataDict"]
from abc import abstractmethod
from typing import Protocol, Self

import setdoc

from ..base.BaseDataDict import BaseDataDict
from .DataMapping import DataMapping
from .DataCopyable import DataCopyable


class DataDict[Key, Value](
    BaseDataDict[Key, Value],
    DataMapping[Key, Value],
    DataCopyable[Key | str],
):
    """Act as base class for dict-like implementation which only needs overriding of __data__ and of __init__ to work immediately."""

    __slots__ = ()

    class Data[DataKey, DataValue](
        BaseDataDict.Data[DataKey, DataValue], 
        DataMapping.Data[DataKey, DataValue],
        DataCopyable.Data[DataKey],
        Protocol[DataKey, DataValue],
    ):
        @setdoc.basic
        def __ior__(
            self: Self,
            other: BaseDataDict.Init[DataKey, DataValue],
            /,
        ) -> object: ...

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> Data[Key, Value]: ...

    @setdoc.basic
    def __ior__(
        self: Self, 
        other: BaseDataDict.Init[Key, Value], 
        /,
    ) -> Self:
        self.__data__().__ior__(other)
        return self
