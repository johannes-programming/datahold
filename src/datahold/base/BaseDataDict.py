"""Provide BaseDataDict."""

from __future__ import annotations

__all__ = ["BaseDataDict"]

from abc import abstractmethod
from collections.abc import Hashable, Iterable
from typing import Optional, Self, TypeVar

import setdoc
from frozendict import frozendict

from .BaseDataMapping import BaseDataMapping

Key = TypeVar("Key", bound=Hashable, covariant=True)
Value = TypeVar("Value", covariant=True)
Value_ = TypeVar("Value_")


class BaseDataDict(BaseDataMapping[Key, Value]):

    __slots__ = ()

    @setdoc.basic
    def __or__(
        self: Self,
        other: BaseDataDict[Key, Value],
        /,
    ) -> Self:
        return type(self)(self.data | other.data)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> frozendict[Key | str, Optional[Value]]: ...

    @classmethod
    @setdoc.basic
    def fromkeys(
        cls: type[Self],
        iterable: Iterable[Key | str],
        value: Optional[Value] = None,
        /,
    ) -> Self:
        return cls(dict.fromkeys(iterable, value))
