__all__: list[str] = ["DataDict"]
from collections.abc import Iterable
from typing import Self, TypeVar

import setdoc
from frozendict import frozendict

from ..base.BaseDataDict import BaseDataDict
from ..typing.SupportsKeysAndGetitem import SupportsKeysAndGetitem
from .DataMapping import DataMapping

Key = TypeVar("Key")
Value = TypeVar("Value")

InitData = SupportsKeysAndGetitem[Key, Value] | Iterable[tuple[Key, Value]]


class DataDict(
    BaseDataDict[Key, Value],
    DataMapping[Key, Value],
):
    """Act as base class for dict-like implementation which only has to override __fget__ and __fset__ to work immediately."""

    __slots__ = ()

    @setdoc.basic
    def __ior__(self: Self, other: InitData[Key, Value], /) -> Self:
        self |= type(self)(self.__fget__() | frozendict(other))

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self.__fget__())
