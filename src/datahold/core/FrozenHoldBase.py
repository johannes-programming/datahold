from typing import *

from datahold.core.FrozenDataBase import FrozenDataBase

__all__ = ["FrozenHoldBase"]


class FrozenHoldBase(FrozenDataBase):

    __slots__ = ("_data",)

    data: Any

    @property
    def data(self: Self) -> Any:
        return self._data
