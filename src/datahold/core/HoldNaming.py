from typing import *

import setdoc
from namings import FrozenNaming

from .BaseHoldNaming import BaseHoldNaming
from .DataNaming import DataNaming
from .HoldObject import HoldObject

__all__ = ["HoldNaming"]

Value = TypeVar("Value")


class HoldNaming(HoldObject, DataNaming[Value], BaseHoldNaming[Value]):
    data: FrozenNaming[Value]
    __slots__ = ()

    @property
    @setdoc.basic
    def data(self: Self) -> FrozenNaming[Value]:
        return self._data

    @data.setter
    def data(self: Self, value: Any) -> None:
        self._data = FrozenNaming[Value](value)
