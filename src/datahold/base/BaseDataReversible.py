"""Provide BaseDataList."""

from __future__ import annotations

__all__: list[str] = ["BaseDataReversible"]

from abc import abstractmethod
from collections.abc import Iterator, Reversible
from typing import Final, Self, TypeVar

import setdoc

from .BaseDataIterable import BaseDataIterable

Item = TypeVar("Item", covariant=True)


class BaseDataReversible(BaseDataIterable, Reversible[Item]):
    __slots__ = ()

    Data: Final[type[Reversible]] = Reversible  # type: ignore[type-abstract, type-arg]

    @setdoc.basic
    def __reversed__(self: Self, /) -> Iterator[Item]:
        return reversed(self.data)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Reversible[Item]: ...
