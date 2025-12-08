from typing import *

from datahold._utils import unfrozen
from datahold.core.DataSet import DataSet
from datahold.core.HoldBase import HoldBase

__all__ = ["HoldSet"]


Item = TypeVar("Item")


@unfrozen.dataDeco()
class HoldSet(HoldBase, DataSet[Item]):
    __slots__ = ()
    data: frozenset[Item]
