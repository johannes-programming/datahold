"""Provide FrozenDataObject."""

__all__: list[str] = ["FrozenDataObject"]

from abc import abstractmethod
from collections.abc import Hashable
from typing import Final, Self

import setdoc

from ..base.BaseDataObject import BaseDataObject


class FrozenDataObject(BaseDataObject, Hashable):

    __slots__ = ()

    Data: Final[type[Hashable]] = Hashable  # type: ignore[type-abstract]

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.data)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Hashable: ...
