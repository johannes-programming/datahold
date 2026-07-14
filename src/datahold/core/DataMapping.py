from __future__ import annotations

__all__: list[str] = ["DataMapping"]
from collections.abc import Hashable, MutableMapping
from typing import Optional, Self, TypeVar

import setdoc

from ..base.BaseDataMapping import BaseDataMapping

Key = TypeVar("Key")
Value = TypeVar("Value")


class DataMapping(  
    BaseDataMapping[Key | str, Optional[Value]],
    MutableMapping[Key | str, Optional[Value]],
):
    """Act as base class for mutable mapping implementation which only has to override __fget__ and __fset__ to work immediately."""

    __slots__ = ()

    @setdoc.basic
    def __delitem__(self: Self, key: Hashable, /) -> None:
        data: dict[Key | str, Optional[Value]]
        data = dict(self.__fget__())
        del data[key]
        self.__fset__(data)

    @setdoc.basic
    def __setitem__(self: Self, key: Key, value: Value) -> None:
        data: dict[Key | str, Optional[Value]]
        data = dict(self.__fget__())
        data[key] = value
        self.__fset__(data)
