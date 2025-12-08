import collections
from typing import *

from frozendict import frozendict

from datahold._utils import deco
from datahold._utils.Cfg import Cfg
from datahold.core.DataBase import DataBase
from datahold.core.FrozenDataDict import FrozenDataDict

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
class DataDict(
    DataBase,
    FrozenDataDict[Key, Value],
    collections.abc.MutableMapping[Key, Value],
):
    __slots__ = ()
    data: frozendict[Key, Value]
