"""Provide DataDict."""

__all__ = ["DataDict"]

from abc import abstractmethod
from collections.abc import Hashable, Iterable, MutableMapping
from typing import Optional, Self, TypeVar, overload

import setdoc
from frozendict import frozendict

from .._utils.Missing import Missing
from ..base.BaseDataDict import BaseDataDict
from ..typing.SupportsKeysAndGetitem import SupportsKeysAndGetitem
from .DataObject import DataObject

Key = TypeVar("Key", bound=Hashable)
Value = TypeVar("Value")
Value_ = TypeVar("Value_")


class DataDict(
    DataObject,
    BaseDataDict[Key, Value],
    MutableMapping[Key | str, Optional[Value]],
):
    __slots__ = ()

    @setdoc.basic
    def __delitem__(self: Self, key: Hashable, /) -> None:
        self.data = self.data.delete(key)  # type: ignore[arg-type]

    @setdoc.basic
    def __init__(
        self: Self,
        data: (
            SupportsKeysAndGetitem[Key | str, Optional[Value]]
            | Iterable[tuple[Key | str, Optional[Value]]]
        ) = (),
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
        self.data = self.data.set(key, value)

    @setdoc.basic
    def clear(self: Self, /) -> None:
        self.data = frozendict()

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> frozendict[Key | str, Optional[Value]]: ...

    @data.setter
    @abstractmethod
    @setdoc.basic
    def data(
        self: Self,
        value: (
            SupportsKeysAndGetitem[Key | str, Optional[Value]]
            | Iterable[tuple[Key | str, Optional[Value]]]
        ),
    ) -> None: ...

    @overload
    @setdoc.basic
    def pop(self: Self, key: Hashable, /) -> Optional[Value]: ...

    @overload
    @setdoc.basic
    def pop(
        self: Self,
        key: Hashable,
        default: Value_,
        /,
    ) -> Optional[Value | Value_]: ...

    @setdoc.basic
    def pop(
        self: Self,
        key: Hashable,
        default: Missing | Value_ = Missing.missing,
        /,
    ) -> Optional[Value | Value_]:
        ans: Optional[Value | Value_]
        data: dict[Key | str, Optional[Value]]
        data = dict(self.data)
        if isinstance(default, Missing):
            ans = data.pop(key)  # type: ignore[arg-type]
        else:
            ans = data.pop(key, default)  # type: ignore[arg-type]
        self.data = frozendict(data)
        return ans

    @setdoc.basic
    def popitem(self: Self, /) -> tuple[Key | str, Optional[Value]]:
        ans: tuple[Key | str, Optional[Value]]
        data: dict[Key | str, Optional[Value]]
        data = dict(self.data)
        ans = data.popitem()
        self.data = frozendict(data)
        return ans

    @setdoc.basic
    def setdefault(
        self: Self,
        key: Key | str,
        default: Optional[Value] = None,
        /,
    ) -> Optional[Value]:
        ans: Optional[Value]
        data: dict[Key | str, Optional[Value]]
        data = dict(self.data)
        ans = data.setdefault(key, default)
        self.data = frozendict(data)
        return ans

    @setdoc.basic
    def update(
        self: Self,
        other: (
            SupportsKeysAndGetitem[Key | str, Optional[Value]]
            | Iterable[tuple[Key | str, Optional[Value]]]
        ) = (),
        /,
        **kwargs: Optional[Value],
    ) -> None:
        data: dict[Key | str, Optional[Value]]
        data = dict(self.data)
        data.update(other, **kwargs)
        self.data = frozendict(data)
