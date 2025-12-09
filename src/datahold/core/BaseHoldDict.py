from typing import *
from .BaseHoldObject import BaseHoldObject
from .BaseDataDict import BaseDataDict
from frozendict import frozendict

__all__ = ["BaseHoldDict"]

Key = TypeVar("Key")
Value = TypeVar("Value")

class BaseHoldDict(BaseDataDict[Key, Value], BaseHoldObject):
    data:frozendict[Key, Value]
    __slots__ = ()

