import collections
from typing import *

from datahold._utils import frozen
from datahold._utils.Cfg import Cfg
from datahold.core.FrozenDataBase import FrozenDataBase

__all__ = ["FrozenDataSet"]

Item = TypeVar("Item")


@frozen.frozenDeco(
    funcnames=Cfg.cfg.data["frozen"]["set"],
    Frozen=frozenset[Item],
    NonFrozen=set[Item],
)
class FrozenDataSet(
    FrozenDataBase,
    collections.abc.Set[Item],
):
    __slots__ = ()
    data: frozenset[Item]
