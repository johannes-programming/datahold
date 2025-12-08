from typing import *

from datahold.core.FrozenDataABC import FrozenDataABC

__all__ = ["DataABC"]


class DataABC(FrozenDataABC):
    __slots__ = ()

    __hash__ = None
