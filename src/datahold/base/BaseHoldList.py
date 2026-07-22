"""Provide BaseHoldList."""

__all__: list[str] = ["BaseHoldList"]

from .BaseDataList import BaseDataList
from .BaseHoldObject import BaseHoldObject


class BaseHoldList[Item](BaseDataList[Item], BaseHoldObject):
    """Provide an template for FrozenHoldList and for HoldList."""

    __slots__ = ()
