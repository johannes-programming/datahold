"""Provide BaseDataMapping."""

from __future__ import annotations

__all__: list[str] = ["BaseDataMapping"]

from abc import abstractmethod
from collections.abc import Mapping
from typing import Never, Protocol, Self

import setdoc

from .BaseDataCollection import BaseDataCollection


class BaseDataMapping[Key, Value](
    BaseDataCollection[Key], Mapping[Key, Value]
):
    """Provide an easy abc for a custom mapping."""

    __slots__ = ()

    @setdoc.basic
    class Data[DataKey, DataValue](
        BaseDataCollection.Data[DataKey],
        Protocol,
    ):
        @setdoc.basic
        def __getitem__(self: Self, key: Never, /) -> DataValue:
            pass

    @setdoc.basic
    def __getitem__(self: Self, key: object, /) -> Value:
        try:
            return self.__fget__()[key]  # type: ignore[index]
        except TypeError:
            raise KeyError(key) from None

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> Data[Key, Value]: ...
