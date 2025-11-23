import collections
from typing import *

from datahold._utils import deco
from datahold._utils.Cfg import Cfg
from datahold.core.HashABC import HashABC

__all__ = ["HashSet"]


Item = TypeVar("Item")


@deco.frozenDeco(
    funcnames=Cfg.cfg.data["frozen"]["set"],
    Frozen=frozenset[Item],
    NonFrozen=set[Item],
)
@deco.initDeco(
    Frozen=frozenset[Item],
    NonFrozen=set[Item],
)
class HashSet(HashABC, collections.abc.MutableSet[Item]):
    __slots__ = ()
    data: frozenset[Item]
