"""Provide FrozenDataDict."""

__all__: list[str] = ["FrozenDataDict"]

from collections.abc import Hashable

from ..base.BaseDataDict import BaseDataDict
from .FrozenDataObject import FrozenDataObject


class FrozenDataDict[Key: Hashable, Value](
    BaseDataDict[Key, Value],
    FrozenDataObject,
):
    """Provide easy abc for custom frozen dict-like."""

    __slots__ = ()

    __hash__ = FrozenDataObject.__hash__
