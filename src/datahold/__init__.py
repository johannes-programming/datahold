from __future__ import annotations

__all__: list[str] = ["ListLike", "FrozenListLike", "FrozenListSlot"]

import sys
from abc import abstractmethod
from collections import abc
from reprlib import recursive_repr
from types import NotImplementedType
from typing import Any, Protocol, Self, SupportsIndex, overload

type Slice[Index] = slice[Index, Index, Index]


class SupportsGE[Other, Return](Protocol):
    def __ge__(self: Self, other: Other, /) -> Return: ...
class SupportsGT[Other, Return](Protocol):
    def __gt__(self: Self, other: Other, /) -> Return: ...
class SupportsLE[Other, Return](Protocol):
    def __le__(self: Self, other: Other, /) -> Return: ...
class SupportsLT[Other, Return](Protocol):
    def __lt__(self: Self, other: Other, /) -> Return: ...


class ListLike[Item](abc.Sequence[Item]):
    __slots__ = ()

    def __add__[Item_](
        self: Self,
        other: ListLike[Item_],
        /,
    ) -> ListLike[Item | Item_]:
        if isinstance(other, ListLike):
            return self.__type__(  # type: ignore[return-value]
                self.__fget__() + other.__fget__()  # type: ignore[operator]
            )
        else:
            return NotImplemented

    def __contains__(self, value: object, /) -> bool:
        return value in self.__fget__()

    def __eq__(
        self: Self,
        other: object,
        /,
    ) -> bool | NotImplementedType:
        if isinstance(other, ListLike):
            return self.__fget__() == other.__fget__()
        else:
            return NotImplemented

    @abstractmethod
    def __fget__(self: Self, /) -> tuple[Item, ...]: ...

    @overload
    def __ge__[Item_, Return](
        self: ListLike[SupportsGE[Item_, Return]],
        other: ListLike[Item_],
        /,
    ) -> Return | bool: ...

    @overload
    def __ge__[Return](
        self: Self,
        other: ListLike[SupportsLE[Item, Return]],
        /,
    ) -> Return | bool: ...

    def __ge__(
        self: Self,
        other: ListLike[Any],
        /,
    ) -> Any:
        if isinstance(other, ListLike):
            return self.__fget__() >= other.__fget__()
        else:
            return NotImplemented

    @overload
    def __getitem__(self: Self, index: SupportsIndex, /) -> Item: ...

    @overload
    def __getitem__(
        self: Self, index: Slice[SupportsIndex | None], /
    ) -> ListLike[Item]: ...

    def __getitem__(
        self: Self,
        index: SupportsIndex | Slice[SupportsIndex | None],
        /,
    ) -> Item | ListLike[Item]:
        if isinstance(index, SupportsIndex):
            return self.__fget__()[index]
        else:
            return self.__type__(self.__fget__()[index])

    @overload
    def __gt__[Item_, Return](
        self: ListLike[SupportsGT[Item_, Return]],
        other: ListLike[Item_],
        /,
    ) -> Return | bool: ...

    @overload
    def __gt__[Return](
        self: Self,
        other: ListLike[SupportsLT[Item, Return]],
        /,
    ) -> Return | bool: ...

    def __gt__(
        self: Self,
        other: ListLike[Any],
        /,
    ) -> Any:
        if isinstance(other, ListLike):
            return self.__fget__() > other.__fget__()
        else:
            return NotImplemented

    @abstractmethod
    def __init__(self: Self, data: abc.Iterable[Item] = (), /) -> None: ...

    def __iter__(self) -> abc.Iterator[Item]:
        return iter(self.__fget__())

    @overload
    def __le__[Item_, Return](
        self: ListLike[SupportsLE[Item_, Return]],
        other: ListLike[Item_],
        /,
    ) -> Return | bool: ...

    @overload
    def __le__[Return](
        self: Self,
        other: ListLike[SupportsGE[Item, Return]],
        /,
    ) -> Return | bool: ...

    def __le__(
        self: Self,
        other: ListLike[Any],
        /,
    ) -> Any:
        if isinstance(other, ListLike):
            return self.__fget__() <= other.__fget__()
        else:
            return NotImplemented

    def __len__(self: Self, /) -> int:
        return len(self.__fget__())

    @overload
    def __lt__[Item_, Return](
        self: ListLike[SupportsLT[Item_, Return]],
        other: ListLike[Item_],
        /,
    ) -> Return | bool: ...

    @overload
    def __lt__[Return](
        self: Self,
        other: ListLike[SupportsGT[Item, Return]],
        /,
    ) -> Return | bool: ...

    def __lt__(
        self: Self,
        other: ListLike[Any],
        /,
    ) -> Any:
        if isinstance(other, ListLike):
            return self.__fget__() < other.__fget__()
        else:
            return NotImplemented

    def __mul__(
        self: Self,
        other: SupportsIndex,
        /,
    ) -> ListLike[Item]:
        return self.__type__(self.__fget__() * other)

    __rmul__ = __mul__

    @recursive_repr()
    def __repr__(self) -> str:
        return f"{type(self).__name__}({list(self.__fget__())!r})"

    @classmethod
    def __type__(
        cls: type[Self], data: abc.Iterable[Item], /
    ) -> ListLike[Item]:
        return cls(data)

    def count(self: Self, item: Item, /) -> int:
        return self.__fget__().count(item)

    def index(
        self: Self,
        item: Item,
        start: SupportsIndex = 0,
        stop: SupportsIndex = sys.maxsize,
        /,
    ) -> int:
        return self.__fget__().index(item, start, stop)


class FrozenListLike[Item](ListLike[Item]):
    __slots__ = ()

    def __hash__(self: Self, /) -> int:
        return hash(self.__fget__())


class FrozenListSlot[Item](FrozenListLike[Item]):
    __slots__ = ("_slot",)
    _slot: tuple[Item, ...]

    def __fget__(self: Self, /) -> tuple[Item, ...]:
        return self._slot

    def __getstate__(
        self: Self,
        /,
    ) -> tuple[None, dict[str, tuple[Item, ...]]]:
        return None, {"_slot": self._slot}

    def __init__(self: Self, data: abc.Iterable[Item] = (), /) -> None:
        self._slot = tuple(data)
