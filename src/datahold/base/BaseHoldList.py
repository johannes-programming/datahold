"""Provide BaseHoldList."""

__all__: list[str] = ["BaseHoldList"]

from typing import TypeVar

from .BaseDataList import BaseDataList
from .BaseHoldObject import BaseHoldObject

Item = TypeVar("Item", covariant=True)


class BaseHoldList(BaseHoldObject, BaseDataList[Item]):
    __slots__ = ()