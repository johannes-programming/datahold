__all__: list[str] = ["SlotSet"]
from typing import Self, TypeVar

import setdoc

from .DataSet import DataSet

Item = TypeVar("Item", covariant=True)


class SlotSet(DataSet[Item]):
    """Work as a list-like class."""

    __slots__ = ("_data",)

    @setdoc.basic
    def __fget__(self: Self) -> DataSet.Data[Item]:
        return self._data

    @setdoc.basic
    def __fset__(self: Self, data: DataSet.Data[Item], /) -> None:
        self._data: DataSet.Data[Item] = data
