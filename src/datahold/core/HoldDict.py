"""Provide HoldDict."""

from __future__ import annotations

__all__: list[str] = ["HoldDict"]

from typing import Self

import setdoc
from frozendict import frozendict

from ..base.BaseDataDict import BaseDataDict
from ..base.BaseHoldCollection import BaseHoldCollection
from .DataDict import DataDict


class HoldDict[Key, Value](
    DataDict[Key, Value],
    BaseDataDict[Key, Value],
    BaseHoldCollection[Key | str],
):

    __slots__ = ()

    @property
    @setdoc.basic
    def data(self: Self) -> HoldDict.Data[Key, Value]:
        return self._data

    @data.setter
    @setdoc.basic
    def data(
        self: Self,
        value: HoldDict.Init[Key, Value],
    ) -> None:
        self._data: HoldDict.Data[Key, Value] = frozendict(value)  # type: ignore[arg-type]
