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
    """Act as base class for (abstract) frozen set implementation which only needs overriding of __data__ to work immediately."""

    __slots__ = ()

    @setdoc.basic
    class Data[DataItem](
        BaseDataAbstractSet.Data[DataItem],
        FrozenDataCollection.Data[DataItem],
        Protocol[DataItem],
    ): ...

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> Data[Item]: ...
