"""Provide HoldSet."""

from __future__ import annotations

__all__: list[str] = ["HoldSet"]

from collections import abc
from typing import Self, TypeVar

import setdoc

from ..base.BaseHoldCollection import BaseHoldCollection
from .DataSet import DataSet

Item = TypeVar("Item", bound=abc.Hashable)


class HoldSet[Item: abc.Hashable](
    DataSet[Item],
    BaseHoldCollection[Item],
):
    """Provide usable mutable set-like with slots."""

    __slots__ = ()

    @setdoc.basic
    def __fget__(self: Self) -> HoldSet.Data[Item]:
        return self._data

    @setdoc.basic
    def __fset__(self: Self, value: abc.Iterable[Item], /) -> None:
        self._data: HoldSet.Data[Item] = frozenset(value)
