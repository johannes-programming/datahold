"""Provide BaseDataCollection."""

__all__ = ["BaseDataCollection"]

from abc import abstractmethod
from collections.abc import Collection, Hashable, Iterator
from typing import Self, TypeVar

import setdoc

from ..typing.HashableCollection import HashableCollection
from .BaseDataObject import BaseDataObject

Item = TypeVar("Item", covariant=True)


class BaseDataCollection(BaseDataObject, Collection[Item]):
    __slots__ = ()

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> HashableCollection[Item]: ...
