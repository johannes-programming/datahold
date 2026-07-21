"""Provide BaseDataList."""

from __future__ import annotations

__all__: list[str] = ["BaseDataList"]

from abc import abstractmethod
from collections.abc import Iterable
from typing import Self, SupportsIndex, overload, Any

import setdoc

from .BaseDataSequence import BaseDataSequence, Slice


class BaseDataList[Item](BaseDataSequence[Item]):
    __slots__ = ()

    type Data[DataItem] = tuple[DataItem, ...]
    type Init[InitItem] = Iterable[InitItem]

    @setdoc.basic
    def __add__(self: Self, other: BaseDataList[Item], /) -> Self:
        # list.__add__ reveals Overload(
        #     def [_T] (list[_T], list[_T]) -> list[_T], 
        #     def [_T, _S] (list[_T], list[_S]) -> list[_S | _T],
        # ) 
        # tuple.__add__ reveals Overload(
        #     def [_T_co] (tuple[_T_co, ...], tuple[_T_co, ...]) -> tuple[_T_co, ...], 
        #     def [_T_co, _T] (tuple[_T_co, ...], tuple[_T, ...]) -> tuple[_T_co | _T, ...],
        # )
        return type(self)(self.data + other.data)
    
    @setdoc.basic
    def __eq__(self:Self, other: object, /)-> bool:
        if isinstance(other, BaseDataList):
            return self.data == other.data
        else:
            return False
    
    @setdoc.basic
    def __ge__(self:Self, other: BaseDataList[Any], /) -> bool:
        return self.data >= other.data
    
    @setdoc.basic
    def __gt__(self:Self, other: BaseDataList[Any], /) -> bool:
        return self.data > other.data
    

    @overload
    @setdoc.basic
    def __getitem__(self: Self, index: SupportsIndex, /) -> Item: ...

    @overload
    @setdoc.basic
    def __getitem__(self: Self, index: Slice[SupportsIndex], /) -> Self: ...

    @setdoc.basic
    def __getitem__(
        self: Self, index: SupportsIndex | Slice[SupportsIndex], /
    ) -> Item | Self:
        if isinstance(index, SupportsIndex):
            return self.data[index]
        else:
            return type(self)(self.data[index])

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Init[Item] = (), /) -> None: ...

    @setdoc.basic
    def __le__(self:Self, other: BaseDataList[Any], /) -> bool:
        return self.data <= other.data
    
    @setdoc.basic
    def __lt__(self:Self, other: BaseDataList[Any], /) -> bool:
        return self.data < other.data
    
    @setdoc.basic
    def __mul__(self: Self, other: SupportsIndex, /) -> Self:
        return type(self)(self.data * other)

    @setdoc.basic
    def __repr__(self: Self, /) -> str:
        return f"{type(self).__name__}({list(self.data)!r})"
    
    __rmul__ = __mul__

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data[Item]: ...
