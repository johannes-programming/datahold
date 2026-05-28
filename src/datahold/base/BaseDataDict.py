from __future__ import annotations

from abc import abstractmethod
from collections.abc import (
    Hashable,
    ItemsView,
    Iterable,
    Iterator,
    KeysView,
    Mapping,
    ValuesView,
)
from typing import Optional, Self, TypeVar

import setdoc
from frozendict import frozendict

from ..typing.SupportsKeysAndGetitem import SupportsKeysAndGetitem
from .BaseDataCollection import BaseDataCollection

__all__ = ["BaseDataDict"]

Key = TypeVar("Key", bound=Hashable, covariant=True)
Value = TypeVar("Value", covariant=True)
Value_ = TypeVar("Value_")


class BaseDataDict(
    BaseDataCollection[Key | str], Mapping[Key | str, Optional[Value]]
):

    __slots__ = ()

    @setdoc.setdoc(dict.__getitem__.__doc__)
    def __getitem__(self: Self, key: Hashable, /) -> Optional[Value]:
        return self.data[key]  # type: ignore[index]

    @abstractmethod
    @setdoc.setdoc(dict.__init__.__doc__)
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
    def __or__(
        self: Self,
        other: BaseDataDict[Key, Value],
        /,
    ) -> Self:
        return type(self)(self.data | other.data)

    @setdoc.setdoc(dict.__repr__.__doc__)
    def __repr__(self: Self, /) -> str:
        return f"{type(self).__name__}({dict(self)})"

    @setdoc.setdoc(dict.__reversed__.__doc__)
    def __reversed__(self: Self, /) -> Iterator[Key | str]:
        return reversed(self.data)

    @property
    @abstractmethod
    def data(self: Self) -> frozendict[Key | str, Optional[Value]]: ...

    @classmethod
    @setdoc.setdoc(dict.fromkeys.__doc__)
    def fromkeys(
        cls: type[Self],
        iterable: Iterable[Key | str],
        value: Optional[Value] = None,
        /,
    ) -> Self:
        return cls(dict.fromkeys(iterable, value))

    @setdoc.setdoc(dict.get.__doc__)
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
        return dict(self.data).items()

    @setdoc.basic
    def keys(self: Self, /) -> KeysView[Key | str]:
        return dict(self.data).keys()

    @setdoc.basic
    def values(self: Self, /) -> ValuesView[Optional[Value]]:
        return dict(self.data).values()
