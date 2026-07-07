"""Provide BaseDataCollection."""

from __future__ import annotations

__all__ = ["BaseDataCollection"]

from abc import abstractmethod
from collections.abc import Collection, Hashable
from typing import Final, Protocol, Self, TypeVar

import setdoc

from .BaseDataIterable import BaseDataIterable

Item = TypeVar("Item", covariant=True)


class Data(Collection[Item], Protocol[Item]):
    """Provide hashable collection protocol."""

    @setdoc.basic
    def __hash__(self: Self) -> int: ...


class BaseDataCollection(BaseDataIterable[Item], Collection[Item]):
    __slots__ = ()

    Data: Final[type[Data]] = Data  # type: ignore[type-abstract, type-arg]

    @setdoc.basic
    def __contains__(self: Self, other: Hashable, /) -> bool:
        return other in self.data

    @setdoc.basic
    def __len__(self: Self, /) -> int:
        return len(self.data)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data[Item]: ...
