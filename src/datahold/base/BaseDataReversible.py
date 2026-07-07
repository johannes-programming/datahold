"""Provide BaseDataReversible."""

from __future__ import annotations

__all__ = ["BaseDataReversible"]

from abc import abstractmethod
from collections.abc import Iterator, Reversible
from typing import Final, Protocol, Self, TypeVar

import setdoc

from .BaseDataIterable import BaseDataIterable

Item = TypeVar("Item", covariant=True)


class Data(Reversible[Item], Protocol[Item]):
    """Provide hashable reversible protocol."""

    @setdoc.basic
    def __hash__(self: Self) -> int: ...


class BaseDataReversible(BaseDataIterable[Item], Reversible[Item]):
    __slots__ = ()

    Data: type[Data] = Data  # type: ignore[type-abstract, type-arg]

    @setdoc.basic
    def __reversed__(self: Self, /) -> Iterator[Item]:
        return reversed(self.data)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data[Item]:  # type: ignore[valid-type]
        ...
