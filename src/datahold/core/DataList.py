import collections
from typing import *

from datahold._utils import deco
from datahold._utils.Cfg import Cfg
from datahold.core.DataABC import DataABC

__all__ = ["DataList"]


Item = TypeVar("Item")


@deco.unfrozenDeco(
    funcnames=Cfg.cfg.data["unfrozen"]["list"],
    Frozen=tuple[Item, ...],
    NonFrozen=list[Item],
)
@deco.frozenDeco(
    funcnames=Cfg.cfg.data["frozen"]["list"],
    Frozen=tuple[Item, ...],
    NonFrozen=list[Item],
)
@deco.initDeco(
    Frozen=tuple[Item, ...],
    NonFrozen=list[Item],
)
class DataList(DataABC, collections.abc.MutableSequence[Item]):
    __slots__ = ()
    data: tuple[Item, ...]
