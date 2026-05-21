

from ..base.BaseHoldObject import BaseHoldObject
from .DataObject import DataObject

__all__ = ["HoldObject"]


class HoldObject(DataObject, BaseHoldObject):
    __slots__ = ()
