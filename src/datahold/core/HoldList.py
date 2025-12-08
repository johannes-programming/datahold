from typing import *

from datahold._utils.deco import unfrozen
from datahold.core.DataList import DataList
from datahold.core.HoldBase import HoldBase

__all__ = ["HoldList"]

Item = TypeVar("Item")


@unfrozen.dataDeco()
class HoldList(HoldBase, DataList[Item]):
    __slots__ = ()
    data: tuple[Item, ...]
