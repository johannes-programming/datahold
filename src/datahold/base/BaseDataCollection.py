from __future__ import annotations

__all__: list[str] = ["BaseDataCollection"]
from abc import abstractmethod
from collections.abc import Collection, Container, Iterable, Iterator, Sized
from typing import Never, Protocol, Self

import setdoc


class BaseDataCollection[Item](Collection[Item]):
    """Act as base class for collection implementation which only needs overriding of __data__ to work immediately."""

    __slots__ = ()

    @setdoc.basic
    class Data[DataItem](
        Sized,
        Iterable[DataItem],
        Container[Never],  # every TypeError is worked around
        Protocol[DataItem],
    ): ...

    @setdoc.basic
    def __contains__(self: Self, other: object, /) -> bool:
        try:
            return other in self.__data__()
        except TypeError:
            return other in (x for x in self)  # type: ignore[operator]

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> Data[Item]: ...

    @setdoc.basic
    def __iter__(self: Self) -> Iterator[Item]:
        return iter(self.__data__())

    @setdoc.basic
    def __len__(self: Self) -> int:
        return len(self.__data__())
