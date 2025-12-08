from typing import *

import setdoc

from datahold.core.FrozenDataBase import FrozenDataBase

__all__ = ["FrozenHoldBase"]

Data = TypeVar("Data")


class FrozenHoldBase(FrozenDataBase[Data]):
    __slots__ = ("_data",)

    @setdoc.basic
    def __init__(self: Self, *args: Any, **kwargs: Any) -> None:
        self._data = Data(*args, **kwargs)

    @property
    def data(self: Self) -> Data:
        return self._data
