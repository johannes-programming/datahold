"""Provide BaseDataCollection."""

from __future__ import annotations

__all__ = ["BaseDataCollection"]

from abc import abstractmethod
from collections.abc import Container, Hashable
from typing import Final, Protocol, Self

import setdoc

from .BaseDataObject import BaseDataObject


class Data(Container[Hashable], Protocol):
    """Provide hashable container protocol."""

    @setdoc.basic
    def __hash__(self: Self) -> int: ...


class BaseDataContainer(BaseDataObject, Container[Hashable]):
    __slots__ = ()

    Data: Final[type[Data]] = Data  # type: ignore[type-abstract]

    @setdoc.basic
    def __contains__(self: Self, other: Hashable, /) -> bool:
        return other in self.data  # type: ignore[attr-defined]

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data:  # type: ignore[valid-type]
        ...
