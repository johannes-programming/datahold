"""Provide BaseDataList."""

from __future__ import annotations

__all__: list[str] = ["BaseDataList"]

from abc import abstractmethod
from collections.abc import Iterable
from types import NotImplementedType
from typing import Self, SupportsIndex, overload

import setdoc

from .._utils.Slice import Slice
from .BaseDataSequence import BaseDataSequence


class BaseDataList[Item](BaseDataSequence[Item]):
    """Provide an easy abc for custom list-like."""

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
        if isinstance(other, BaseDataList):
            return type(self)(self.__fget__() + other.__fget__())
        else:
            return NotImplemented

    @setdoc.basic
    def __eq__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, BaseDataList):
            return self.__fget__() == other.__fget__()
        else:
            return NotImplemented

    @setdoc.basic
    def __ge__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, BaseDataList):
            return self.__fget__() >= other.__fget__()
        else:
            return NotImplemented

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
            return self.__fget__()[index]
        else:
            return type(self)(self.__fget__()[index])

    @setdoc.basic
    def __gt__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, BaseDataList):
            return self.__fget__() > other.__fget__()
        else:
            return NotImplemented

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Init[Item] = (), /) -> None: ...

    @setdoc.basic
    def __le__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, BaseDataList):
            return self.__fget__() <= other.__fget__()
        else:
            return NotImplemented

    @setdoc.basic
    def __lt__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, BaseDataList):
            return self.__fget__() < other.__fget__()
        else:
            return NotImplemented

    @setdoc.basic
    def __mul__(self: Self, other: SupportsIndex, /) -> Self:
        return type(self)(self.__fget__() * other)

    @setdoc.basic
    def __repr__(self: Self, /) -> str:
        return f"{type(self).__name__}({list(self.__fget__())!r})"

    __rmul__ = __mul__

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> Data[Item]: ...
