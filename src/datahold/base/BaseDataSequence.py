from __future__ import annotations

__all__: list[str] = ["BaseDataSequence"]
from abc import abstractmethod
from collections.abc import Sequence
from typing import Protocol, Self, overload

import setdoc

from .BaseDataCollection import BaseDataCollection



class BaseDataSequence[Item](
    BaseDataCollection[Item],
    Sequence[Item],
):
    """Act as base class for sequence implementation which only needs overriding of __data__ and __init__ to work immediately."""

    __slots__ = ()

    @setdoc.basic
    class Data[DataItem](BaseDataCollection.Data[DataItem], Protocol[DataItem]):

        @overload
        @setdoc.basic
        def __getitem__(self: Self, index: int, /) -> DataItem: ...

        @overload
        @setdoc.basic
        def __getitem__(self: Self, index: slice, /) -> Sequence[DataItem]: ...

        def __getitem__(
            self: Self, index: int | slice, /
        ) -> DataItem | Sequence[DataItem]: ...
    
    type Init[InitItem] = Sequence[InitItem]

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> Data[Item]: ...

    @overload
    @setdoc.basic
    def __getitem__(self: Self, index: int) -> Item: ...

    @overload
    @setdoc.basic
    def __getitem__(self: Self, index: slice) -> Self: ...

    @setdoc.basic
    def __getitem__(self: Self, index: int | slice) -> Item | Self:
        # Sequence.__getitem__ reveals "Overload(def [_T_co] (typing.Sequence[_T_co], int) -> _T_co, def [_T_co] (typing.Sequence[_T_co], slice[int | None, int | None, int | None]) -> typing.Sequence[_T_co])"
        if isinstance(index, slice):
            # index cannot be an int now because subclassing slice is impossible
            # we are forced to assume a constructor signature
            # the subtype of BaseDataSequence might be immutable
            return type(self)(self.__fget__()[index])
        else:
            return self.__fget__()[index]

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Sequence[Item], /) -> None: ...
