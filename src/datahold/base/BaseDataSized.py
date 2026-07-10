"""Provide BaseDataSized."""

__all__ = ["BaseDataSized"]

from abc import abstractmethod
from collections.abc import Sized
from typing import Protocol, Self, TypeVar

import setdoc

from .BaseDataObject import BaseDataObject

DataItem = TypeVar("DataItem", covariant=True)
Item = TypeVar("Item", covariant=True)


class BaseDataSized(BaseDataObject, Sized):
    __slots__ = ()

    class Data(
        BaseDataObject.Data,
        Sized,
        Protocol,
    ):
        """Provide sized data protocol."""

    @setdoc.basic
    def __len__(self: Self, /) -> int:
        return len(self.data)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data: ...
