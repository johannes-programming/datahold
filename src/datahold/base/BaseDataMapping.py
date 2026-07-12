from __future__ import annotations

__all__: list[str] = ["BaseDataMapping"]
from abc import abstractmethod
from collections.abc import (
    Container,
    Hashable,
    Iterable,
    Mapping,
    Sized,
)
from typing import Protocol, Self, TypeVar
from .BaseDataCollection import BaseDataCollection

import setdoc

DataKey = TypeVar("DataKey", covariant=True)
DataValue = TypeVar("DataValue", covariant=True)
Key = TypeVar("Key", covariant=True)
Value = TypeVar("Value", covariant=True)


class Container_(Container[Hashable]): ...


class BaseDataMapping(  # type: ignore[type-var]
    BaseDataCollection[Key],
    Mapping[Key, Value],
):
    """Act as a base class for concrete mapping implementations backed by a data attribute."""

    # this abc exists to provide the easiest possible template for a Mapping
    # a subclass must only override __fget__ and __fset__
    # and it is immediately non-abstract

    __slots__ = ()

    @setdoc.basic
    class Data(
        Hashable, Sized, Iterable[DataKey], Protocol[DataKey, DataValue]
    ):
        """Define the protocol that the data property must satisfy."""

        @setdoc.basic
        def __getitem__(self: Self, key: Hashable) -> DataValue: ...

    @setdoc.basic
    def __contains__(self:Self, other: DataKey, /) -> bool:
        try:
            return Mapping.__contains__(self, other)
        except TypeError:
            return other in tuple(self)

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> BaseDataMapping.Data[Key, Value]: ...

    @setdoc.basic
    def __getitem__(self: Self, key: Hashable, /) -> Value:
        return self.data[key]

    @property
    @setdoc.basic
    def data(self: Self) -> BaseDataMapping.Data[Key, Value]:
        return self.__fget__()
