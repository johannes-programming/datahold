"""Provide BaseDataCollection."""

__all__ = ["BaseDataCollection"]

from abc import abstractmethod
from collections.abc import Collection, Hashable, Iterator
from typing import Final, Protocol, Self, TypeVar

import setdoc

from .BaseDataObject import BaseDataObject

Item = TypeVar("Item", covariant=True)


class Data(Collection[Item], Protocol[Item]):
    """Provide hashable collection protocol."""

    @setdoc.basic
    def __hash__(self: Self) -> int: ...


Data_ = Data


class BaseDataCollection(BaseDataObject, Collection[Item]):
    __slots__ = ()

    Data: Final[type[Data_]] = Data_  # type: ignore[type-abstract, type-arg]

    @setdoc.basic
    def __contains__(self: Self, other: Hashable, /) -> bool:
        return other in self.data

    @setdoc.basic
    def __iter__(self: Self, /) -> Iterator[Item]:
        return iter(self.data)

    @setdoc.basic
    def __len__(self: Self, /) -> int:
        return len(self.data)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data_[Item]: ...
