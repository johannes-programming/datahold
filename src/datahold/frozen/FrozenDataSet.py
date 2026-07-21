"""Provide FrozenDataSet."""

__all__: list[str] = ["FrozenDataSet"]


from ..base.BaseDataSet import BaseDataSet
from .FrozenDataCollection import FrozenDataCollection


class FrozenDataSet[Item](BaseDataSet[Item], FrozenDataCollection[Item]):

    __slots__ = ()
