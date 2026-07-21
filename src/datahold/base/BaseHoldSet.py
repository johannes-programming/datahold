"""Provide BaseHoldSet."""

__all__: list[str] = ["BaseHoldSet"]

from .BaseDataSet import BaseDataSet
from .BaseHoldCollection import BaseHoldCollection



class BaseHoldSet[Item](BaseDataSet[Item], BaseHoldCollection[Item]):
    __slots__ = ()
