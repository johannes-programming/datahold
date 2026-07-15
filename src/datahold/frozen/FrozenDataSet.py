__all__: list[str] = ["FrozenDataSet"]

from abc import abstractmethod
from typing import Protocol, Self

import setdoc

from ..base.BaseDataSet import BaseDataSet
from .FrozenDataAbstractSet import FrozenDataAbstractSet


class FrozenDataSet[Item](BaseDataSet[Item], FrozenDataAbstractSet[Item]):
    __slots__ = ()

    class Data(
        BaseDataSet.Data[Item],
        FrozenDataAbstractSet.Data[Item],
        Protocol[Item],
    ): ...

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> Data[Item]: ...
