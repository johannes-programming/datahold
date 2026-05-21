from typing import Self, TypeVar
from collections.abc import Iterable

import setdoc
from frozendict import frozendict

from ..base.BaseHoldDict import BaseHoldDict
from .DataDict import DataDict
from .HoldObject import HoldObject
from ..typing.SupportsKeysAndGetitem import SupportsKeysAndGetitem

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
            value: Iterable | SupportsKeysAndGetitem[Key, Value],
    ) -> None:
        self._data = frozendict(value)
