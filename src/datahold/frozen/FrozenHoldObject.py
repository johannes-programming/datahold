"""Provide FrozenHoldObject."""

__all__: list[str] = ["FrozenHoldObject"]

from collections.abc import Hashable
from typing import Self

import setdoc

from ..base.BaseHoldObject import BaseHoldObject
from .FrozenDataObject import FrozenDataObject

# do we really need this class/this file?
# consider removal 
class FrozenHoldObject(FrozenDataObject, BaseHoldObject):

    _data: Hashable
    __slots__ = ()

    @property
    @setdoc.basic
    def data(self: Self) -> Hashable:
        return self._data
