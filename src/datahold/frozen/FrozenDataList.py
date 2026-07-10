"""Provide FrozenDataList."""

__all__: list[str] = ["FrozenDataList"]

from typing import TypeVar

from ..base.BaseDataList import BaseDataList
from .FrozenDataObject import FrozenDataObject

Item = TypeVar("Item", covariant=True)


class FrozenDataList(BaseDataList[Item], FrozenDataObject):

    __slots__ = ()
