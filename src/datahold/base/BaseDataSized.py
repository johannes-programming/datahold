"""Provide BaseDataSized."""

from __future__ import annotations

__all__ = ["BaseDataSized"]

from abc import abstractmethod
from collections.abc import Sized
from typing import Final, Protocol, Self, TypeVar

import setdoc

from .BaseDataObject import BaseDataObject

Item = TypeVar("Item", covariant=True)


class Data(Sized, Protocol[Item]):
    """Provide hashable sized protocol."""

    @setdoc.basic
    def __hash__(self: Self) -> int: ...


class BaseDataSized(BaseDataObject, Sized):
    __slots__ = ()

    Data: Final[type[Data]] = Data  # type: ignore[type-abstract, type-arg]

    @setdoc.basic
    def __len__(self: Self, /) -> int:
        return len(self.data)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data:  # type: ignore[valid-type]
        ...
