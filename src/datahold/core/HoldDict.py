"""Provide HoldDict."""

from __future__ import annotations

__all__: list[str] = ["HoldDict"]

from collections import abc
from typing import Self

import setdoc
from frozendict import frozendict

from ..base.BaseHoldCollection import BaseHoldCollection
from .DataDict import DataDict


class HoldDict[Key: abc.Hashable, Value](
    DataDict[Key, Value],
    BaseHoldCollection[Key | str],
):
    """Provide usable mutable dict-like with slots."""

    __slots__ = ()

    @setdoc.basic
    def __fget__(self: Self) -> HoldDict.Data[Key, Value]:
        return self._data

    @setdoc.basic
    def __fset__(
        self: Self,
        value: HoldDict.Init[Key, Value],
        /,
    ) -> None:
        self._data: HoldDict.Data[Key, Value] = frozendict(value)  # type: ignore[arg-type]
