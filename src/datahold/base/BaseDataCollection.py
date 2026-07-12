from __future__ import annotations

__all__: list[str] = ["BaseDataCollection"]
from abc import abstractmethod
from collections.abc import Container, Hashable, Iterable, Iterator, Sized, Collection
from typing import Never, Protocol, Self, TypeVar, Any
from BaseDataFgettable import BaseDataFgettable

import setdoc

DataItem = TypeVar("DataItem", covariant=True)
Item = TypeVar("Item", covariant=True)


class Fget(
    Hashable,
    Sized,
    Iterable[DataItem],
    Container[Never],  # every TypeError is worked around
    Protocol[DataItem],
):
    ...
Fget.__name__ = "Data"
setdoc.basic(Fget)
class BaseDataCollection(BaseDataFgettable[Fget[Item]], Collection[Item]):
    """Act as a base class for concrete set implementations backed by a data attribute."""

    # this abc exists to provide the easiest possible template for a Set
    # a subclass must only override __fget__ and __fset__
    # and it is immediately non-abstract

    __slots__ = ()

    Data = Fget

    @setdoc.basic
    def __contains__(self: Self, other: object) -> bool:
        try:
            return other in self.data
        except TypeError:
            return other in (x for x in self)

    @abstractmethod
    @setdoc.basic
    def __fset__(self: Self, data:Iterable[Any], /) -> None: ...

    @setdoc.basic
    def __init__(self:Self, data:Iterable[Any] = (), /) -> None:
        self.__fset__(data)

    @setdoc.basic
    def __iter__(self: Self) -> Iterator[Item]:
        return iter(self.data)

    @setdoc.basic
    def __len__(self: Self) -> int:
        return len(self.data)
