"""Provide BaseDataCollection."""

__all__: list[str] = ["BaseDataCollection"]

from abc import ABCMeta, abstractmethod
from collections import abc
from typing import Never, Protocol, Self

import setdoc


class BaseDataCollection[Item](
    abc.Sized,
    abc.Iterable[Item],
    abc.Container[object],
    metaclass=ABCMeta,
):
    """Provide an easy abc for a custom collection."""

    __slots__ = ()

    @setdoc.basic
    class Data[DataItem](
        abc.Sized,
        abc.Iterable[DataItem],
        abc.Container[Never],
        abc.Hashable,
        Protocol,
    ):
        """Provide collection data protocol."""

    @setdoc.basic
    def __contains__(self: Self, other: object, /) -> bool:
        try:
            return other in self.__fget__()
        except TypeError:
            return other in (x for x in self.__fget__())  # type: ignore[operator]

    @setdoc.basic
    def __iter__(self: Self, /) -> abc.Iterator[Item]:
        return iter(self.__fget__())

    @setdoc.basic
    def __len__(self: Self, /) -> int:
        return len(self.__fget__())

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> Data[Item]: ...
