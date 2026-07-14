from __future__ import annotations

__all__: list[str] = ["BaseDataCollection"]
from abc import abstractmethod
from collections.abc import (
    Collection,
    Container,
    Hashable,
    Iterable,
    Iterator,
    Sized,
)
from typing import Never, Protocol, Self, TypeVar

import setdoc

DataItem = TypeVar("DataItem", covariant=True)
Item = TypeVar("Item", covariant=True)


class Fget(
    Hashable,
    Sized,
    Iterable[DataItem],
    Container[Never],  # every TypeError is worked around
    Protocol[DataItem],
): ...


Fget.__name__ = "Data"
setdoc.basic(Fget)


class BaseDataCollection(Collection[Item]):
    """Act as base class for collection implementation which only has to override __fget__ and __fset__ to work immediately."""

    __slots__ = ()

    Data = Fget

    @setdoc.basic
    def __contains__(self: Self, other: object, /) -> bool:
        try:
            return other in self.__fget__()
        except TypeError:
            return other in (x for x in self)

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> Fget[Item]: ...

    @abstractmethod
    @setdoc.basic
    def __fset__(self: Self, data: Never, /) -> None: ...

    @setdoc.basic
    def __iter__(self: Self) -> Iterator[Item]:
        return iter(self.__fget__())

    @setdoc.basic
    def __len__(self: Self) -> int:
        return len(self.__fget__())
