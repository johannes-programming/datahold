from typing import *

from datahold._utils import deco
from datahold.core.DataSet import DataSet
from datahold.core.HoldABC import HoldABC

__all__ = [
    "HoldSet",
]


@deco.dataDeco()
class HoldSet(HoldABC, DataSet):
    __slots__ = ()
    data: frozenset
