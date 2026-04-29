from typing import *

from namings import FrozenNaming

from .BaseDataNaming import BaseDataNaming
from .BaseHoldObject import BaseHoldObject

__all__ = ["BaseHoldNaming"]

Value = TypeVar("Value")


class BaseHoldNaming(BaseHoldObject, BaseDataNaming[Value]):
    data: FrozenNaming[Value]
    __slots__ = ()
