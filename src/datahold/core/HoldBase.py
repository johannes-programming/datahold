from typing import *

from datahold.core.DataBase import DataBase

__all__ = ["HoldBase"]


class HoldBase(DataBase):
    __slots__ = ("_data",)
    data: Any
