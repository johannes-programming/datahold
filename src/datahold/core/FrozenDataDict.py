import collections
from typing import *

from frozendict import frozendict

from datahold._utils.Cfg import Cfg
from datahold._utils.deco import frozen
from datahold.core.FrozenDataBase import FrozenDataBase

__all__ = ["FrozenDataDict"]

Key = TypeVar("Key")
Value = TypeVar("Value")


@frozen.frozenDeco(
    funcnames=Cfg.cfg.data["frozen"]["dict"],
    Frozen=frozendict[Key, Value],
    NonFrozen=dict[Key, Value],
)
class FrozenDataDict(
    FrozenDataBase,
    collections.abc.Mapping[Key, Value],
):
    __slots__ = ()
    data: frozendict[Key, Value]
