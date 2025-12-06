from typing import *

from datahold._utils import deco
from datahold._utils.Cfg import Cfg
from datahold.core.DataABC import DataABC
from datahold.core.HashSet import HashSet

__all__ = ["DataSet"]


Item = TypeVar("Item")


@deco.unfrozenDeco(
    funcnames=Cfg.cfg.data["unfrozen"]["set"],
    Frozen=frozenset[Item],
    NonFrozen=set[Item],
)
@deco.initDeco(
    Frozen=frozenset[Item],
    NonFrozen=set[Item],
)
class DataSet(DataABC, HashSet[Item]):
    __slots__ = ()
    data: frozenset[Item]
