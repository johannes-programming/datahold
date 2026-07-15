__all__: list[str] = ["FrozenDataSequence"]

from abc import abstractmethod
from typing import Protocol, Self

import setdoc

from ..base.BaseDataSequence import BaseDataSequence
from .FrozenDataCollection import FrozenDataCollection


class FrozenDataSequence[Item](
    BaseDataSequence[Item], 
    FrozenDataCollection[Item],
):
    __slots__ = ()

    class Data(
        BaseDataSequence.Data[Item],
        FrozenDataCollection.Data[Item],
        Protocol[Item],
    ): ...

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> Data[Item]: ...
