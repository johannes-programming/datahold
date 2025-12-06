from typing import *

from unhash import unhash

from datahold.core.HashABC import HashABC

__all__ = ["HashABC"]


class DataABC(HashABC):
    __slots__ = ()

    data: Any

    __hash__ = None
