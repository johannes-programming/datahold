"""Provide BaseHoldCollection."""

__all__: list[str] = ["BaseHoldCollection"]

from .BaseDataCollection import BaseDataCollection


class BaseHoldCollection[Item](BaseDataCollection[Item]):
    """Provide abc for usable classes with slots."""

    __slots__ = ("_data",)
