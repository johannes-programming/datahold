import collections
from typing import *

from datahold._utils import deco
from datahold._utils.Cfg import Cfg
from datahold.core.FrozenDataABC import FrozenDataABC

__all__ = ["FrozenDataSet"]

Item = TypeVar("Item")


@deco.frozenDeco(
    funcnames=Cfg.cfg.data["frozen"]["set"],
    Frozen=frozenset[Item],
    NonFrozen=set[Item],
)
class FrozenDataSet(
    FrozenDataABC,
    collections.abc.Set[Item],
):
    __slots__ = ()
    data: frozenset[Item]
