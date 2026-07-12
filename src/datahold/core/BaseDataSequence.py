from __future__ import annotations

__all__: list[str] = ["BaseDataSequence"]
from abc import abstractmethod
from collections.abc import Container, Hashable, Sequence, Sized
from typing import Protocol, Self, TypeVar

import setdoc

DataItem = TypeVar("DataItem", covariant=True)
Item = TypeVar("Item", covariant=True)


class Container_(Container[object]): ...


class BaseDataSequence(Container_, Sequence[Item]):
    """Act as a base class for concrete sequence implementations backed by a data attribute."""

    __slots__ = ()

    class Data(Hashable, Sized, Protocol[DataItem]):
        """Define the protocol that the data property must satisfy."""

        @setdoc.basic
        def __getitem__(self: Self, index: int) -> DataItem: ...

    __contains__ = Sequence[object].__contains__

    @setdoc.basic
    def __getitem__(self: Self, index: int) -> Item:
        return self.data[index]

    @setdoc.basic
    def __len__(self: Self) -> int:
        return len(self.data)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> BaseDataSequence.Data[Item]: ...
