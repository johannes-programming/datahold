"""Provide BaseHoldSet."""

__all__: list[str] = ["BaseHoldSet"]

from collections.abc import Hashable

from .BaseDataSet import BaseDataSet
from .BaseHoldObject import BaseHoldObject


class BaseHoldSet[Item: Hashable](BaseDataSet[Item], BaseHoldObject):
    """Provide an template for FrozenHoldSet and for HoldSet."""

    __slots__ = ()
