import types
import typing
from collections.abc import Iterable

import setdoc

from ..base.BaseHoldDict import BaseHoldDict
from ..typing.SupportsKeysAndGetitem import SupportsKeysAndGetitem
from .DataDict import DataDict
from .HoldObject import HoldObject

__all__ = ["HoldDict"]

Key = typing.TypeVar("Key")
Value = typing.TypeVar("Value")


class HoldDict(HoldObject, DataDict[Key, Value], BaseHoldDict[Key, Value]):

    __slots__ = ()

    @property
    @setdoc.basic
    def data(self: typing.Self) -> types.MappingProxyType[Key, Value]:
        return self._data

    @data.setter
    def data(
        self: typing.Self,
        value: Iterable[tuple[Key, Value]] | SupportsKeysAndGetitem[Key, Value],
    ) -> None:
        self._data = types.MappingProxyType(dict(value))
