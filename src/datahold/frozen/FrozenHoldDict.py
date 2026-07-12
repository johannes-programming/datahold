from ..base.BaseDataDict import BaseDataDict
from typing import TypeVar, Self, Optional
from frozendict import frozendict
from collections.abc import Iterable
from .FrozenHoldFgettable import FrozenHoldFgettable
import setdoc
from ..typing.SupportsKeysAndGetitem import SupportsKeysAndGetitem

Key = TypeVar("Key", covariant=True)
Value = TypeVar("Value", covariant=True)
class FrozenHoldSet(
    FrozenHoldFgettable[frozendict[Key|str, Optional[Value]]], 
    BaseDataDict[Key, Value],
):
    __slots__ = ()
    @setdoc.basic
    def __fset__(
        self:Self, 
        data:SupportsKeysAndGetitem[Key|str, Optional[Value]]|Iterable[tuple[Key, Value]],
    ) -> None:
        self._data = frozendict(data)