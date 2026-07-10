"""Provide FrozenDataDict."""

__all__: list[str] = ["FrozenDataDict"]

from collections.abc import Hashable
from typing import TypeVar

from ..base.BaseDataDict import BaseDataDict
from .FrozenDataObject import FrozenDataObject

Key = TypeVar("Key", bound=Hashable, covariant=True)
Value = TypeVar("Value", covariant=True)


class FrozenDataDict(BaseDataDict[Key, Value], FrozenDataObject):
    __slots__ = ()
