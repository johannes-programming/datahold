import collections
from typing import *

import setdoc
from frozendict import frozendict

from datahold.core.FrozenDataDict import FrozenDataDict
from datahold.core.FrozenHoldABC import FrozenHoldABC

__all__ = ["FrozenHoldDict"]

Key = TypeVar("Key")
Value = TypeVar("Value")


class FrozenHoldDict(
    FrozenHoldABC,
    FrozenDataDict[Key, Value],
    collections.abc.MutableMapping[Key, Value],
):

    __slots__ = ()

    data: frozendict[Key, Value]

    @setdoc.basic
    def __init__(self: Self, data: Any, /, **kwargs: Any) -> None:
        self._data = frozendict(data, **kwargs)
