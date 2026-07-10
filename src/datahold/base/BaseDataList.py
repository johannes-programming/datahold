"""Provide BaseDataList."""

from __future__ import annotations

__all__: list[str] = ["BaseDataList"]

import sys
from abc import abstractmethod
from collections.abc import Hashable, Iterable, Sequence
from typing import Any, Self, SupportsIndex, TypeVar, cast, overload

import setdoc

from .BaseDataCollection import BaseDataCollection
from .BaseDataReversible import BaseDataReversible

Item = TypeVar("Item", covariant=True)
Data_ = tuple[Item, ...]


class BaseDataList(
    BaseDataReversible[Item], BaseDataCollection[Item], Sequence[Item]
):
    __slots__ = ()

    Data = Data_

    @setdoc.basic
    def __add__(self: Self, other: Iterable[Item], /) -> Self:
        return type(self)(self.data + tuple(other))

    @setdoc.basic
    def __contains__(self: Self, other: object, /) -> bool:
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
        return f"{type(self).__name__}({list(self.data)!r})"

    @setdoc.basic
    def __rmul__(self: Self, other: SupportsIndex, /) -> Self:
        return type(self)(other * self.data)

    @setdoc.basic
    def count(self: Self, item: Hashable, /) -> int:
        return self.data.count(cast(Any, item))

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data_[Item]: ...

    @setdoc.basic
    def index(
        self: Self,
        item: Hashable,
        start: SupportsIndex = 0,
        end: SupportsIndex = sys.maxsize,
        /,
    ) -> int:
        return self.data.index(cast(Any, item), start, end)
