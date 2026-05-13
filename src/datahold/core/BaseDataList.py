import collections
import sys
from abc import abstractmethod
from typing import *

import setdoc

from .BaseDataObject import BaseDataObject

__all__ = ["BaseDataList"]

Item = TypeVar("Item")


class BaseDataList(
    BaseDataObject,
    collections.abc.Sequence[Item],
):
    data: tuple[Item, ...]
    __slots__ = ()

    @setdoc.setdoc(list.__add__.__doc__)
    def __add__(self: Self, value: list[Item], /) -> Any:
        return list(self.data).__add__(value)

    @setdoc.setdoc(list.__contains__.__doc__)
    def __contains__(self: Self, value: Any, /) -> Any:
        return list(self.data).__contains__(value)

    @setdoc.setdoc(list.__getitem__.__doc__)
    def __getitem__(self: Self, key: Any, /) -> Item:
        return list(self.data).__getitem__(key)

    @abstractmethod
    @setdoc.setdoc(list.__init__.__doc__)
    def __init__(self: Self, data: Iterable[Item] = (), /) -> None: ...

    @setdoc.setdoc(list.__iter__.__doc__)
    def __iter__(self: Self, /) -> Iterable[Item]:
        return list(self.data).__iter__()

    @setdoc.setdoc(list.__len__.__doc__)
    def __len__(self: Self, /) -> int:
        return list(self.data).__len__()

    @setdoc.setdoc(list.__mul__.__doc__)
    def __mul__(self: Self, value: Any, /) -> Any:
        return list(self.data).__mul__(value)

    @setdoc.setdoc(list.__repr__.__doc__)
    def __repr__(self: Self, /) -> str:
        return list(self.data).__repr__()

    @setdoc.setdoc(list.__reversed__.__doc__)
    def __reversed__(self: Self, /) -> Iterable[Item]:
        return list(self.data).__reversed__()

    @setdoc.setdoc(list.__rmul__.__doc__)
    def __rmul__(self: Self, value: Any, /) -> Any:
        return list(self.data).__rmul__(value)

    @setdoc.setdoc(list.count.__doc__)
    def count(self: Self, value: Item, /) -> int:
        return list(self.data).count(value)

    @setdoc.setdoc(list.index.__doc__)
    def index(
        self: Self,
        value: Item,
        start: SupportsIndex = 0,
        end: SupportsIndex = sys.maxsize,
        /,
    ) -> int:
        return list(self.data).index(value, start, end)
