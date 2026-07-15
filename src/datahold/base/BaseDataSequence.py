from __future__ import annotations

__all__: list[str] = ["BaseDataSequence"]
from abc import abstractmethod
from collections.abc import Sequence
from typing import Optional, Protocol, Self, overload, SupportsIndex

import operator
import setdoc

from .BaseDataCollection import BaseDataCollection

type Slice[SliceItem] = slice[Optional[SliceItem], Optional[SliceItem], Optional[SliceItem]]

def optionalIndex(index:Optional[SupportsIndex]) -> Optional[int]:
    if index is None:
        return None
    else:
        return operator.index(index)
def sequenceSlice(index:Slice[SupportsIndex]) -> Slice[int]:
    return slice(
        optionalIndex(index.start),
        optionalIndex(index.stop),
        optionalIndex(index.step),
    )
    

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
            self: Self, key: int | Slice[int], /
        ) -> DataItem | Sequence[DataItem]: ...

    type Init[InitItem] = Sequence[InitItem]

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> Data[Item]: ...

    @overload
    @setdoc.basic
    def __getitem__(self: Self, key: SupportsIndex) -> Item: ...

    @overload
    @setdoc.basic
    def __getitem__(self: Self, key: Slice[SupportsIndex]) -> Self: ...

    @setdoc.basic
    def __getitem__(self: Self, key: SupportsIndex | Slice[SupportsIndex]) -> Item | Self:
        # Sequence.__getitem__ reveals "Overload(def [_T_co] (typing.Sequence[_T_co], int) -> _T_co, def [_T_co] (typing.Sequence[_T_co], slice[int | None, int | None, int | None]) -> typing.Sequence[_T_co])"
        # we are forced to assume a constructor signature
        # the subtype of BaseDataSequence might be immutable
        if isinstance(key, SupportsIndex):
            return self.__data__()[optionalIndex(key)]
        return type(self)(self.__data__()[sequenceSlice(key)])
        

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Sequence[Item], /) -> None: ...
