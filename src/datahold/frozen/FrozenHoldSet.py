"""Provide FrozenHoldSet."""

__all__: list[str] = ["FrozenHoldSet"]

from collections.abc import Iterable
from typing import Self

import setdoc

from ..base.BaseHoldSet import BaseHoldSet
from .FrozenDataSet import FrozenDataSet
from .FrozenHoldCollection import FrozenHoldCollection


class FrozenHoldSet[Item](
    FrozenDataSet[Item],
    BaseHoldSet[Item],
    FrozenHoldCollection[Item],
):

    __slots__ = ()

    @setdoc.basic
    def __init__(self: Self, data: Iterable[Item] = (), /) -> None:
        self._data: frozenset[Item] = frozenset(data)

    @property
    @setdoc.basic
    def data(self: Self) -> frozenset[Item]:
        return self._data
