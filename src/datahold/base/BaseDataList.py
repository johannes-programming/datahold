"""Provide BaseDataList."""

from __future__ import annotations

__all__: list[str] = ["BaseDataList"]

from collections.abc import Iterable
from typing import Final, Self, SupportsIndex, TypeVar, cast, overload

import setdoc

from .BaseDataSequence import BaseDataSequence

Item = TypeVar("Item", covariant=True)

Data = tuple[Item, ...]


class BaseDataList(BaseDataSequence[Item]):  # type: ignore[misc]
    __slots__ = ()

    Data: Final[type[Data]] = Data

    @setdoc.basic
    def __add__(self: Self, other: Iterable[Item], /) -> Self:
        return type(self)(self.data + tuple(other))

    @setdoc.basic
    def __mul__(self: Self, other: SupportsIndex, /) -> Self:
        return type(self)(self.data * other)

    @setdoc.basic
    def __rmul__(self: Self, other: SupportsIndex, /) -> Self:
        return type(self)(other * self.data)
