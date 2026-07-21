"""Provide BaseDataDict."""

from __future__ import annotations

__all__ = ["BaseDataDict"]

from abc import abstractmethod
from collections.abc import Iterable
from typing import Optional, Self, Protocol, Never

import setdoc
from frozendict import frozendict

from .BaseDataMapping import BaseDataMapping




class SupportsKeysAndGetitem[Key, Value](Protocol[Key, Value]):

    @setdoc.basic
    def __getitem__(self: Self, key: Never, /) -> Value: ...

    @setdoc.basic
    def keys(self: Self) -> Iterable[Key]: ...


class BaseDataDict[Key, Value](
    BaseDataMapping[Key | str, Optional[Value]]
):
    
    # dict has rich cmp that always returns NotImplemented
    # should we add these here as well?

    __slots__ = ()

    type Data[DataKey, DataValue] = frozendict[DataKey | str, Optional[DataValue]]
    type Init[DataKey, DataValue] = (
        SupportsKeysAndGetitem[DataKey | str, Optional[DataValue]]
        | Iterable[tuple[DataKey | str, Optional[DataValue]]]
    )

    @abstractmethod
    @setdoc.basic
    def __init__(
        self: Self,
        data: Init[Key, Value] = (),
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

    @setdoc.basic
    def __repr__(self: Self, /) -> str:
        return f"{type(self).__name__}({dict(self)!r})"

    # __ror__ is unnecessary because of how __or__ is defined

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data[Key, Value]: ...

    @classmethod
    @setdoc.basic
    def fromkeys(
        cls: type[Self],
        iterable: Iterable[Key | str],
        value: Optional[Value] = None,
        /,
    ) -> Self:
        return cls(dict.fromkeys(iterable, value))
