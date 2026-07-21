"""Provide BaseHoldCollection."""

__all__: list[str] = ["BaseHoldCollection"]

from .BaseDataCollection import BaseDataCollection


class BaseHoldCollection[Item](BaseDataCollection[Item]):
    __slots__ = ("_data",)
