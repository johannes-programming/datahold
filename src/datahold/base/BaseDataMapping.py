from __future__ import annotations

__all__: list[str] = ["BaseDataMapping"]
from collections.abc import Hashable, Mapping
from typing import Protocol, Self, TypeVar

import setdoc

from .BaseDataCollection import BaseDataCollection
from .BaseDataFgettable import BaseDataFgettable

DataKey = TypeVar("DataKey", covariant=True)
DataValue = TypeVar("DataValue", covariant=True)
Key = TypeVar("Key", covariant=True)
Value = TypeVar("Value", covariant=True)


class Fget(
    BaseDataCollection.Data,
    Protocol[DataKey, DataValue],
):
    """Define the protocol that the data property must satisfy."""

    @setdoc.basic
    def __getitem__(self: Self, key: Hashable) -> DataValue: ...


Fget.__name__ = "Data"
setdoc.basic(Fget)


class BaseDataMapping(  # type: ignore[type-var]
    BaseDataCollection[Key],
    Mapping[Key, Value],
):
    """Act as base class for mapping implementation which only has to override __fget__ and __fset__ to work immediately."""

    __slots__ = ()

    Data = Fget

    @setdoc.basic
    def __contains__(self: Self, other: object, /) -> bool:
        try:
            return Mapping.__contains__(self, other)
        except TypeError:
            return other in tuple(self)

    @setdoc.basic
    def __fget__(self: Self) -> Fget:
        return super().__fget__()

    @setdoc.basic
    def __getitem__(self: Self, key: Hashable, /) -> Value:
        return self.__fget__()[key]
