"""Provide BaseDataSized."""

__all__ = ["BaseDataSized"]

from abc import abstractmethod
from collections.abc import Sized
from typing import Self, TypeVar

import setdoc

from ..typing.HashableSized import HashableSized
from .BaseDataObject import BaseDataObject

Item = TypeVar("Item", covariant=True)


class BaseDataSized(BaseDataObject, Sized):
    __slots__ = ()

    @setdoc.basic
    def __len__(self: Self, /) -> int:
        return len(self.data)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> HashableSized[Item]: ...
