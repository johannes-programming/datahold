__all__: list[str] = ["FrozenSlotSet"]

from typing import Self, TypeVar

import setdoc

from ..base.BaseDataSet import BaseDataSet

Item = TypeVar("Item", covariant=True)


class FrozenSlotSet(BaseDataSet[Item]):
    __slots__ = ("_data",)

    @setdoc.basic
    def __fget__(self: Self) -> frozenset[Item]:
        return self._data

    @setdoc.basic
    def __fset__(self: Self, data: frozenset[Item], /) -> None:
        self._data = data

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.__fget__())
