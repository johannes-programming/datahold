"""Provide BaseHoldSet."""

__all__: list[str] = ["BaseHoldSet"]

from collections.abc import Hashable
from typing import TypeVar

from .BaseDataSet import BaseDataSet
from .BaseHoldObject import BaseHoldObject

Item = TypeVar("Item", bound=Hashable)


class BaseHoldSet(BaseDataSet[Item], BaseHoldObject):
    __slots__ = ()
