"""Provide BaseDataMapping."""

from __future__ import annotations

__all__ = ["BaseDataMapping"]

from abc import abstractmethod
from collections.abc import Mapping
from typing import Never, Optional, Protocol, Self

import setdoc

from .BaseDataCollection import BaseDataCollection


class BaseDataMapping[Key, Value](
    BaseDataCollection[Key | str], Mapping[Key | str, Optional[Value]]
):

    __slots__ = ()

    class Data[DataKey, DataValue](
        BaseDataCollection.Data[DataKey],
        Protocol,
    ):
        @setdoc.basic
        def __getitem__(self: Self, key: Never, /) -> DataValue:
            pass

    @setdoc.basic
    def __getitem__(self: Self, key: object, /) -> Optional[Value]:
        try:
            return self.data[key]
        except TypeError:
            raise KeyError(key) from None

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data[Key, Value]: ...
