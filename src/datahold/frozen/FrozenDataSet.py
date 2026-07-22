"""Provide FrozenDataSet."""

__all__: list[str] = ["FrozenDataSet"]

from collections.abc import Hashable

from ..base.BaseDataSet import BaseDataSet
from .FrozenDataObject import FrozenDataObject


class FrozenDataSet[Item: Hashable](
    BaseDataSet[Item],
    FrozenDataObject,
):
    """Provide easy abc for custom frozen set-like."""

    __slots__ = ()

    __hash__ = FrozenDataObject.__hash__
