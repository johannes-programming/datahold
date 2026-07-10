"""Provide FrozenDataObject."""

__all__: list[str] = ["FrozenDataObject"]

from collections.abc import Hashable
from typing import Self

import setdoc

from ..base.BaseDataObject import BaseDataObject


class FrozenDataObject(BaseDataObject, Hashable):

    __slots__ = ()

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.data)
