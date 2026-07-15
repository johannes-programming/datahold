from __future__ import annotations

__all__: list[str] = ["FrozenSlotDict"]
from typing import Optional, Self

import setdoc
from frozendict import frozendict

from ..base.BaseDataDict import BaseDataDict


class FrozenSlotDict[Key, Value](BaseDataDict[Key, Value]):
    """Act as frozen dict-like class."""

    __slots__ = ("_data",)

    type Data[DataKey, DataValue] = frozendict[
        DataKey | str, Optional[DataValue]
    ]

    @setdoc.basic
    def __data__(self: Self) -> Data[Key, Value]:
        return self.__data__()

    @setdoc.basic
    def __init__(
        self: Self,
        data: BaseDataDict.Init[Key, Value] = (),
        /,
        **kwargs: Optional[Value],
    ):
        self._data: FrozenSlotDict.Data[Key, Value] = frozendict(
            data, **kwargs
        )
