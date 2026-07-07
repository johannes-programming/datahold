"""Provide BaseDataCollection."""

from __future__ import annotations

__all__ = ["BaseDataIterable"]

from abc import abstractmethod
from collections.abc import Iterable, Iterator
from typing import Protocol, Self, TypeVar

import setdoc

from .BaseDataObject import BaseDataObject

Item = TypeVar("Item", covariant=True)


class BaseDataIterable(BaseDataObject, Iterable[Item]):
    __slots__ = ()

    class Data(
        BaseDataObject.Data,  # type: ignore[misc, valid-type]
        Iterable[Item],
        Protocol[Item],
    ):
        """Provide hashable iterable protocol."""

    @setdoc.basic
    def __iter__(self: Self, /) -> Iterator[Item]:
        return iter(self.data)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data[Item]:  # type: ignore[valid-type]
        ...
