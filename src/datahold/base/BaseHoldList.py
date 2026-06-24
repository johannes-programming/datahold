"""Provide BaseHoldList."""

from typing import TypeVar

from .BaseDataList import BaseDataList
from .BaseHoldObject import BaseHoldObject

__all__ = ["BaseHoldList"]

Item = TypeVar("Item", covariant=True)


class BaseHoldList(BaseHoldObject, BaseDataList[Item]):
    __slots__ = ()
