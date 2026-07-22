"""Provide BaseHoldDict."""

__all__: list[str] = ["BaseHoldDict"]

from collections.abc import Hashable

from .BaseDataDict import BaseDataDict
from .BaseHoldObject import BaseHoldObject


class BaseHoldDict[Key: Hashable, Value](
    BaseDataDict[Key, Value], BaseHoldObject
):
    """Provide an template for FrozenHoldDict and for HoldDict."""

    __slots__ = ()
