from typing import *

from frozendict import frozendict

from datahold._utils import unfrozen
from datahold.core.DataDict import DataDict
from datahold.core.HoldBase import HoldBase

__all__ = ["HoldDict"]

Key = TypeVar("Key")
Value = TypeVar("Value")


@unfrozen.dataDeco()
class HoldDict(HoldBase, DataDict[Key, Value]):
    __slots__ = ()
    data: frozendict[Key, Value]
