__all__: list[str] = ["DataList"]
from typing import Any, Self, SupportsIndex, TypeVar

import setdoc

from ..base.BaseDataList import BaseDataList
from .DataSequence import DataSequence

Item = TypeVar("Item")


class DataList(
    BaseDataList[Item],
    DataSequence[Item],
):
    """Act as base class for list-like implementation which only has to override __fget__ and __fset__ to work immediately."""

    __slots__ = ()

    @setdoc.basic
    def __imul__(self: Self, other: SupportsIndex, /) -> Self:
        self.__fset__(list(self.__fget__()) * other)
        return self

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self)

    @setdoc.basic
    def sort(self: Self, *, key: Any = None, reverse: bool = False) -> None:
        # Overload(
        #     def [_T, SupportsRichComparisonT <: _typeshed.SupportsDunderLT[Any] | _typeshed.SupportsDunderGT[Any]] (self: list[SupportsRichComparisonT], *, key: None =, reverse: bool =),
        #     def [_T] (self: list[_T], *, key: def (_T) -> _typeshed.SupportsDunderLT[Any] | _typeshed.SupportsDunderGT[Any], reverse: bool =),
        # )
        data: list[Item]
        data = list(self)
        data.sort(key=key, reverse=reverse)
        self.__fset__(data)
