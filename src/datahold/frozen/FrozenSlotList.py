from __future__ import annotations

__all__: list[str] = ["FrozenSlotList"]
from typing import Self

import setdoc

from ..base.BaseDataList import BaseDataList


class FrozenSlotList[Item](BaseDataList[Item]):
    """Act as frozen list-like class."""

    __slots__ = ("_data",)

    type Data[DataItem] = tuple[DataItem, ...]

    @setdoc.basic
    def __data__(self: Self) -> Data[Item]:
        return self.__data__()

    @setdoc.basic
    def __init__(
        self: Self,
        data: BaseDataList.Init[Item] = (),
        /,
    ):
        self._data: FrozenSlotList.Data[Item] = tuple(data)
