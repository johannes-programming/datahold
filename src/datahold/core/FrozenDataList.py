import collections
from typing import *

from datahold._utils.Cfg import Cfg
from datahold._utils.deco import frozen
from datahold.core.FrozenDataBase import FrozenDataBase

__all__ = ["FrozenDataList"]

Item = TypeVar("Item")


@frozen.frozenDeco(
    funcnames=Cfg.cfg.data["frozen"]["list"],
    Frozen=tuple[Item, ...],
    NonFrozen=list[Item],
)
class FrozenDataList(
    FrozenDataBase,
    collections.abc.Sequence[Item],
):
    __slots__ = ()
    data: tuple[Item, ...]
