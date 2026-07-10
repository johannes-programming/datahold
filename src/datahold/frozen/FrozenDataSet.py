"""Provide FrozenDataSet."""

__all__: list[str] = ["FrozenDataSet"]

from collections.abc import Hashable
from typing import TypeVar

from ..base.BaseDataSet import BaseDataSet
from .FrozenDataObject import FrozenDataObject

Item = TypeVar("Item", bound=Hashable, covariant=True)


class FrozenDataSet(BaseDataSet[Item], FrozenDataObject):

    __slots__ = ()
