__all__: list[str] = ["DataList"]
from typing import Any, Self, SupportsIndex, Protocol

import setdoc

from ..base.BaseDataList import BaseDataList
from .DataSequence import DataSequence
from .DataCopyable import DataCopyable


class DataList[Item](
    BaseDataList[Item],
    DataSequence[Item],
    DataCopyable[Item],
):
    """Act as base class for list-like implementation which only needs overriding of __data__ and of __init__ to work immediately."""

    __slots__ = ()

    @setdoc.basic
    class Data[DataItem](
        BaseDataList.Data[DataItem],
        DataSequence.Data[DataItem],
        DataCopyable.Data[DataItem],
        Protocol[DataItem],
    ):
        @setdoc.basic
        def __imul__(self:Self, other:SupportsIndex, /) -> object:
            ...
        @setdoc.basic
        def sort(self: Self, *, key: Any = None, reverse: bool = False) -> object:
            ...
    
    @setdoc.basic
    def __data__(self:Self) -> Data[Item]:
        ...

    @setdoc.basic
    def __imul__(self: Self, other: SupportsIndex, /) -> Self:
        self.__fset__(list(self.__fget__()) * other)
        return self


    @setdoc.basic
    def sort(self: Self, *, key: Any = None, reverse: bool = False) -> None:
        # Overload(
        #     def [_T, SupportsRichComparisonT <: _typeshed.SupportsDunderLT[Any] | _typeshed.SupportsDunderGT[Any]] (self: list[SupportsRichComparisonT], *, key: None =, reverse: bool =),
        #     def [_T] (self: list[_T], *, key: def (_T) -> _typeshed.SupportsDunderLT[Any] | _typeshed.SupportsDunderGT[Any], reverse: bool =),
        # )
        self.__data__().sort(key=key, reverse=reverse)

