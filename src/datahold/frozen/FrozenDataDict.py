"""Provide FrozenDataDict."""

__all__ = ["FrozenDataDict"]

from collections.abc import Hashable
from typing import TypeVar

from ..base.BaseDataDict import BaseDataDict
from .FrozenDataObject import FrozenDataObject

Key = TypeVar("Key", bound=Hashable, covariant=True)
Value = TypeVar("Value", covariant=True)


class FrozenDataDict(FrozenDataObject, BaseDataDict[Key, Value]):
    __slots__ = ()
