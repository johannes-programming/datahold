"""Provide BaseHoldObject."""

__all__: list[str] = ["BaseHoldObject"]

from .BaseDataObject import BaseDataObject


class BaseHoldObject(BaseDataObject):
    __slots__ = ("_data",)
