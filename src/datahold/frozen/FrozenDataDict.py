__all__: list[str] = ["FrozenDataDict"]
from abc import abstractmethod
from typing import Self

import setdoc

from ..base.BaseDataDict import BaseDataDict
from .FrozenDataMapping import FrozenDataMapping



class FrozenDataDict[Key, Value](
    BaseDataDict[Key, Value],
    FrozenDataMapping[Key, Value],
):
    __slots__ = ()

    class Data[DataKey, DataValue](
        BaseDataDict.Data[DataKey, DataValue],
        FrozenDataMapping.Data[DataKey, DataValue],
    ): ...

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> Data[Key, Value]: ...
