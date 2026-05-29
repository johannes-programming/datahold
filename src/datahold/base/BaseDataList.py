from __future__ import annotations

import sys
from abc import abstractmethod
from collections.abc import Hashable, Iterable, Iterator, Sequence
from typing import Any, Self, SupportsIndex, TypeVar, cast, overload

import setdoc

from .BaseDataCollection import BaseDataCollection

__all__ = ["BaseDataList"]

Item = TypeVar("Item", covariant=True)
Item_ = TypeVar("Item_")


class BaseDataList(BaseDataCollection[Item], Sequence[Item]):
    __slots__ = ()

    @setdoc.basic
    def __add__(self: Self, other: Iterable[Item], /) -> Self:
        return type(self)(self.data + tuple(other))

    @setdoc.basic
    def __contains__(self: Self, other: object) -> bool:
        return other in self.data

    @overload
    @setdoc.basic
    def __getitem__(self: Self, index: SupportsIndex, /) -> Item: ...

    @overload
    @setdoc.basic
    def __getitem__(self: Self, index: slice, /) -> Self: ...

    @setdoc.basic
    def __getitem__(
        self: Self, index: SupportsIndex | slice, /
    ) -> Item | Self:
        if isinstance(index, SupportsIndex):
            return self.data[index]
        else:
            return type(self)(self.data[index])

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Iterable[Item] = (), /) -> None: ...

    @setdoc.basic
    def __mul__(self: Self, other: SupportsIndex, /) -> Self:
        return type(self)(self.data * other)

    @setdoc.basic
    def __repr__(self: Self, /) -> str:
        return "%s(%r)" % (type(self).__name__, list(self.data))

    @setdoc.basic
    def __reversed__(self: Self, /) -> Iterator[Item]:
        return reversed(self.data)

    @setdoc.basic
    def __rmul__(self: Self, other: SupportsIndex, /) -> Self:
        return type(self)(other * self.data)

    @setdoc.setdoc(list.count.__doc__)
    def count(self: Self, value: Hashable, /) -> int:
        return self.data.count(cast(Any, value))

    @property
    @abstractmethod
    def data(self: Self) -> tuple[Item, ...]: ...

    @setdoc.setdoc(list.index.__doc__)
    def index(
        self: Self,
        value: Hashable,
        start: SupportsIndex = 0,
        end: SupportsIndex = sys.maxsize,
        /,
    ) -> int:
        return self.data.index(cast(Any, value), start, end)
