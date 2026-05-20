from typing import *

from frozendict import frozendict

from .BaseDataDict import BaseDataDict
from .FrozenDataObject import FrozenDataObject

__all__ = ["FrozenDataDict"]

Key = TypeVar("Key", covariant=True)
Value = TypeVar("Value", covariant=True)


class FrozenDataDict(FrozenDataObject, BaseDataDict[Key, Value]):
    data: frozendict[Key, Value]
    __slots__ = ()
