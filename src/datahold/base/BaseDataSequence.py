from __future__ import annotations

__all__: list[str] = ["BaseDataSequence"]
from abc import abstractmethod
from collections.abc import Sequence
from typing import Optional, Protocol, Self, overload, SupportsIndex

import setdoc

from .BaseDataCollection import BaseDataCollection

type Slice[SliceItem] = slice[Optional[SliceItem], Optional[SliceItem], Optional[SliceItem]]
type Key[KeyItem] = KeyItem | Slice[KeyItem]


class BaseDataSequence[Item](
    BaseDataCollection[Item],
    Sequence[Item],
):
    """Act as base class for sequence implementation which only needs overriding of __data__ and __init__ to work immediately."""

    __slots__ = ()

    @setdoc.basic
    class Data[DataItem](
        BaseDataCollection.Data[DataItem], Protocol[DataItem]
    ):

        @overload
        @setdoc.basic
        def __getitem__(self: Self, key: int, /) -> DataItem: ...

        @overload
        @setdoc.basic
        def __getitem__(self: Self, key: Slice[int], /) -> Sequence[DataItem]: ...

        def __getitem__(
            self: Self, key: Key[int], /
        ) -> DataItem | Sequence[DataItem]: ...

    type Init[InitItem] = Sequence[InitItem]

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> Data[Item]: ...

    @overload
    @setdoc.basic
    def __getitem__(self: Self, key: int) -> Item: ...

    @overload
    @setdoc.basic
    def __getitem__(self: Self, key: Slice[int]) -> Sequence[Item]: ...

    @setdoc.basic
    def __getitem__(self: Self, key: Key[int]) -> Item | Sequence[Item]:
        return self.__data__()[key]
        

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Sequence[Item], /) -> None: ...
