from __future__ import annotations

__all__: list[str] = ["FrozenDataFgettable"]
from typing import  Self, TypeVar
from ..base.BaseDataFgettable import BaseDataFgettable
import setdoc

Data = TypeVar("Data", covariant=True)


class FrozenDataFgettable(BaseDataFgettable[Data]):

    __slots__ = ()

    @property
    @setdoc.basic
    def data(self: Self) -> Data:
        return self.__fget__()
