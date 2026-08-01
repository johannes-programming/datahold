"""Provide provides base classes for customized collections."""

from __future__ import annotations

__all__: list[str] = [
    "FrozenListLike",
    "FrozenListSlot",
    "ListLike",
    "ListSlot",
    "MutableListLike",
    "MutableListSlot",
]

from abc import abstractmethod
from collections import abc
from typing import Any, Optional, Self, SupportsIndex, overload

import setdoc

### UTILS ###

type Slice[Key] = slice[Optional[Key], Optional[Key], Optional[Key]]


### LIST-LIKE ###
class ListLike[Item](abc.Sequence[Item]):
    """Provide a base class for customized list-likes."""

    __slots__ = ()

    @setdoc.basic
    def __add__[Item_](
        self: Self, other: ListLike[Item_], /
    ) -> ListLike[Item | Item_]:
        if isinstance(other, ListLike):
            return type(self)(self.__fget__() + other.__fget__())
        else:
            raise TypeError

    @setdoc.basic
    def __contains__(self: Self, other: object, /) -> bool:
        return other in self.__fget__()

    @setdoc.basic
    def __eq__(self: Self, other: ListLike[Any], /) -> bool:
        if isinstance(other, ListLike):
            return self.__fget__() == other.__fget__()
        else:
            return NotImplemented

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self, /) -> list[Item]: ...

    @setdoc.basic
    def __ge__(self: Self, other: ListLike[Any], /) -> bool:
        if isinstance(other, ListLike):
            return self.__fget__() >= other.__fget__()
        else:
            return NotImplemented

    @overload
    @setdoc.basic
    def __getitem__(self: Self, key: SupportsIndex, /) -> Item: ...

    @overload
    @setdoc.basic
    def __getitem__(self: Self, key: Slice[SupportsIndex], /) -> Self: ...

    @setdoc.basic
    def __getitem__(
        self: Self,
        key: SupportsIndex | Slice[SupportsIndex],
        /,
    ) -> Item | Self:
        if isinstance(key, SupportsIndex):
            return self.__fget__()[key]
        else:
            return type(self)(self.__fget__()[key])

    @setdoc.basic
    def __gt__(self: Self, other: ListLike[Any], /) -> bool:
        if isinstance(other, ListLike):
            return self.__fget__() > other.__fget__()
        else:
            return NotImplemented

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: abc.Iterable[Item] = (), /) -> None: ...

    @setdoc.basic
    def __le__(self: Self, other: ListLike[Any], /) -> bool:
        if isinstance(other, ListLike):
            return self.__fget__() <= other.__fget__()
        else:
            return NotImplemented

    @setdoc.basic
    def __len__(self: Self, /) -> int:
        return len(self.__fget__())

    @setdoc.basic
    def __lt__(self: Self, other: ListLike[Any], /) -> bool:
        if isinstance(other, ListLike):
            return self.__fget__() < other.__fget__()
        else:
            return NotImplemented

    @setdoc.basic
    def __mul__(self: Self, other: SupportsIndex, /) -> Self:
        if isinstance(other, SupportsIndex):
            return type(self)(self.__fget__() * other)
        else:
            raise TypeError

    __rmul__ = __mul__

    @setdoc.basic
    def __repr__(self: Self, /) -> str:
        return f"{type(self).__name__}({self.__fget__()!r})"


class ListSlot[Item](ListLike[Item]):
    """Provide slotted list-like class."""

    __slots__ = ("_slot",)

    @setdoc.basic
    def __fget__(self: Self) -> None:
        return self._slot


class FrozenListLike[Item](ListLike[Item], abc.Hashable):
    """Provide a base class for customized frozen list-likes."""

    __slots__ = ()

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(tuple(self.__fget__()))


class FrozenListSlot[Item](ListSlot[Item], FrozenListLike[Item]):
    """Provide a base class for customized frozen data-holds."""

    __slots__ = ()

    @setdoc.basic
    def __init__(self: Self, data: abc.Iterable[Item] = (), /) -> None:
        self._slot: list[Item] = list(data)


class MutableListLike[Item](ListLike[Item], abc.MutableSequence[Item]):
    """Provide a base class for customized mutable list-likes."""

    __slots__ = ()

    @overload
    @setdoc.basic
    def __delitem__(self: Self, key: SupportsIndex, /) -> None: ...
    @overload
    @setdoc.basic
    def __delitem__(self: Self, key: Slice[SupportsIndex], /) -> None: ...
    @setdoc.basic
    def __delitem__(
        self: Self, key: SupportsIndex | Slice[SupportsIndex], /
    ) -> None:
        data: list[Item]
        data = self.__fget__()
        del data[key]
        self.__fset__(data)

    @abstractmethod
    @setdoc.basic
    def __fset__(self: Self, data: list[Item], /) -> None: ...

    @setdoc.basic
    def __imul__(self: Self, other: SupportsIndex, /) -> Self:
        data: list[Item]
        data = self.__fget__()
        data *= other
        self.__fset__(data)
        return self

    @setdoc.basic
    def __init__(self: Self, data: abc.Iterable[Item] = (), /) -> None:
        self.__fset__(list(data))

    @overload
    @setdoc.basic
    def __setitem__(
        self: Self, key: SupportsIndex, value: Item, /
    ) -> None: ...
    @overload
    @setdoc.basic
    def __setitem__(
        self: Self, key: Slice[SupportsIndex], value: abc.Iterable[Item], /
    ) -> None: ...
    @setdoc.basic
    def __setitem__(
        self: Self,
        key: SupportsIndex | Slice[SupportsIndex],
        value: Item | abc.Iterable[Item],
        /,
    ) -> None:
        data: list[Item]
        data = self.__fget__()
        data[key] = value  # type: ignore
        self.__fset__(data)

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self.__fget__())

    @setdoc.basic
    def insert(self: Self, index: SupportsIndex, item: Item, /) -> None:
        data: list[Item]
        data = self.__fget__()
        data.insert(index, item)
        self.__fset__(data)

    @setdoc.basic
    def sort(self: Self, /, *, key: Any = None, reverse: bool = False) -> None:
        data: list[Item]
        data = self.__fget__()
        data.sort(key=key, reverse=reverse)
        self.__fset__(data)


class MutableListSlot[Item](ListSlot[Item], MutableListLike[Item]):
    """Provide slotted mutable list-like class."""

    __slots__ = ()

    @setdoc.basic
    def __fset__(self: Self, data: list[Item], /) -> None:
        self._slot: list[Item] = data
