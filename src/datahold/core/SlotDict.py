from __future__ import annotations

__all__: list[str] = ["SlotDict"]
from typing import Optional, Self

import setdoc

from .DataDict import DataDict


class SlotDict[Key, Value](DataDict[Key, Value]):
    """Act as dict-like class."""

    __slots__ = ("_data",)

    type Data[DataKey, DataValue] = dict[DataKey | str, Optional[DataValue]]

    @setdoc.basic
    def __data__(self: Self) -> Data[Key, Value]:
        return self._data

    @setdoc.basic
    def __init__(
        self: Self,
        data: DataDict.Init[Key, Value] = (),
        /,
        **kwargs: Optional[Value],
    ) -> None:
        self._data: SlotDict.Data[Key, Value] = dict(data, **kwargs)
