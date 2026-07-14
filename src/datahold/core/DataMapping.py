

from __future__ import annotations

__all__: list[str] = ["DataMapping"]
from ..base.BaseDataMapping import BaseDataMapping
from collections.abc import (
    Hashable,
    MutableMapping,
)
from typing import Self, TypeVar, Optional

import setdoc

Key = TypeVar("Key")
Value = TypeVar("Value")


class DataMapping(  # type: ignore[type-var]
    BaseDataMapping[Key|str, Optional[Value]],
    MutableMapping[Key|str, Optional[Value]],
):
    """Act as a base class for concrete mutable mapping backed by a data attribute."""

    # this abc exists to provide the easiest possible template for a MutableMapping
    # a subclass must only override __fget__ and __fset__
    # and it is immediately non-abstract

    __slots__ = ()

    @setdoc.basic
    def __delitem__(self:Self, key:Hashable, /)->None:
        data:dict[Key|str, Optional[Value]]
        data = dict(self.__fget__())
        del data[key]
        self.__fset__(data)
    
    @setdoc.basic
    def __setitem__(self:Self, key:Key, value:Value)->None:
        data:dict[Key|str, Optional[Value]]
        data = dict(self.__fget__())
        data[key] = value
        self.__fset__(data)



