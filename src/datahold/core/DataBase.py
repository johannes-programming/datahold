from typing import *

import setdoc

from datahold.core.FrozenDataBase import FrozenDataBase

__all__ = ["DataBase"]


class DataBase(FrozenDataBase):
    __slots__ = ()

    __hash__ = None

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self)
