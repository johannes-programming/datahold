import collections
from typing import *

from datahold._utils import unfrozen
from datahold._utils.Cfg import Cfg
from datahold.core.DataBase import DataBase
from datahold.core.FrozenDataList import FrozenDataList

__all__ = ["DataList"]


Item = TypeVar("Item")


@unfrozen.funcDeco(
    funcnames=Cfg.cfg.data["unfrozen"]["list"],
    Frozen=tuple[Item, ...],
    NonFrozen=list[Item],
)
@unfrozen.initDeco(
    Frozen=tuple[Item, ...],
    NonFrozen=list[Item],
)
class DataList(
    DataBase,
    FrozenDataList[Item],
    collections.abc.MutableSequence[Item],
):
    __slots__ = ()
    data: tuple[Item, ...]
