"""Provide BaseDataList."""

from __future__ import annotations

__all__: list[str] = ["BaseDataList"]

from abc import abstractmethod
from collections.abc import Iterable
from typing import Self, SupportsIndex, TypeVar

import setdoc

from .BaseDataSequence import BaseDataSequence

Item = TypeVar("Item", covariant=True)


class BaseDataList(BaseDataSequence[Item]):
    __slots__ = ()

    @setdoc.basic
    def __add__(self: Self, other: Iterable[Item], /) -> Self:
        return type(self)(self.data + tuple(other))

    @setdoc.basic
    def __mul__(self: Self, other: SupportsIndex, /) -> Self:
        return type(self)(self.data * other)

    @setdoc.basic
    def __rmul__(self: Self, other: SupportsIndex, /) -> Self:
        return type(self)(other * self.data)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> tuple[Item, ...]: ...
