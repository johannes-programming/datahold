from __future__ import annotations

__all__: list[str] = ["BaseDataMapping"]
from collections.abc import (
    Hashable,
    Mapping,
)
from typing import Protocol, Self, TypeVar
from .BaseDataCollection import BaseDataCollection
from .BaseDataFgettable import BaseDataFgettable

import setdoc

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

class BaseDataFgettable_(BaseDataFgettable[Fget]): ...


class BaseDataMapping(  # type: ignore[type-var]
    BaseDataFgettable_,
    BaseDataCollection[Key],
    Mapping[Key, Value],
):
    """Act as a base class for concrete mapping implementations backed by a data attribute."""

    # this abc exists to provide the easiest possible template for a Mapping
    # a subclass must only override __fget__ and __fset__
    # and it is immediately non-abstract

    __slots__ = ()

    Data=Fget

    @setdoc.basic
    def __contains__(self:Self, other: object, /) -> bool:
        try:
            return Mapping.__contains__(self, other)
        except TypeError:
            return other in tuple(self)

    @setdoc.basic
    def __getitem__(self: Self, key: Hashable, /) -> Value:
        return self.data[key]
