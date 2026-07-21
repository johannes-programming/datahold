"""Provide BaseDataSequence."""

__all__ = ["BaseDataSequence"]


from collections.abc import Sequence
from typing import Protocol, Self, Optional, overload

import setdoc

from abc import abstractmethod

from .BaseDataCollection import BaseDataCollection

type Slice[Index] = slice[Optional[Index], Optional[Index], Optional[Index]]


class BaseDataSequence[Item](
    BaseDataCollection[Item], 
    Sequence[Item],
):
    __slots__ = ()

    class Data[DataItem](
        Protocol[DataItem],
    ):
        """Provide sequence data protocol."""
        @overload
        @setdoc.basic
        def __getitem__(self:Self, key: int, /) -> DataItem:
            ...
        @overload
        @setdoc.basic
        def __getitem__(self:Self, key: Slice[int], /) -> Sequence[DataItem]:
            ...
        @setdoc.basic
        def __getitem__(self:Self, key: int | Slice[int], /) -> DataItem | Sequence[DataItem]:
            ...

    @overload
    @setdoc.basic
    def __getitem__(self:Self, key: int, /) -> Item:
        ...
    @overload
    @setdoc.basic
    def __getitem__(self:Self, key: Slice[int], /) -> Sequence[Item]:
        ...
    @setdoc.basic
    def __getitem__(self:Self, key: int | Slice[int], /) -> Item | Sequence[Item]:
        return self.data[key]

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data[Item]: ...
