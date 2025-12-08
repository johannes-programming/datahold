from typing import *

from datahold.core.FrozenDataBase import FrozenDataBase

__all__ = ["DataBase"]


class DataBase(FrozenDataBase):
    __slots__ = ()

    __hash__ = None
