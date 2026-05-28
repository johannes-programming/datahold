import sys
from abc import abstractmethod
from collections.abc import Sequence, Iterable, Iterator
from typing import Any, Generic, Self, TypeVar, SupportsIndex, cast

import setdoc

from .BaseDataObject import BaseDataObject

__all__ = ["BaseDataList"]

Item = TypeVar("Item", covariant=True)
Item_ = TypeVar("Item_")


class BaseDataList(BaseDataObject, Generic[Item]):
    __slots__ = ()

    @setdoc.setdoc(list.__add__.__doc__)
    def __add__(self: Self, value: list[Item_], /) -> list[Item | Item_]:
        return list(self.data).__add__(value)

    @setdoc.setdoc(list.__contains__.__doc__)
    def __contains__(self: Self, value: object, /) -> bool:
        return list(self.data).__contains__(value)

    @setdoc.setdoc(list.__getitem__.__doc__)
    def __getitem__(self: Self, key: SupportsIndex, /) -> Item:
        return list(self.data).__getitem__(key)

    @abstractmethod
    @setdoc.setdoc(list.__init__.__doc__)
    def __init__(self: Self, data: Iterable[Item] = (), /) -> None: ...

    @setdoc.setdoc(list.__iter__.__doc__)
    def __iter__(self: Self, /) -> Iterator[Item]:
        return list(self.data).__iter__()

    @setdoc.setdoc(list.__len__.__doc__)
    def __len__(self: Self, /) -> int:
        return list(self.data).__len__()

    @setdoc.setdoc(list.__mul__.__doc__)
    def __mul__(self: Self, value: SupportsIndex, /) -> list[Item]:
        return list(self.data).__mul__(value)

    @setdoc.setdoc(list.__repr__.__doc__)
    def __repr__(self: Self, /) -> str:
        return list(self.data).__repr__()

    @setdoc.setdoc(list.__reversed__.__doc__)
    def __reversed__(self: Self, /) -> Iterator[Item]:
        return list(self.data).__reversed__()

    @setdoc.setdoc(list.__rmul__.__doc__)
    def __rmul__(self: Self, value: SupportsIndex, /) -> list[Item]:
        return list(self.data).__rmul__(value)

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
