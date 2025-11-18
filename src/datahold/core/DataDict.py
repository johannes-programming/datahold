import collections
from typing import *

from frozendict import frozendict

from datahold._utils import deco
from datahold._utils.Cfg import Cfg
from datahold.core.DataABC import DataABC

Key = TypeVar("Key")
Value = TypeVar("Value")


@deco.funcDeco(
    funcnames=Cfg.cfg.data["datafuncs"]["Dict"],
    Frozen=frozendict[Key, Value],
    NonFrozen=dict[Key, Value],
)
@deco.initDeco(
    Frozen=frozendict[Key, Value],
    NonFrozen=dict[Key, Value],
)
class DataDict(DataABC, collections.abc.MutableMapping[Key, Value]):
    __slots__ = ()
    data: frozendict[Key, Value]
