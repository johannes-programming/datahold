"""Provide DataDict."""

from __future__ import annotations

__all__: list[str] = ["DataDict"]

from abc import abstractmethod
from collections.abc import Hashable, MutableMapping
from typing import Optional, Self

import setdoc
from frozendict import frozendict

from ..base.BaseDataDict import BaseDataDict


class DataDict[Key: Hashable, Value](
    BaseDataDict[Key, Value],
    MutableMapping[Key | str, Optional[Value]],
):
    """Provide easy abc for custom mutable dict-like."""

    __slots__ = ()

    @setdoc.basic
    def __delitem__(self: Self, key: Key | str, /) -> None:
        self.__fset__(self.__fget__().delete(key))

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> DataDict.Data[Key, Value]: ...

    @abstractmethod
    @setdoc.basic
    def __fset__(self: Self, data: DataDict.Data[Key, Value], /) -> None: ...

    @setdoc.basic
    def __init__(
        self: Self,
        data: BaseDataDict.Init[Key, Value] = (),
        /,
        **kwargs: Optional[Value],
    ) -> None:
        self.__fset__(frozendict(data, **kwargs))  # type: ignore[arg-type]

    @setdoc.basic
    def __ior__(
        self: Self,
        other: BaseDataDict[Key, Value],
        /,
    ) -> Self:
        self.__fset__(self.__fget__() | other.__fget__())
        return self

    @setdoc.basic
    def __setitem__(
        self: Self,
        key: Key | str,
        value: Optional[Value],
        /,
    ) -> None:
        # what to do if Key includes unhashable types?
        self.__fset__(self.__fget__().set(key, value))

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self)
