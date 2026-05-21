from collections.abc import Iterable
from typing import Any, Self, TypeVar

import setdoc
from frozendict import frozendict

from ..base.BaseHoldDict import BaseHoldDict
from ..typing.SupportsKeysAndGetitem import SupportsKeysAndGetitem
from .DataDict import DataDict
from .HoldObject import HoldObject

__all__ = ["HoldDict"]

Key = TypeVar("Key")
Value = TypeVar("Value")


class HoldDict(HoldObject, DataDict[Key, Value], BaseHoldDict[Key, Value]):

    __slots__ = ()

    @property
    @setdoc.basic
    def data(self: Self) -> frozendict[Key, Value]:
        return self._data

    @data.setter
    def data(
        self: Self,
        value: Iterable[tuple[Key, Value]] | SupportsKeysAndGetitem[Key, Value],
    ) -> None:
        data_: Any
        data_ = value
        self._data = frozendict(data_)
