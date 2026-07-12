from __future__ import annotations

__all__: list[str] = ["BaseDataMapping"]
from abc import abstractmethod
from collections.abc import (
    Container,
    Hashable,
    Iterable,
    Iterator,
    Mapping,
    Sized,
)
from typing import Protocol, Self, TypeVar

import setdoc

DataKey = TypeVar("DataKey", covariant=True)
DataValue = TypeVar("DataValue", covariant=True)
Key = TypeVar("Key", covariant=True)
Value = TypeVar("Value", covariant=True)


class Container_(Container[Hashable]): ...


class BaseDataMapping(  # type: ignore[type-var]
    Container_,
    Mapping[Key, Value],
):
    """Act as a base class for concrete mapping implementations backed by a data attribute."""

    # this abc exists to provide the easiest possible template for a Mapping
    # a subclass must only override ``data``
    # and it is immediately non-abstract

    __slots__ = ()

    @setdoc.basic
    class Data(
        Hashable, Sized, Iterable[DataKey], Protocol[DataKey, DataValue]
    ):
        """Define the protocol that the data property must satisfy."""

        @setdoc.basic
        def __getitem__(self: Self, key: Hashable) -> DataValue: ...

    __contains__ = Mapping[Hashable, Value].__contains__

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> BaseDataMapping.Data[Key, Value]: ...

    @setdoc.basic
    def __getitem__(self: Self, key: Hashable) -> Value:
        return self.data[key]

    @setdoc.basic
    def __iter__(self: Self) -> Iterator[Key]:
        return iter(self.data)

    @setdoc.basic
    def __len__(self: Self) -> int:
        return len(self.data)

    @property
    @setdoc.basic
    def data(self: Self) -> BaseDataMapping.Data[Key, Value]:
        return self.__fget__()
