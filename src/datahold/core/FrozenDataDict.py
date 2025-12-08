import collections
from typing import *

from frozendict import frozendict

from datahold._utils import deco
from datahold._utils.Cfg import Cfg
from datahold.core.FrozenDataBase import FrozenDataBase

__all__ = ["FrozenDataDict"]

Key = TypeVar("Key")
Value = TypeVar("Value")


@deco.frozenDeco(
    funcnames=Cfg.cfg.data["frozen"]["dict"],
    Frozen=frozendict[Key, Value],
    NonFrozen=dict[Key, Value],
)
class FrozenDataDict(
    FrozenDataBase[frozendict[Key, Value]],
    collections.abc.Mapping[Key, Value],
):
    __slots__ = ()
    data: frozendict[Key, Value]
