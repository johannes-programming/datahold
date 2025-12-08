from typing import *

from datahold._utils import deco
from datahold.core.DataSet import DataSet
from datahold.core.HoldBase import HoldBase

__all__ = ["HoldSet"]


Item = TypeVar("Item")


@deco.dataDeco()
class HoldSet(HoldBase, DataSet[Item]):
    __slots__ = ()
    data: frozenset[Item]
