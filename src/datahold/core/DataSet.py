import collections
from typing import *

from datahold._utils import deco
from datahold._utils.Cfg import Cfg
from datahold.core.DataABC import DataABC

__all__ = ["DataSet"]


Item = TypeVar("Item")


@deco.funcDeco(
    funcnames=Cfg.cfg.data["datafuncs"]["Set"],
    Frozen=frozenset[Item],
    NonFrozen=set[Item],
)
@deco.initDeco(
    Frozen=frozenset[Item],
    NonFrozen=set[Item],
)
class DataSet(DataABC, collections.abc.MutableSet[Item]):
    __slots__ = ()
    data: frozenset[Item]
