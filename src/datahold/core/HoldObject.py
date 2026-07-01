"""Provide HoldObject."""

__all__: list[str] = ["HoldObject"]

from ..base.BaseHoldObject import BaseHoldObject
from .DataObject import DataObject


class HoldObject(DataObject, BaseHoldObject):
    __slots__ = ()
