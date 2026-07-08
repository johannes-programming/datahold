"""Provide BaseDataSized."""

__all__ = ["BaseDataSized"]

from abc import abstractmethod
from collections.abc import Sized
from typing import Protocol, Self, TypeVar, runtime_checkable

import setdoc

from .BaseDataObject import BaseDataObject

Item = TypeVar("Item", covariant=True)


class BaseDataSized(BaseDataObject, Sized):
    __slots__ = ()

    @runtime_checkable
    class Data(BaseDataObject.Data, Sized, Protocol): ...

    @setdoc.basic
    def __len__(self: Self, /) -> int:
        return len(self.data)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data: ...
