import typing
from abc import abstractmethod

from frozendict import frozendict

from .BaseDataDict import BaseDataDict
from .BaseHoldObject import BaseHoldObject

__all__ = ["BaseHoldDict"]

Key = typing.TypeVar("Key", covariant=True)
Value = typing.TypeVar("Value", covariant=True)


class BaseHoldDict(BaseHoldObject, BaseDataDict[Key, Value]):
    __slots__ = ()
