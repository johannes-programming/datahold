"""Provide FrozenHoldDict."""

from __future__ import annotations

__all__: list[str] = ["FrozenHoldDict"]

from typing import Optional, Self

import setdoc
from frozendict import frozendict

from ..base.BaseHoldCollection import BaseHoldCollection
from .FrozenDataDict import FrozenDataDict


class FrozenHoldDict[Key, Value](
    FrozenDataDict[Key, Value],
    BaseHoldCollection[Key | str],
):

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
