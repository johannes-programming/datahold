"""Provide BaseDataCollection."""

__all__ = ["BaseDataCollection"]


from collections.abc import Collection, Hashable, Iterator, Container, Sized, Iterable
from typing import Protocol, Self, Any, Never

import setdoc

from abc import ABCMeta, abstractmethod


class BaseDataCollection[Item](
    Collection[Item], 
    metaclass=ABCMeta,
):
    __slots__ = ()

    class Data[DataItem](
        Sized,
        Iterable[DataItem],
        Container[Never],
        Hashable,
        Protocol[DataItem],
    ):
        """Provide collection data protocol."""


    @setdoc.basic
    def __eq__(self: Self, other: Any, /) -> Any:
        if isinstance(other, BaseDataCollection):
            return self.data.__eq__(other.data)
        else:
            return NotImplemented

    #@setdoc.basic
    #def __ge__(self: Self, other: Any, /) -> Any:
    #    if not isinstance(other, BaseDataCollection):
    #        return NotImplemented
    #    try:
    #        return self.data.__ge__(other.data)  # type: ignore[operator]
    #    except Exception:
    #        return NotImplemented

    #@setdoc.basic
    #def __gt__(self: Self, other: Any, /) -> Any:
    #    if not isinstance(other, BaseDataCollection):
    #        return NotImplemented
    #    try:
    #        return self.data.__gt__(other.data)  # type: ignore[operator]
    #    except Exception:
    #        return NotImplemented

    #@abstractmethod
    #@setdoc.basic
    #def __init__(self: Self, data: Self, /) -> None: ...

    #@setdoc.basic
    #def __le__(self: Self, other: Any, /) -> Any:
    #    if not isinstance(other, BaseDataCollection):
    #        return NotImplemented
    #    try:
    #        return self.data.__le__(other.data)  # type: ignore[operator]
    #    except Exception:
    #        return NotImplemented

    #@setdoc.basic
    #def __lt__(self: Self, other: Any, /) -> Any:
    #    if not isinstance(other, BaseDataCollection):
    #        return NotImplemented
    #    try:
    #        return self.data.__lt__(other.data)  # type: ignore[operator]
    #    except Exception:
    #        return NotImplemented

    #@setdoc.basic
    #def __ne__(self: Self, other: Any, /) -> Any:
    #    if isinstance(other, BaseDataCollection):
    #        return self.data.__ne__(other.data)
    #    else:
    #        return NotImplemented



    @setdoc.basic
    def __contains__(self: Self, other: object, /) -> bool:
        try:
            return other in self.data
        except TypeError:
            return other in (x for x in self.data)

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
