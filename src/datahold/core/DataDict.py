import collections
from typing import *

from frozendict import frozendict

from datahold._utils.Cfg import Cfg
from datahold._utils.deco import unfrozen
from datahold.core.DataBase import DataBase
from datahold.core.FrozenDataDict import FrozenDataDict

Key = TypeVar("Key")
Value = TypeVar("Value")


@unfrozen.unfrozenDeco(
    funcnames=Cfg.cfg.data["unfrozen"]["dict"],
    Frozen=frozendict[Key, Value],
    NonFrozen=dict[Key, Value],
)
@unfrozen.initDeco(
    Frozen=frozendict[Key, Value],
    NonFrozen=dict[Key, Value],
)
class DataDict(
    DataBase,
    FrozenDataDict[Key, Value],
    collections.abc.MutableMapping[Key, Value],
):
    __slots__ = ()
    data: frozendict[Key, Value]
