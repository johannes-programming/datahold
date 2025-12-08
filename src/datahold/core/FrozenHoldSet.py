from typing import *

from datahold._utils import frozen
from datahold.core.FrozenDataSet import FrozenDataSet
from datahold.core.FrozenHoldBase import FrozenHoldBase

__all__ = ["FrozenHoldSet"]

Item = TypeVar("Item")


@frozen.initDeco(
    Frozen=frozenset[Item],
    NonFrozen=set[Item],
)
class FrozenHoldSet(
    FrozenHoldBase,
    FrozenDataSet[Item],
):

    __slots__ = ()

    data: frozenset[Item]
