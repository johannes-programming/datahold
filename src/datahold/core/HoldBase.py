from typing import *

from datahold.core.DataBase import DataBase

__all__ = ("HoldBase",)
Data = TypeVar("Data")


class HoldBase(DataBase[Data]):
    __slots__ = ("_data",)
