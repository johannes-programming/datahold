import collections
from typing import *

from datahold._utils import deco
from datahold._utils.Cfg import Cfg
from datahold.core.HashABC import HashABC

__all__ = ["HashList"]


Item = TypeVar("Item")


@deco.frozenDeco(
    funcnames=Cfg.cfg.data["frozen"]["list"],
    Frozen=tuple[Item, ...],
    NonFrozen=list[Item],
)
class HashList(HashABC, collections.abc.MutableSequence[Item]):
    __slots__ = ()
    data: tuple[Item, ...]
