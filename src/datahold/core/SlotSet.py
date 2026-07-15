__all__: list[str] = ["SlotSet"]
from typing import Self
from collections.abc import Iterable

import setdoc

from .DataSet import DataSet



class SlotSet[Item](DataSet[Item]):
    """Provide set-like class."""

    __slots__ = ("_data",)

    Data = set

    @setdoc.basic
    def __data__(self:Self)->set[Item]:
        return self._data
    
    @setdoc.basic
    def __init__(self:Self, data:Iterable[Item] = (), /)->None:
        self._data:set[Item] = set(data)
