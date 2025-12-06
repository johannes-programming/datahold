from typing import *

from frozendict import frozendict

from datahold._utils import deco
from datahold._utils.Cfg import Cfg
from datahold.core.DataABC import DataABC
from datahold.core.HashDict import HashDict

Key = TypeVar("Key")
Value = TypeVar("Value")


@deco.unfrozenDeco(
    funcnames=Cfg.cfg.data["unfrozen"]["dict"],
    Frozen=frozendict[Key, Value],
    NonFrozen=dict[Key, Value],
)
@deco.initDeco(
    Frozen=frozendict[Key, Value],
    NonFrozen=dict[Key, Value],
)
class DataDict(DataABC, HashDict[Key, Value]):
    __slots__ = ()
    data: frozendict[Key, Value]
