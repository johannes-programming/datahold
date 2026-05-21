from typing import Any, Self, TypeVar

import setdoc
from frozendict import frozendict

from ..base.BaseHoldDict import BaseHoldDict
from .FrozenDataDict import FrozenDataDict
from .FrozenHoldObject import FrozenHoldObject

__all__ = ["FrozenHoldDict"]

Key = TypeVar("Key", covariant=True)
Value = TypeVar("Value", covariant=True)


class FrozenHoldDict(FrozenHoldObject, FrozenDataDict, BaseHoldDict[Key, Value]):

    __slots__ = ()

    @setdoc.basic
    def __init__(self: Self, data: Any, /, **kwargs: Value) -> None:
        self._data = frozendict(data, **kwargs)
