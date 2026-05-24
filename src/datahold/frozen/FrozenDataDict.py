import typing

from ..base.BaseDataDict import BaseDataDict
from .FrozenDataObject import FrozenDataObject

__all__ = ["FrozenDataDict"]

Key = typing.TypeVar("Key", covariant=True)
Value = typing.TypeVar("Value", covariant=True)


class FrozenDataDict(FrozenDataObject, BaseDataDict[Key, Value]):
    __slots__ = ()
