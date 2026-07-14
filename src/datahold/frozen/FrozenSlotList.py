__all__: list[str] = ["FrozenSlotList"]

from typing import Self, TypeVar

import setdoc

from ..base.BaseDataList import BaseDataList

Item = TypeVar("Item", covariant=True)


class FrozenSlotList(BaseDataList[Item]):
    __slots__ = ("_data",)

    @setdoc.basic
    def __fget__(self: Self) -> tuple[Item, ...]:
        return self._data

    @setdoc.basic
    def __fset__(self: Self, data: tuple[Item, ...], /) -> None:
        self._data = data

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.__fget__())
