__all__: list[str] = ["FrozenDataMapping"]
from abc import abstractmethod
from typing import Protocol, Self

import setdoc

from ..base.BaseDataMapping import BaseDataMapping
from ..frozen.FrozenDataCollection import FrozenDataCollection


class FrozenDataMapping[Key, Value](
    BaseDataMapping[Key, Value],
    FrozenDataCollection[Key, Value],
):
    __slots__ = ()

    class Data[DataKey, DataValue](
        BaseDataMapping.Data[DataKey, DataValue],
        FrozenDataCollection.Data[DataKey, DataValue],
        Protocol[DataKey, DataValue],
    ): ...

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> Data[Key, Value]: ...
