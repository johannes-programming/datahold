from abc import abstractmethod
from collections.abc import Collection, Iterator
from typing import Self, TypeVar

import setdoc

from ..typing.HashableCollection import HashableCollection
from .BaseDataObject import BaseDataObject

__all__ = ["BaseDataCollection"]

Item = TypeVar("Item", covariant=True)


class BaseDataCollection(BaseDataObject, Collection[Item]):
    __slots__ = ()

    @setdoc.basic
    def __contains__(self: Self, other: object, /) -> bool:
        return other in self.data

    @setdoc.basic
    def __iter__(self: Self, /) -> Iterator[Item]:
        return iter(self.data)

    @setdoc.basic
    def __len__(self: Self, /) -> int:
        return len(self.data)

    @property
    @abstractmethod
    def data(self: Self) -> HashableCollection[Item]: ...
