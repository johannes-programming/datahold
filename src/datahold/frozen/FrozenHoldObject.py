"""Provide FrozenHoldObject."""

__all__ = ["FrozenHoldObject"]

from typing import Any, Self

from ..base.BaseHoldObject import BaseHoldObject
from .FrozenDataObject import FrozenDataObject


class FrozenHoldObject(FrozenDataObject, BaseHoldObject):

    _data: Any
    __slots__ = ()

    @property
    def data(self: Self) -> Any:
        return self._data
