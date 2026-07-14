__all__:list[str]=["DataDict"]
from .DataMapping import DataMapping
from .DataCopyable import DataCopyable
from ..base.BaseDataDict import BaseDataDict
from ..typing.SupportsKeysAndGetitem import SupportsKeysAndGetitem
from collections.abc import Iterable
from typing import TypeVar, Self
import setdoc
from frozendict import frozendict

Key = TypeVar("Key")
Value = TypeVar("Value")

InitData = SupportsKeysAndGetitem[Key, Value] | Iterable[tuple[Key, Value]]

class DataDict(
    BaseDataDict[Key, Value],
    DataMapping[Key, Value],
    DataCopyable,
):
    __slots__=()
    @setdoc.basic
    def __ior__(self:Self, other:InitData[Key, Value], /) -> Self:
        self |= type(self)(self.__fget__() | frozendict(other))