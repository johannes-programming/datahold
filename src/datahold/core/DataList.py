from typing import *

from datahold._utils import deco
from datahold._utils.Cfg import Cfg
from datahold.core.DataABC import DataABC
from datahold.core.HashList import HashList

__all__ = ["DataList"]


Item = TypeVar("Item")


@deco.unfrozenDeco(
    funcnames=Cfg.cfg.data["unfrozen"]["list"],
    Frozen=tuple[Item, ...],
    NonFrozen=list[Item],
)
@deco.initDeco(
    Frozen=tuple[Item, ...],
    NonFrozen=list[Item],
)
class DataList(DataABC, HashList[Item]):
    __slots__ = ()
    data: tuple[Item, ...]
