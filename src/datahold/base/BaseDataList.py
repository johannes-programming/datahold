import sys
from abc import abstractmethod
from collections.abc import Iterable, Iterator, Sequence
from typing import Any, Generic, Self, SupportsIndex, TypeVar, cast

import setdoc

from .BaseDataObject import BaseDataObject

__all__ = ["BaseDataList"]

Item = TypeVar("Item", covariant=True)
Item_ = TypeVar("Item_")


class BaseDataList(BaseDataObject, Generic[Item]):
    __slots__ = ()

    @setdoc.basic
    def __add__(self: Self, other: list[Item_], /) -> list[Item | Item_]:
        return list(self.data).__add__(other)

    @setdoc.basic
    def __contains__(self: Self, other: object, /) -> bool:
        return list(self.data).__contains__(other)

    @setdoc.basic
    def __getitem__(self: Self, index: SupportsIndex, /) -> Item:
        return list(self.data).__getitem__(index)

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Iterable[Item] = (), /) -> None: ...

    @setdoc.basic
    def __iter__(self: Self, /) -> Iterator[Item]:
        return list(self.data).__iter__()

    @setdoc.basic
    def __len__(self: Self, /) -> int:
        return list(self.data).__len__()

    @setdoc.basic
    def __mul__(self: Self, other: SupportsIndex, /) -> list[Item]:
        return list(self.data).__mul__(other)

    @setdoc.basic
    def __repr__(self: Self, /) -> str:
        return list(self.data).__repr__()

    @setdoc.basic
    def __reversed__(self: Self, /) -> Iterator[Item]:
        return list(self.data).__reversed__()

    @setdoc.basic
    def __rmul__(self: Self, other: SupportsIndex, /) -> list[Item]:
        return list(self.data).__rmul__(other)

    @setdoc.setdoc(list.count.__doc__)
    def count(self: Self, value: object, /) -> int:
        return list(self.data).count(cast(Any, value))

    @property
    @abstractmethod
    def data(self: Self) -> tuple[Item, ...]: ...

    @setdoc.setdoc(list.index.__doc__)
    def index(
        self: Self,
        value: object,
        start: SupportsIndex = 0,
        end: SupportsIndex = sys.maxsize,
        /,
    ) -> int:
        return list(self.data).index(cast(Any, value), start, end)


Sequence.register(BaseDataList)  # type: ignore[type-abstract]
