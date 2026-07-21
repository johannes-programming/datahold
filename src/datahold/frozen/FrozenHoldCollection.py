"""Provide FrozenHoldCollection."""
from __future__ import annotations

__all__: list[str] = ["FrozenHoldCollection"]

from typing import Self

import setdoc

from ..base.BaseHoldCollection import BaseHoldCollection
from .FrozenDataCollection import FrozenDataCollection


class FrozenHoldCollection[Item](
    FrozenDataCollection[Item], 
    BaseHoldCollection[Item],
):

    _data: FrozenHoldCollection.Data[Item]
    __slots__ = ()

    @property
    @setdoc.basic
    def data(self: Self) -> FrozenHoldCollection.Data[Item]:
        return self._data
