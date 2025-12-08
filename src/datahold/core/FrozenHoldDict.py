import collections
from typing import *

import setdoc
from frozendict import frozendict

from datahold.core.FrozenDataDict import FrozenDataDict
from datahold.core.FrozenHoldBase import FrozenHoldBase

__all__ = ["FrozenHoldDict"]

Key = TypeVar("Key")
Value = TypeVar("Value")


class FrozenHoldDict(
    FrozenHoldBase,
    FrozenDataDict[Key, Value],
):

    __slots__ = ()

    data: frozendict[Key, Value]

    @setdoc.basic
    def __init__(self: Self, data: Any, /, **kwargs: Any) -> None:
        self._data = frozendict(data, **kwargs)
