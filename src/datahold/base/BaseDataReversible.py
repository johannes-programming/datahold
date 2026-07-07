"""Provide BaseDataReversible."""

from __future__ import annotations

__all__: list[str] = ["BaseDataReversible"]

from abc import abstractmethod
from collections.abc import Iterator, Reversible
from typing import Self, TypeVar

import setdoc

from .BaseDataIterable import BaseDataIterable

Item = TypeVar("Item", covariant=True)


class BaseDataReversible(BaseDataIterable[Item], Reversible[Item]):
    __slots__ = ()

    class Data(Reversible[Item], BaseDataIterable.Data[Item]):  # type: ignore[misc, valid-type]
        """Provide hashable reversible protocol."""

    @setdoc.basic
    def __reversed__(self: Self, /) -> Iterator[Item]:
        return reversed(self.data)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data[Item]: ...
