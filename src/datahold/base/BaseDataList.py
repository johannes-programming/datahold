from __future__ import annotations

__all__: list[str] = ["BaseDataList"]

from abc import abstractmethod
from collections.abc import Iterable
from types import NotImplementedType
from typing import Self, SupportsIndex, TypeVar

import setdoc

from .BaseDataSequence import BaseDataSequence

Item = TypeVar("Item", covariant=True)
Fget = tuple[Item, ...]


class BaseDataList(BaseDataSequence[Item]):
    """Act as base class for list-like implementation """ """which only has to override __fget__ and __fset__ to work immediately."""

    __slots__ = ()

    Data = Fget

    @setdoc.basic
    def __add__(self: Self, other: BaseDataList[Item], /) -> Self:
        return type(self)(self.data + tuple(other))

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

    @setdoc.basic
    def __gt__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, BaseDataList):
            return self.__fget__() > other.__fget__()
        else:
            return NotImplemented

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> tuple[Item, ...]: ...

    @setdoc.basic
    def __init__(self: Self, data: Iterable[Item] = (), /) -> None:
        self.__fset__(tuple(data))

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
        return type(self)(self.data * other)

    __rmul__ = __mul__
