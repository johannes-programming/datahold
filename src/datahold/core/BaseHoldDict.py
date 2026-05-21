from abc import abstractmethod
from typing import *

import types

from .BaseDataDict import BaseDataDict
from .BaseHoldObject import BaseHoldObject

__all__ = ["BaseHoldDict"]

Key = TypeVar("Key", covariant=True)
Value = TypeVar("Value", covariant=True)


class BaseHoldDict(BaseHoldObject, BaseDataDict[Key, Value]):
    __slots__ = ()

    @property
    @abstractmethod
    def data(self: Self) -> types.MappingProxyType[Key, Value]: ...
