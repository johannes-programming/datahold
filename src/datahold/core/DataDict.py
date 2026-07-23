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
        self.data = self.data.delete(key)

    @setdoc.basic
    def __init__(
        self: Self,
        data: BaseDataDict.Init[Key, Value] = (),
        /,
        **kwargs: Optional[Value],
    ) -> None:
        self.data = frozendict(data, **kwargs)  # type: ignore[arg-type]

    @setdoc.basic
    def __ior__(
        self: Self,
        other: BaseDataDict[Key, Value],
        /,
    ) -> Self:
        self.data |= other.data
        return self

    @setdoc.basic
    def __setitem__(
        self: Self,
        key: Key | str,
        value: Optional[Value],
        /,
    ) -> None:
        # what to do if Key includes unhashable types?
        self.data = self.data.set(key, value)

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> DataDict.Data[Key, Value]: ...

    @data.setter
    @abstractmethod
    @setdoc.basic
    def data(self: Self, value: DataDict.Init[Key, Value]) -> None: ...
