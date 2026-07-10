"""Provide FrozenHoldSet."""

__all__: list[str] = ["FrozenHoldSet"]

from collections.abc import Hashable, Iterable
from typing import Self, TypeVar

import setdoc

from ..base.BaseHoldSet import BaseHoldSet
from .FrozenDataSet import FrozenDataSet
from .FrozenHoldObject import FrozenHoldObject

Item = TypeVar("Item", bound=Hashable)


class FrozenHoldSet(
    FrozenDataSet[Item],
    BaseHoldSet[Item],
    FrozenHoldObject,
):

    __slots__ = ()

    @setdoc.basic
    def __init__(self: Self, data: Iterable[Item] = (), /) -> None:
        self._data: frozenset[Item]
        self._data = frozenset(data)

    @property
    @setdoc.basic
    def data(self: Self) -> frozenset[Item]:
        return self._data
