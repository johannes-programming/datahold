"""Provide FrozenDataList."""

from typing import TypeVar

from ..base.BaseDataList import BaseDataList
from .FrozenDataObject import FrozenDataObject

__all__ = ["FrozenDataList"]

Item = TypeVar("Item", covariant=True)


class FrozenDataList(FrozenDataObject, BaseDataList[Item]):

    __slots__ = ()
