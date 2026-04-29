from typing import *

from namings import FrozenNaming

from .BaseDataNaming import BaseDataNaming
from .FrozenDataObject import FrozenDataObject

__all__ = ["FrozenDataNaming"]

Value = TypeVar("Value")


class FrozenDataNaming(FrozenDataObject, BaseDataNaming[Value]):
    data: FrozenNaming[Value]
    __slots__ = ()
