"""Provide BaseDataContainer."""

__all__ = ["BaseDataContainer"]

from abc import abstractmethod
from collections.abc import Hashable, Container
from typing import Self, TypeVar

import setdoc

from ..typing.HashableContainer import HashableContainer
from .BaseDataObject import BaseDataObject

Item = TypeVar("Item", covariant=True)


class BaseDataContainer(BaseDataObject, Container[Item]):
    __slots__ = ()

    @setdoc.basic
    def __contains__(self: Self, other: Hashable, /) -> bool:
        return other in self.data

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> HashableContainer[Item]: ...
