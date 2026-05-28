import typing

from .BaseDataList import BaseDataList
from .BaseHoldObject import BaseHoldObject

__all__ = ["BaseHoldList"]

Item = typing.TypeVar("Item", covariant=True)


class BaseHoldList(BaseHoldObject, BaseDataList[Item]):
    __slots__ = ()
