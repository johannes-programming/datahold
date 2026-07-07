"""Provide BaseDataDict."""

from __future__ import annotations

__all__ = ["BaseDataDict"]

from abc import abstractmethod
from collections.abc import Hashable, Iterable
from typing import Final, Optional, Self, TypeVar

import setdoc
from frozendict import frozendict

from .BaseDataMapping import BaseDataMapping

Key = TypeVar("Key", bound=Hashable, covariant=True)
Value = TypeVar("Value", covariant=True)


Data = frozendict[Key | str, Optional[Value]]


class BaseDataDict(BaseDataMapping[Key, Value]):

    __slots__ = ()

    Data: Final[type[Data]] = Data  # type: ignore[misc, type-arg]

    @setdoc.basic
    def __or__(
        self: Self,
        other: BaseDataDict[Key, Value],
        /,
    ) -> Self:
        return type(self)(self.data | other.data)  # type: ignore[operator]

    # __ror__ is unnecessary because of how __or__ is defined

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data[Key, Value]: ...  # type: ignore[valid-type]

    @classmethod
    @setdoc.basic
    def fromkeys(
        cls: type[Self],
        iterable: Iterable[Key | str],
        value: Optional[Value] = None,
        /,
    ) -> Self:
        return cls(dict.fromkeys(iterable, value))
