"""Provide BaseDataSequence."""

__all__: list[str] = ["BaseDataSequence"]

from abc import abstractmethod
from collections import abc
from typing import Protocol, Self, overload

import setdoc

from .._utils.Slice import Slice
from .BaseDataCollection import BaseDataCollection


class BaseDataSequence[Item](
    BaseDataCollection[Item],
    abc.Sequence[Item],
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
        ) -> abc.Sequence[DataItem]: ...
        @setdoc.basic
        def __getitem__(
            self: Self, key: int | Slice[int], /
        ) -> DataItem | abc.Sequence[DataItem]: ...

    @overload
    @setdoc.basic
    def __getitem__(self: Self, key: int, /) -> Item: ...
    @overload
    @setdoc.basic
    def __getitem__(self: Self, key: Slice[int], /) -> abc.Sequence[Item]: ...
    @setdoc.basic
    def __getitem__(
        self: Self, key: int | Slice[int], /
    ) -> Item | abc.Sequence[Item]:
        return self.__fget__()[key]

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> Data[Item]: ...
