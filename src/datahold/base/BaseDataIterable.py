"""Provide BaseDataIterable."""

__all__ = ["BaseDataIterable"]

from abc import abstractmethod
from collections.abc import Iterable, Iterator
from typing import Self, TypeVar

import setdoc

from ..typing.HashableIterable import HashableIterable
from .BaseDataObject import BaseDataObject

Item = TypeVar("Item", covariant=True)


class BaseDataIterable(BaseDataObject, Iterable[Item]):
    __slots__ = ()

    @setdoc.basic
    def __iter__(self: Self, /) -> Iterator[Item]:
        return iter(self.data)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> HashableIterable[Item]: ...
