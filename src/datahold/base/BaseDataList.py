from __future__ import annotations

__all__: list[str] = ["BaseDataList"]

from abc import abstractmethod
from collections.abc import Iterable
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

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> tuple[Item, ...]: ...

    @setdoc.basic
    def __init__(self: Self, data: Iterable[Item] = (), /) -> None:
        self.__fset__(tuple(data))

    @setdoc.basic
    def __mul__(self: Self, other: SupportsIndex, /) -> Self:
        return type(self)(self.data * other)

    __rmul__ = __mul__
