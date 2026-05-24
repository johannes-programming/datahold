import types
import typing
from abc import abstractmethod

from .BaseDataDict import BaseDataDict
from .BaseHoldObject import BaseHoldObject

__all__ = ["BaseHoldDict"]

Key = typing.TypeVar("Key", covariant=True)
Value = typing.TypeVar("Value", covariant=True)


class BaseHoldDict(BaseHoldObject, BaseDataDict[Key, Value]):
    __slots__ = ()

    @property
    @abstractmethod
    def data(self: typing.Self) -> types.MappingProxyType[Key, Value]: ...
