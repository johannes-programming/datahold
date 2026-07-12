from __future__ import annotations

__all__: list[str] = ["BaseDataDict"]

from typing import TypeVar, Self, Optional
from .BaseDataMapping import BaseDataMapping
from .BaseDataFgettable import BaseDataFgettable
from collections.abc import Iterable
from ..typing.SupportsKeysAndGetitem import SupportsKeysAndGetitem
import setdoc
from frozendict import frozendict

Key = TypeVar("Key", covariant=True)
Value = TypeVar("Value", covariant=True)


class BaseDataDict(BaseDataMapping[Key | str, Optional[Value]]):

    __slots__ = ()

    Data = frozendict

    __fget__ = BaseDataFgettable[frozendict[Key | str, Optional[Value]]].__fget__

    @setdoc.basic
    def __init__(
        self:Self, 
        data:SupportsKeysAndGetitem[Key|str, Optional[Value]]|Iterable[tuple[Key, Value]] = (), 
        /, 
        **kwargs: Optional[Value],
    ) -> None:
        self.__fset__(frozendict(data, **kwargs))

    @setdoc.basic
    def __or__(self:Self, other:BaseDataDict[Key|str, Optional[Value]], /) -> Self:
        return type(self)(self.__fget__() | frozendict(other))
    
    # __ror__ is not needed
    # because of how __or__ is defined

    @classmethod
    def fromkeys(self: Self, keys:Iterable[Key|str], value:Optional[Value]=None, /)->Self:
        return type(self)(frozendict.fromkeys(keys,value))