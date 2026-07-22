"""Provide HoldDict."""

from __future__ import annotations

__all__: list[str] = ["HoldDict"]

from collections.abc import Hashable
from typing import Self

import setdoc
from frozendict import frozendict

from ..base.BaseHoldDict import BaseHoldDict
from .DataDict import DataDict
from .HoldObject import HoldObject


class HoldDict[Key: Hashable, Value](
    DataDict[Key, Value],
    BaseHoldDict[Key, Value],
    HoldObject,
):
    """Provide usable mutable dict-like with slots."""

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
