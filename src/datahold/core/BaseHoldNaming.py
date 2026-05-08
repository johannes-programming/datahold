from typing import *

import namings

from .BaseDataNaming import BaseDataNaming
from .BaseHoldObject import BaseHoldObject

__all__ = ["BaseHoldNaming"]

Value = TypeVar("Value")


class BaseHoldNaming(BaseHoldObject, BaseDataNaming[Value]):
    data: namings.FrozenNaming[Value]
    __slots__ = ()
