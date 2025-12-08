from typing import *

from datahold._utils import deco
from datahold.core.DataList import DataList
from datahold.core.HoldABC import HoldABC

__all__ = ["HoldList"]

Item = TypeVar("Item")


@deco.dataDeco()
class HoldList(HoldABC, DataList[Item]):
    __slots__ = ()
    data: tuple[Item, ...]
