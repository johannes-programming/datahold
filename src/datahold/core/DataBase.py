from typing import *

import setdoc

from datahold.core.FrozenDataBase import FrozenDataBase

__all__ = ["DataBase"]

Data = TypeVar("Data")


class DataBase(FrozenDataBase[Data]):
    __slots__ = ()

    data: Data

    __hash__ = None

    @setdoc.basic
    def __init__(self: Self, *args: Any, **kwargs: Any) -> None:
        self.data = Data(*args, **kwargs)
