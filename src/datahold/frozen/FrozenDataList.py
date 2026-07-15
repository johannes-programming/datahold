__all__: list[str] = ["FrozenDataList"]

from abc import abstractmethod
from typing import Protocol, Self, TypeVar

import setdoc

from ..base.BaseDataList import BaseDataList
from .FrozenDataSequence import FrozenDataSequence

Item = TypeVar("Item", covariant=True)


class FrozenDataList(BaseDataList[Item], FrozenDataSequence[Item]):
    __slots__ = ()

    class Data(
        BaseDataList.Data[Item],
        FrozenDataSequence.Data[Item],
        Protocol[Item],
    ): ...

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> Data[Item]: ...
