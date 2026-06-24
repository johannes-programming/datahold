"""Provide BaseHoldSet."""

__all__ = ["BaseHoldSet"]

from collections.abc import Hashable
from typing import TypeVar

from .BaseDataSet import BaseDataSet
from .BaseHoldObject import BaseHoldObject

Item = TypeVar("Item", bound=Hashable)


class BaseHoldSet(BaseHoldObject, BaseDataSet[Item]):
    __slots__ = ()
