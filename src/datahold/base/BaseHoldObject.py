"""Provide BaseHoldObject."""

__all__ = ["BaseHoldObject"]

from .BaseDataObject import BaseDataObject


class BaseHoldObject(BaseDataObject):
    __slots__ = ("_data",)
