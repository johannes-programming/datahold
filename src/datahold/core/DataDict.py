from typing import *

from frozendict import frozendict

from datahold._utils import deco
from datahold._utils.Cfg import Cfg
from datahold.core.DataBase import DataBase

__all__ = ["DataDict"]

Key = TypeVar("Key")
Value = TypeVar("Value")


@deco.unfrozenDeco(
    funcnames=Cfg.cfg.data["unfrozen"]["dict"],
    Frozen=frozendict[Key, Value],
    NonFrozen=dict[Key, Value],
)
class DataDict(DataBase):
    __slots__ = ()
    data: frozendict[Key, Value]
