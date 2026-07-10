"""Provide HoldDict."""

__all__: list[str] = ["HoldDict"]

from collections.abc import Hashable, Iterable
from typing import Optional, Self, TypeVar

import setdoc
from frozendict import frozendict

from ..base.BaseHoldDict import BaseHoldDict
from ..typing.SupportsKeysAndGetitem import SupportsKeysAndGetitem
from .DataDict import DataDict
from .HoldObject import HoldObject

Key = TypeVar("Key", bound=Hashable)
Value = TypeVar("Value")


class HoldDict(DataDict[Key, Value], BaseHoldDict[Key, Value], HoldObject):

    __slots__ = ()

    @property
    @setdoc.basic
    def data(self: Self) -> frozendict[Key | str, Optional[Value]]:
        return self._data

    @data.setter
    @setdoc.basic
    def data(
        self: Self,
        value: (
            SupportsKeysAndGetitem[Key | str, Optional[Value]]
            | Iterable[tuple[Key | str, Optional[Value]]]
        ),
    ) -> None:
        self._data = frozendict(value)  # type: ignore[arg-type]
