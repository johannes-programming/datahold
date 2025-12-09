
from .FrozenDataDict import FrozenDataDict
from .BaseHoldDict import BaseHoldDict
from .FrozenHoldObject import FrozenHoldObject
from typing import *
from frozendict import frozendict
import setdoc
__all__ = ["FrozenHoldDict"]

Key = TypeVar("Key")
Value = TypeVar("Value")

class FrozenHoldDict(BaseHoldDict[Key, Value], FrozenDataDict, FrozenHoldObject):
    data:frozendict[Key, Value]
    __slots__ = ()
    @setdoc.basic
    def __init__(self:Self, data:Any, /, **kwargs:Any)->None:
        self._data = frozendict[Key, Value](data, **kwargs)
