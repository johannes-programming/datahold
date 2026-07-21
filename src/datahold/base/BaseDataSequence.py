"""Provide BaseDataSequence."""

__all__ = ["BaseDataSequence"]


from abc import abstractmethod
from collections.abc import Sequence
from typing import Protocol, Self, overload

import setdoc

from .._utils.Slice import Slice
from .BaseDataCollection import BaseDataCollection


class BaseDataSequence[Item](
    BaseDataCollection[Item],
    Sequence[Item],
):
    """Provide an easy abc for a custom sequence."""

    __slots__ = ()

    @setdoc.basic
    class Data[DataItem](
        BaseDataCollection.Data[DataItem],
        Protocol,
    ):
        """Provide sequence data protocol."""

        @overload
        @setdoc.basic
        def __getitem__(self: Self, key: int, /) -> DataItem: ...
        @overload
        @setdoc.basic
        def __getitem__(
            self: Self, key: Slice[int], /
        ) -> Sequence[DataItem]: ...
        @setdoc.basic
        def __getitem__(
            self: Self, key: int | Slice[int], /
        ) -> DataItem | Sequence[DataItem]: ...

    @overload
    @setdoc.basic
    def __getitem__(self: Self, key: int, /) -> Item: ...
    @overload
    @setdoc.basic
    def __getitem__(self: Self, key: Slice[int], /) -> Sequence[Item]: ...
    @setdoc.basic
    def __getitem__(
        self: Self, key: int | Slice[int], /
    ) -> Item | Sequence[Item]:
        return self.data[key]

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data[Item]: ...
