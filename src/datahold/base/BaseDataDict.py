from __future__ import annotations

__all__: list[str] = ["BaseDataDict"]

from abc import abstractmethod
from collections.abc import Iterable
from typing import Optional, Self, TypeVar

import setdoc
from frozendict import frozendict

from ..typing.SupportsKeysAndGetitem import SupportsKeysAndGetitem
from .BaseDataMapping import BaseDataMapping

Key = TypeVar("Key", covariant=True)
Value = TypeVar("Value", covariant=True)
InitData = (
    SupportsKeysAndGetitem[Key | str, Optional[Value]]
    | Iterable[tuple[Key, Value]]
)


class BaseDataDict(BaseDataMapping[Key | str, Optional[Value]]):
    """Act as base class for dict-like implementation """ """which only has to override __fget__ and __fset__ to work immediately."""

    __slots__ = ()

    Data = frozendict

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> frozendict[Key | str, Optional[Value]]: ...

    @abstractmethod
    @setdoc.basic
    def __fset__(
        self: Self, data: frozenset[Key | str, Optional[Value]], /
    ) -> None: ...

    @setdoc.basic
    def __init__(
        self: Self,
        data: InitData[Key, Value] = (),
        /,
        **kwargs: Optional[Value],
    ) -> None:
        self.__fset__(frozendict(data, **kwargs))

    @setdoc.basic
    def __or__(
        self: Self, other: BaseDataDict[Key | str, Optional[Value]], /
    ) -> Self:
        return type(self)(self.__fget__() | frozendict(other))

    # __ror__ is not needed
    # because of how __or__ is defined

    @classmethod
    def fromkeys(
        self: Self, keys: Iterable[Key | str], value: Optional[Value] = None, /
    ) -> Self:
        return type(self)(frozendict.fromkeys(keys, value))
