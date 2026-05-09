from types import MappingProxyType
from typing import *

from .BaseDataDict import BaseDataDict
from .FrozenDataObject import FrozenDataObject

__all__ = ["FrozenDataDict"]

Key = TypeVar("Key")
Value = TypeVar("Value")


class FrozenDataDict(FrozenDataObject, BaseDataDict[Key, Value]):
    data: MappingProxyType[Key, Value]
    __slots__ = ()
