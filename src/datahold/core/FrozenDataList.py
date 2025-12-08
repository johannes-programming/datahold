import collections
from typing import *

from datahold._utils import frozen
from datahold._utils.Cfg import Cfg
from datahold.core.FrozenDataBase import FrozenDataBase

__all__ = ["FrozenDataList"]

Item = TypeVar("Item")


@frozen.funcDeco(
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
