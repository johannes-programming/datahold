"""Provide BaseDataCollection."""

__all__ = ["BaseDataCollection"]


from abc import ABCMeta, abstractmethod
from collections.abc import Container, Hashable, Iterable, Iterator, Sized
from typing import Never, Protocol, Self

import setdoc


class BaseDataCollection[Item](
    Sized,
    Iterable[Item],
    Container[object],
    metaclass=ABCMeta,
):
    """Provide an easy abc for a custom collection."""

    __slots__ = ()

    @setdoc.basic
    class Data[DataItem](
        Sized,
        Iterable[DataItem],
        Container[Never],
        Hashable,
        Protocol,
    ):
        """Provide collection data protocol."""

    @setdoc.basic
    def __contains__(self: Self, other: object, /) -> bool:
        try:
            return other in self.data
        except TypeError:
            return other in (x for x in self.data)  # type: ignore[operator]

    @setdoc.basic
    def __iter__(self: Self, /) -> Iterator[Item]:
        return iter(self.data)

    @setdoc.basic
    def __len__(self: Self, /) -> int:
        return len(self.data)

    @property
    @abstractmethod
    @setdoc.basic
    def data(self: Self) -> Data[Item]: ...
