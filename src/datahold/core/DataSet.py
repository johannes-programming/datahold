import collections
from typing import *

from datahold._utils import deco
from datahold._utils.Cfg import Cfg
from datahold.core.DataBase import DataBase
from datahold.core.FrozenDataSet import FrozenDataSet

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
class DataSet(
    DataBase,
    FrozenDataSet[Item],
    collections.abc.MutableSet[Item],
):
    __slots__ = ()
    data: frozenset[Item]
