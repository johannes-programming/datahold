from __future__ import annotations
__all__: list[str] = ["SlotList"]
from typing import Self
from collections.abc import Iterable

import setdoc

from .DataList import DataList

class SlotList[Item](DataList[Item]):
    """Act as list-like class."""

    __slots__ = ("_data",)

    type Data[DataItem] = list[DataItem]

    @setdoc.basic
    def __data__(self:Self) -> list[Item]:
        return self._data
    
    @setdoc.basic
    def __init__(self: Self, data:Iterable[Item] =(), /) -> None:
        self._data:list[Item] = list(data)

