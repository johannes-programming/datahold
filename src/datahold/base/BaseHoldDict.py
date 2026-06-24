"""Provide BaseHoldDict."""

__all__ = ["BaseHoldDict"]

from collections.abc import Hashable
from typing import TypeVar

from .BaseDataDict import BaseDataDict
from .BaseHoldObject import BaseHoldObject

Key = TypeVar("Key", bound=Hashable, covariant=True)
Value = TypeVar("Value", covariant=True)


class BaseHoldDict(BaseHoldObject, BaseDataDict[Key, Value]):
    __slots__ = ()
