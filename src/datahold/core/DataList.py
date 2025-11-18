import collections
from typing import *

from datahold._utils import deco
from datahold._utils.Cfg import Cfg
from datahold.core.DataABC import DataABC

__all__ = ["DataList"]


Item = TypeVar("Item")


@deco.funcDeco(
    funcnames=Cfg.cfg.data["datafuncs"]["List"],
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
