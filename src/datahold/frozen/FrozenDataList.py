"""Provide FrozenDataList."""

__all__: list[str] = ["FrozenDataList"]

from ..base.BaseDataList import BaseDataList
from .FrozenDataObject import FrozenDataObject


class FrozenDataList[Item](
    BaseDataList[Item],
    FrozenDataObject,
):
    """Provide easy abc for custom frozen list-like."""

    __slots__ = ()

    __hash__ = FrozenDataObject.__hash__
