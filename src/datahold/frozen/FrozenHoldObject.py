"""Provide FrozenHoldObject."""

__all__ = ["FrozenHoldObject"]

from typing import Any, Self

import setdoc

from ..base.BaseHoldObject import BaseHoldObject
from .FrozenDataObject import FrozenDataObject


class FrozenHoldObject(FrozenDataObject, BaseHoldObject):

    _data: Any
    __slots__ = ()

    @property
    @setdoc.basic
    def data(self: Self) -> Any:
        return self._data
