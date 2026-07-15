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
    """Act as base class for frozen dict-like implementation which only needs overriding of __data__ and of __init__ to work immediately."""

    __slots__ = ()

    @setdoc.basic
    class Data[DataKey, DataValue](
        BaseDataDict.Data[DataKey, DataValue],
        FrozenDataMapping.Data[DataKey, DataValue],
    ): ...

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> Data[Key, Value]: ...
