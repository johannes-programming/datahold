from __future__ import annotations

__all__: list[str] = ["DataMapping"]
from collections.abc import Hashable, MutableMapping
from typing import Optional, Self, Protocol

import setdoc
from abc import abstractmethod

from ..base.BaseDataMapping import BaseDataMapping


class DataMapping[Key, Value](
    BaseDataMapping[Key | str, Optional[Value]],
    MutableMapping[Key | str, Optional[Value]],
):
    """Act as base class for mutable mapping implementation which only has to override __data__ to work immediately."""

    __slots__ = ()

    @setdoc.basic
    class Data[DataKey, DataValue](
        BaseDataMapping.Data[DataKey | str, Optional[DataValue]], 
        Protocol[DataKey, DataValue],
    ):
        @setdoc.basic
        def __delitem__(self:Self, key: Hashable) -> None:
            ...
        @setdoc.basic
        def __setitem__(self:Self, key: DataKey, value: DataValue) -> None:
            ...
    
    @abstractmethod
    @setdoc.basic
    def __data__(self:Self) -> Data[Key, Value]:
        ...


    @setdoc.basic
    def __delitem__(self: Self, key: Hashable, /) -> None:
        del self.__data__()[key]

    @setdoc.basic
    def __setitem__(
        self: Self, key: Key | str, value: Optional[Value]
    ) -> None:
        self.__data__()[key] = value
