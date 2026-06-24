"""Provide FrozenDataSet."""

from collections.abc import Hashable
from typing import TypeVar

from ..base.BaseDataSet import BaseDataSet
from .FrozenDataObject import FrozenDataObject

__all__ = ["FrozenDataSet"]

Item = TypeVar("Item", bound=Hashable, covariant=True)


class FrozenDataSet(FrozenDataObject, BaseDataSet[Item]):

    __slots__ = ()
