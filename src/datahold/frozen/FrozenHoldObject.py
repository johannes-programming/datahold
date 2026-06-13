from typing import Any, Self

from ..base.BaseHoldObject import BaseHoldObject
from .FrozenDataObject import FrozenDataObject

__all__ = ["FrozenHoldObject"]


class FrozenHoldObject(FrozenDataObject, BaseHoldObject):

    _data: Any
    __slots__ = ()

    @property
    def data(self: Self) -> Any:
        return self._data
