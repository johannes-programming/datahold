from __future__ import annotations

__all__: list[str] = ["BaseDataSequence"]
from abc import abstractmethod
from collections.abc import Iterable, Sequence
from typing import Protocol, Self, TypeVar, overload

import setdoc

from .BaseDataCollection import BaseDataCollection
from .BaseDataFgettable import BaseDataFgettable

DataItem = TypeVar("DataItem", covariant=True)
Item = TypeVar("Item", covariant=True)


class Fget(BaseDataCollection.Data[DataItem], Protocol[DataItem]):

    @overload
    @setdoc.basic
    def __getitem__(self: Self, index: int) -> DataItem: ...

    @overload
    @setdoc.basic
    def __getitem__(self: Self, index: slice) -> Sequence[DataItem]: ...

    def __getitem__(
        self: Self, index: int | slice
    ) -> DataItem | Iterable[DataItem]: ...


Fget.__name__ = "Data"
setdoc.basic(Fget)


class BaseDataSequence(
    BaseDataCollection[Item],
    Sequence[Item],
):
    """Act as base class for sequence implementation which only has to override __fget__ and __fset__ to work immediately."""

    __slots__ = ()

    Data = Fget

    __contains__ = Sequence[object].__contains__

    @overload
    @setdoc.basic
    def __getitem__(self: Self, index: int) -> Item: ...

    @overload
    @setdoc.basic
    def __getitem__(self: Self, index: slice) -> Self: ...

    @setdoc.basic
    def __getitem__(self: Self, index: int | slice) -> Item | Self:
        # Sequence.__getitem__ reveals "Overload(def [_T_co] (typing.Sequence[_T_co], int) -> _T_co, def [_T_co] (typing.Sequence[_T_co], slice[int | None, int | None, int | None]) -> typing.Sequence[_T_co])"
        if isinstance(index, slice):
            # index cannot be an int now because subclassing slice is impossible
            # we are forced to assume a constructor signature
            # the subtype of BaseDataSequence might be immutable
            return type(self)(self.__fget__()[index])
        else:
            return self.__fget__()[index]

    @setdoc.basic
    def __init__(self: Self, data: Sequence[Item], /) -> None:
        self.__fset__(data)
