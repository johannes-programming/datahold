__all__: list[str] = ["FrozenDataList"]

from abc import abstractmethod
from typing import Protocol, Self, TypeVar

import setdoc

from ..base.BaseDataList import BaseDataList
from .FrozenDataSequence import FrozenDataSequence

Item = TypeVar("Item", covariant=True)


class FrozenDataList(BaseDataList[Item], FrozenDataSequence[Item]):
    """Act as base class for frozen list-like implementation which only needs overriding of __data__ and of __init__ to work immediately."""

    __slots__ = ()

    @setdoc.basic
    class Data[DataItem](
        BaseDataList.Data[DataItem],
        FrozenDataSequence.Data[DataItem],
        Protocol[DataItem],
    ): ...

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> Data[Item]: ...
