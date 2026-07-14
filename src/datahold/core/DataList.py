__all__:list[str] =[]
from ..base.BaseDataList import BaseDataList
from typing import TypeVar, Self, Any, SupportsIndex
import setdoc
from .DataCopyable import DataCopyable
from .DataSequence import DataSequence

Item = TypeVar("Item")

class DataSequence(
    BaseDataList[Item],
    DataSequence[Item],
    DataCopyable,
):
    __slots__=()
    @setdoc.basic
    def __imul__(self:Self, other: SupportsIndex, /) -> Self:
        self.__fset__(list(self.__fget__()) * other)
        return self
    
    @setdoc.basic
    def sort(self:Self, *, key:Any =None, reverse:bool=False) -> None:
        # Overload(
        #     def [_T, SupportsRichComparisonT <: _typeshed.SupportsDunderLT[Any] | _typeshed.SupportsDunderGT[Any]] (self: list[SupportsRichComparisonT], *, key: None =, reverse: bool =), 
        #     def [_T] (self: list[_T], *, key: def (_T) -> _typeshed.SupportsDunderLT[Any] | _typeshed.SupportsDunderGT[Any], reverse: bool =),
        # )
        data:list[Item]
        data=list(self)
        data.sort(key=key, reverse=reverse)
        self.__fset__(data)
        
