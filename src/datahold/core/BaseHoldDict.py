from types import MappingProxyType
from typing import *

from .BaseDataDict import BaseDataDict
from .BaseHoldObject import BaseHoldObject

__all__ = ["BaseHoldDict"]

Key = TypeVar("Key")
Value = TypeVar("Value")


class BaseHoldDict(BaseHoldObject, BaseDataDict[Key, Value]):
    data: MappingProxyType[Key, Value]
    __slots__ = ()
