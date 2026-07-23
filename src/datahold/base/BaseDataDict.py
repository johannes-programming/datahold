"""Provide BaseDataDict."""

from __future__ import annotations

__all__: list[str] = ["BaseDataDict"]

from abc import abstractmethod
from collections import abc
from typing import Never, Optional, Protocol, Self

import setdoc
from frozendict import frozendict

from .BaseDataMapping import BaseDataMapping


class SupportsKeysAndGetitem[Key, Value](Protocol):

    @setdoc.basic
    def __getitem__(self: Self, key: Never, /) -> Value: ...

    @setdoc.basic
    def keys(self: Self) -> abc.Iterable[Key]: ...


class BaseDataDict[Key: abc.Hashable, Value](
    BaseDataMapping[Key | str, Optional[Value]],
):
    """Provide an easy abc for custom dict-like."""

    __slots__ = ()

    type Data[DataKey, DataValue] = frozendict[
        DataKey | str, Optional[DataValue]
    ]
    type Init[DataKey, DataValue] = (
        SupportsKeysAndGetitem[DataKey | str, Optional[DataValue]]
        | abc.Iterable[tuple[DataKey | str, Optional[DataValue]]]
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
        return type(self)(self.__fget__() | other.__fget__())

    @setdoc.basic
    def __repr__(self: Self, /) -> str:
        return f"{type(self).__name__}({dict(self)!r})"

    # __ror__ is unnecessary because of how __or__ is defined

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> Data[Key, Value]: ...

    @classmethod
    @setdoc.basic
    def fromkeys(
        cls: type[Self],
        iterable: abc.Iterable[Key | str],
        value: Optional[Value] = None,
        /,
    ) -> Self:
        return cls(dict.fromkeys(iterable, value))
