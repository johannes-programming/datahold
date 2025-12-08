from typing import *

from frozendict import frozendict

from datahold.core.FrozenHoldDict import FrozenHoldDict
from datahold.core.HoldBase import HoldBase

__all__ = ["HoldDict"]

Key = TypeVar("Key")
Value = TypeVar("Value")


class HoldDict(
    HoldBase[frozendict[Key, Value]],
    FrozenHoldDict[Key, Value],
): ...
