import collections
from typing import *

from datahold._utils import deco
from datahold._utils.Cfg import Cfg
from datahold.core.FrozenDataABC import FrozenDataABC

__all__ = ["FrozenDataList"]

Item = TypeVar("Item")


@deco.frozenDeco(
    funcnames=Cfg.cfg.data["frozen"]["list"],
    Frozen=tuple[Item, ...],
    NonFrozen=list[Item],
)
class FrozenDataList(
    FrozenDataABC,
    collections.abc.Sequence[Item],
):
    __slots__ = ()
    data: tuple[Item, ...]
