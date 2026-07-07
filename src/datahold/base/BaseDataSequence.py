"""Provide BaseDataList."""

from __future__ import annotations

__all__: list[str] = ["BaseDataSequence"]

import sys
from abc import abstractmethod
from collections.abc import Hashable, Iterable, Sequence
from typing import Any, Final, Self, SupportsIndex, TypeVar, cast, overload

import setdoc

from .BaseDataCollection import BaseDataCollection
from .BaseDataReversible import BaseDataReversible

Item = TypeVar("Item", covariant=True)


class BaseDataSequence(
    BaseDataReversible[Item], BaseDataCollection[Item], Sequence[Item]
):
    __slots__ = ()

    Data: Final[type[Sequence]] = Sequence  # type: ignore[type-abstract,type-arg]

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
            return self.data[index]  # type: ignore[call-overload,no-any-return]
        else:
            return type(self)(self.data[index])

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Iterable[Item] = (), /) -> None: ...

    @setdoc.basic
    def __repr__(self: Self, /) -> str:
        return f"{type(self).__name__}({list(self.data)!r})"

    @setdoc.basic
    def count(self: Self, item: Hashable, /) -> int:
        return self.data.count(cast(Any, item))

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Sequence[Item]: ...

    @setdoc.basic
    def index(
        self: Self,
        item: Hashable,
        start: SupportsIndex = 0,
        end: SupportsIndex = sys.maxsize,
        /,
    ) -> int:
        return self.data.index(cast(Any, item), start, end)  # type: ignore[arg-type]
