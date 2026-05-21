from abc import abstractmethod
from typing import *

from frozendict import frozendict

from ..base.BaseDataDict import BaseDataDict
from .FrozenDataObject import FrozenDataObject

__all__ = ["FrozenDataDict"]

Key = TypeVar("Key", covariant=True)
Value = TypeVar("Value", covariant=True)


class FrozenDataDict(FrozenDataObject, BaseDataDict[Key, Value]):
    __slots__ = ()

    @property
    @abstractmethod
    def data(self: Self) -> frozendict[Key, Value]: ...
