__all__: list[str] = ["FrozenDataSet"]

from abc import abstractmethod
from typing import Protocol, Self

import setdoc

from ..base.BaseDataSet import BaseDataSet
from .FrozenDataAbstractSet import FrozenDataAbstractSet


class FrozenDataSet[Item](BaseDataSet[Item], FrozenDataAbstractSet[Item]):
    """Act as base class for frozen set-like implementation which only needs overriding of __data__ and of __init__ to work immediately."""

    __slots__ = ()

    @setdoc.basic
    class Data(
        BaseDataSet.Data[Item],
        FrozenDataAbstractSet.Data[Item],
        Protocol[Item],
    ): ...

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> Data[Item]: ...
