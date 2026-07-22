# change into BaseHoldCollection in v4.0
"""Provide BaseHoldObject."""

__all__: list[str] = ["BaseHoldObject"]

from .BaseDataObject import BaseDataObject


class BaseHoldObject(BaseDataObject):
    """Provide abc with slot layout."""

    __slots__ = ("_data",)
