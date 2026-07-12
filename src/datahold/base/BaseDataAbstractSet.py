from __future__ import annotations

__all__: list[str] = ["BaseDataAbstractSet"]
from abc import abstractmethod
from collections.abc import Container, Hashable, Iterable, Iterator, Set, Sized
from typing import Never, Protocol, Self, TypeVar

import setdoc

DataItem = TypeVar("DataItem", covariant=True)
Item = TypeVar("Item", covariant=True)


class Container_(Container[object]): ...


class BaseDataAbstractSet(Container_, Set[Item]):
    """Act as a base class for concrete set implementations backed by a data attribute."""

    # this abc exists to provide the easiest possible template for a Set
    # a subclass must only override ``data``
    # and it is immediately non-abstract

    __slots__ = ()

    @setdoc.basic
    class Data(
        Hashable,
        Sized,
        Iterable[DataItem],
        Container[Never],  # every TypeError is worked around
        Protocol[DataItem],
    ):
        """Define the protocol that the data property must satisfy."""

    @setdoc.basic
    def __contains__(self: Self, other: object) -> bool:
        try:
            return other in self.data
        except TypeError:
            return other in tuple(self)

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> BaseDataAbstractSet.Data[Item]: ...

    @setdoc.basic
    def __iter__(self: Self) -> Iterator[Item]:
        return iter(self.data)

    @setdoc.basic
    def __len__(self: Self) -> int:
        return len(self.data)

    @property
    @setdoc.basic
    def data(self: Self) -> BaseDataAbstractSet.Data[Item]:
        return self.__fget__()
