"""Provide BaseDataMapping."""

from __future__ import annotations

__all__ = ["BaseDataMapping"]

from abc import abstractmethod
from collections.abc import (
    Hashable,
    ItemsView,
    Iterable,
    KeysView,
    Mapping,
    ValuesView,
)
from typing import Optional, Self, TypeVar

import setdoc

from ..typing.SupportsKeysAndGetitem import SupportsKeysAndGetitem
from .BaseDataCollection import BaseDataCollection

Key = TypeVar("Key", bound=Hashable, covariant=True)
Value = TypeVar("Value", covariant=True)
Value_ = TypeVar("Value_")


class BaseDataMapping(
    BaseDataCollection[Key | str], Mapping[Key | str, Optional[Value]]
):

    __slots__ = ()

    @setdoc.basic
    def __getitem__(self: Self, key: Hashable, /) -> Optional[Value]:
        return self.data[key]  # type: ignore[index]

    @abstractmethod
    @setdoc.basic
    def __init__(
        self: Self,
        data: (
            SupportsKeysAndGetitem[Key | str, Optional[Value]]
            | Iterable[tuple[Key | str, Optional[Value]]]
        ) = (),
        /,
        **kwargs: Optional[Value],
    ) -> None: ...

    @setdoc.basic
    def __repr__(self: Self, /) -> str:
        return f"{type(self).__name__}({dict(self)!r})"

    # Mapping already defines: __reversed__ = None

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Mapping[Key | str, Optional[Value]]: ...

    @setdoc.basic
    def get(
        self: Self,
        key: Hashable,
        default: Optional[Value_] = None,
        /,
    ) -> Optional[Value | Value_]:
        return self.data.get(key, default)  # type: ignore[arg-type]

    @setdoc.basic
    def items(
        self: Self,
        /,
    ) -> ItemsView[Key | str, Optional[Value]]:
        return ItemsView(self)

    @setdoc.basic
    def keys(self: Self, /) -> KeysView[Key | str]:
        return KeysView(self)

    @setdoc.basic
    def values(self: Self, /) -> ValuesView[Optional[Value]]:
        return ValuesView(self)
