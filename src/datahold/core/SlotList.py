__all__: list[str] = ["SlotList"]
from typing import Self, TypeVar

import setdoc

from .DataList import DataList

Item = TypeVar("Item", covariant=True)


class SlotList(DataList[Item]):
    """Work as a list-like class."""

    __slots__ = ("_data",)

    @setdoc.basic
    def __fget__(self: Self) -> DataList.Data[Item]:
        return self._data

    @setdoc.basic
    def __fset__(self: Self, data: DataList.Data[Item], /) -> None:
        self._data: DataList.Data[Item] = data
