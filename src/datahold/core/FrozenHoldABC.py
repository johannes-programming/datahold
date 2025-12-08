from typing import *

from datahold.core.FrozenDataABC import FrozenDataABC

__all__ = ["FrozenHoldDict"]


class FrozenHoldDict(FrozenDataABC):

    __slots__ = ("_data",)

    data: Any

    @property
    def data(self: Self) -> Any:
        return self._data
