from __future__ import annotations

__all__: list[str] = ["BaseDataList"]

from abc import abstractmethod
from collections.abc import Iterable
from types import NotImplementedType
from typing import Protocol, Self, SupportsIndex, TypeVar

import setdoc

from .BaseDataSequence import BaseDataSequence

DataItem = TypeVar("DataItem", covariant=True)
Item = TypeVar("Item", covariant=True)


class BaseDataList(BaseDataSequence[Item]):
    """Act as base class for list-like implementation which only needs overriding of __data__ and of __init__ to work immediately."""

    __slots__ = ()

    @setdoc.basic
    class Data(BaseDataSequence.Data[DataItem], Protocol[DataItem]):
        @setdoc.basic
        def __add__(
            self: Self, other: BaseDataList.Data[DataItem], /
        ) -> Iterable[DataItem]: ...
        @setdoc.basic
        def __eq__(
            self: Self, other: BaseDataList.Data[DataItem], /
        ) -> NotImplementedType | bool: ...
        @setdoc.basic
        def __ge__(
            self: Self, other: BaseDataList.Data[DataItem], /
        ) -> NotImplementedType | bool: ...
        @setdoc.basic
        def __gt__(
            self: Self, other: BaseDataList.Data[DataItem], /
        ) -> NotImplementedType | bool: ...
        @setdoc.basic
        def __le__(
            self: Self, other: BaseDataList.Data[DataItem], /
        ) -> NotImplementedType | bool: ...
        @setdoc.basic
        def __lt__(
            self: Self, other: BaseDataList.Data[DataItem], /
        ) -> NotImplementedType | bool: ...
        @setdoc.basic
        def __mul__(
            self: Self, other: SupportsIndex, /
        ) -> Iterable[DataItem]: ...
        @setdoc.basic
        def __rmul__(
            self: Self, other: SupportsIndex, /
        ) -> Iterable[DataItem]: ...
    
    type Init[InitItem] = Iterable[InitItem]

    @setdoc.basic
    def __add__(self: Self, other: BaseDataList[Item], /) -> Self:
        return type(self)(self.__data__().__add__(other.__data__()))

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> Data[Item]: ...

    @setdoc.basic
    def __eq__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, BaseDataList):
            return self.__data__().__eq__(other.__data__())
        else:
            return NotImplemented

    @setdoc.basic
    def __ge__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, BaseDataList):
            return self.__data__().__ge__(other.__data__())
        else:
            return NotImplemented

    @setdoc.basic
    def __gt__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, BaseDataList):
            return self.__data__().__gt__(other.__data__())
        else:
            return NotImplemented

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Iterable[Item] = (), /) -> None: ...

    @setdoc.basic
    def __le__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, BaseDataList):
            return self.__data__().__le__(other.__data__())
        else:
            return NotImplemented

    @setdoc.basic
    def __lt__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, BaseDataList):
            return self.__data__().__lt__(other.__data__())
        else:
            return NotImplemented

    @setdoc.basic
    def __mul__(self: Self, other: SupportsIndex, /) -> Self:
        return type(self)(self.__data__().__mul__(other))

    @setdoc.basic
    def __rmul__(self: Self, other: SupportsIndex, /) -> Self:
        return type(self)(self.__data__().__rmul__(other))
