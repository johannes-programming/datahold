"""Provide FrozenDataList."""

__all__: list[str] = ["FrozenDataList"]

from ..base.BaseDataList import BaseDataList
from .FrozenDataCollection import FrozenDataCollection


class FrozenDataList[Item](
    BaseDataList[Item], 
    FrozenDataCollection[Item],
):

    __slots__ = ()
