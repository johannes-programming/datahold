from typing import *

from frozendict import frozendict

from datahold.core.FrozenDataDict import FrozenDataDict
from datahold.core.FrozenHoldBase import FrozenHoldBase

__slots__ = ("FrozenHoldDict",)

Key = TypeVar("Key")
Value = TypeVar("Value")


class FrozenHoldDict(
    FrozenHoldBase[frozendict[Key, Value]],
    FrozenDataDict[Key, Value],
):
    __slots__ = ()
