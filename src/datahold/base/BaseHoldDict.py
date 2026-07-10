"""Provide BaseHoldDict."""

__all__: list[str] = ["BaseHoldDict"]

from collections.abc import Hashable
from typing import TypeVar

from .BaseDataDict import BaseDataDict
from .BaseHoldObject import BaseHoldObject

Key = TypeVar("Key", bound=Hashable, covariant=True)
Value = TypeVar("Value", covariant=True)


class BaseHoldDict(BaseDataDict[Key, Value], BaseHoldObject):
    __slots__ = ()
