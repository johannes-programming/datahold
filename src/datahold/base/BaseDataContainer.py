"""Provide BaseDataContainer."""

__all__ = ["BaseDataContainer"]

from abc import abstractmethod
from collections.abc import Container, Hashable
from typing import Protocol, Self, TypeVar, runtime_checkable

import setdoc

from .BaseDataObject import BaseDataObject

Item = TypeVar("Item", covariant=True)


class BaseDataContainer(BaseDataObject, Container[Hashable]):
    __slots__ = ()

    @runtime_checkable
    class Data(BaseDataObject.Data, Container[Hashable], Protocol): ...

    @setdoc.basic
    def __contains__(self: Self, other: Hashable, /) -> bool:
        return other in self.data

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data: ...
