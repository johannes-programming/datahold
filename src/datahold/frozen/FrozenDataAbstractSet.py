__all__: list[str] = ["FrozenDataAbstractSet"]

from abc import abstractmethod
from typing import Protocol, Self

import setdoc

from ..base.BaseDataAbstractSet import BaseDataAbstractSet
from .FrozenDataCollection import FrozenDataCollection


class FrozenDataAbstractSet[Item](
    BaseDataAbstractSet[Item], 
    FrozenDataCollection[Item],
):
    __slots__ = ()

    class Data(
        BaseDataAbstractSet.Data[Item],
        FrozenDataCollection.Data[Item],
        Protocol[Item],
    ): ...

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> Data[Item]: ...
