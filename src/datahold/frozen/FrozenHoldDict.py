"""Provide FrozenHoldDict."""

from __future__ import annotations

__all__: list[str] = ["FrozenHoldDict"]

from collections.abc import Hashable
from typing import Optional, Self

import setdoc
from frozendict import frozendict

from ..base.BaseHoldDict import BaseHoldDict
from .FrozenDataDict import FrozenDataDict
from .FrozenHoldObject import FrozenHoldObject


class FrozenHoldDict[Key: Hashable, Value](
    FrozenDataDict[Key, Value],
    BaseHoldDict[Key, Value],
    FrozenHoldObject,
):
    """Provide usable frozen dict-like with slots."""

    __slots__ = ()

    @setdoc.basic
    def __init__(
        self: Self,
        data: FrozenHoldDict.Init[Key, Value] = (),
        /,
        **kwargs: Optional[Value],
    ) -> None:
        self._data: FrozenHoldDict.Data[Key, Value] = frozendict(
            data,  # type: ignore[arg-type]
            **kwargs,
        )

    @property
    @setdoc.basic
    def data(self: Self) -> FrozenHoldDict.Data[Key, Value]:
        return self._data
