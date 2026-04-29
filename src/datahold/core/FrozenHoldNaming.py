from typing import *

import setdoc
from namings import FrozenNaming

from .BaseHoldNaming import BaseHoldNaming
from .FrozenDataNaming import FrozenDataNaming
from .FrozenHoldObject import FrozenHoldObject

__all__ = ["FrozenHoldNaming"]

Value = TypeVar("Value")


class FrozenHoldNaming(FrozenHoldObject, FrozenDataNaming, BaseHoldNaming[Value]):
    data: FrozenNaming[Value]
    __slots__ = ()

    @setdoc.basic
    def __init__(self: Self, data: Any, /, **kwargs: Any) -> None:
        self._data = FrozenNaming[Value](data, **kwargs)
