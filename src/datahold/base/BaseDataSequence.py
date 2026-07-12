from __future__ import annotations

__all__: list[str] = ["BaseDataSequence"]
from abc import abstractmethod
from collections.abc import Container, Hashable, Iterable, Sequence, Sized
from typing import Protocol, Self, TypeVar, overload

import setdoc

DataItem = TypeVar("DataItem", covariant=True)
Item = TypeVar("Item", covariant=True)


class Container_(Container[object]): ...


class BaseDataSequence(Container_, Sequence[Item]):
    """Act as a base class for concrete sequence implementations backed by a data attribute."""

    # this abc exists to provide the easiest possible template for a Sequence
    # a subclass must only override ``__init__`` and ``data``
    # and it is immediately non-abstract

    __slots__ = ()

    @setdoc.basic
    class Data(Hashable, Sized, Protocol[DataItem]):
        """Define the protocol that the data property must satisfy."""

        @overload
        @setdoc.basic
        def __getitem__(self: Self, index: int) -> DataItem: ...

        @overload
        @setdoc.basic
        def __getitem__(self: Self, index: slice) -> Iterable[DataItem]: ...

        def __getitem__(
            self: Self, index: int | slice
        ) -> DataItem | Iterable[DataItem]: ...

    __contains__ = Sequence[object].__contains__

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> BaseDataSequence.Data[Item]: ...

    @overload
    @setdoc.basic
    def __getitem__(self: Self, index: int) -> Item: ...

    @overload
    @setdoc.basic
    def __getitem__(self: Self, index: slice) -> Self: ...

    @setdoc.basic
    def __getitem__(self: Self, index: int | slice) -> Item | Self:
        # Sequence.__getitem__ reveals "Overload(def [_T_co] (typing.Sequence[_T_co], int) -> _T_co, def [_T_co] (typing.Sequence[_T_co], slice[int | None, int | None, int | None]) -> typing.Sequence[_T_co])"
        if isinstance(index, slice):
            # index cannot be an int now because subclassing slice is impossible
            # we are forced to assume a constructor signature
            # the subtype of BaseDataSequence might be immutable
            return type(self)(self.data[index])
        else:
            return self.data[index]

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Iterable[Item] = (), /) -> None:
        # Implementing an (abstract) __init__ is necessary
        # because of __getitem__
        # Iterable[Item] is more practical than Data[Item]
        # as annotation for data
        ...

    @setdoc.basic
    def __len__(self: Self) -> int:
        return len(self.data)

    @property
    @setdoc.basic
    def data(self: Self) -> BaseDataSequence.Data[Item]:
        return self.__fget__()
