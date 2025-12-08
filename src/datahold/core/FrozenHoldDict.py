from typing import *

from frozendict import frozendict

from datahold._utils import frozen
from datahold.core.FrozenDataDict import FrozenDataDict
from datahold.core.FrozenHoldBase import FrozenHoldBase

__all__ = ["FrozenHoldDict"]

Key = TypeVar("Key")
Value = TypeVar("Value")


@frozen.initDeco(
    Frozen=frozendict[Key, Value],
    NonFrozen=dict[Key, Value],
)
class FrozenHoldDict(
    FrozenHoldBase,
    FrozenDataDict[Key, Value],
):

    __slots__ = ()

    data: frozendict[Key, Value]
