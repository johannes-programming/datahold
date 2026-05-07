from typing import *

import namings
from namings import FrozenNaming

from .BaseDataNaming import BaseDataNaming
from .FrozenDataObject import FrozenDataObject

__all__ = ["FrozenDataNaming"]

Value = TypeVar("Value")


class FrozenDataNaming(
    FrozenDataObject,
    BaseDataNaming[Value],
    namings.abc.FrozenNamingABC.FrozenNamingABC[Value],
):
    data: FrozenNaming[Value]
    __slots__ = ()
