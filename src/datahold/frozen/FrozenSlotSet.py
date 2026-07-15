from __future__ import annotations

__all__: list[str] = ["FrozenSlotSet"]
from typing import Self

import setdoc

from ..base.BaseDataSet import BaseDataSet


class FrozenSlotSet[Item](BaseDataSet[Item]):
    """Act as frozen set-like class."""

    __slots__ = ("_data",)

    type Data[DataItem] = frozenset[DataItem]

    @setdoc.basic
    def __data__(self: Self) -> Data[Item]:
        return self.__data__()

    @setdoc.basic
    def __init__(
        self: Self,
        data: BaseDataSet.Init[Item] = (),
        /,
    ):
        self._data: FrozenSlotSet.Data[Item] = frozenset(data)
