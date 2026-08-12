"""Provide easily customized collections."""

from __future__ import annotations

__all__: list[str] = ["MutableListSlot"]

import sys
from collections import abc
from contextlib import contextmanager
from types import NotImplementedType
from typing import Any, Protocol, Self, SupportsIndex, overload

import setdoc

### PROTOCOLS ###


class SupportsDunderGE[Other](Protocol):
    def __ge__(self: Any, other: Other, /) -> bool: ...
class SupportsDunderGT[Other](Protocol):
    def __gt__(self: Any, other: Other, /) -> bool: ...
class SupportsDunderLE[Other](Protocol):
    def __le__(self: Any, other: Other, /) -> bool: ...
class SupportsDunderLT[Other](Protocol):
    def __lt__(self: Any, other: Other, /) -> bool: ...


### ALIASES ###

type Slice[Index] = slice[Index | None, Index | None, Index | None]
type Sort = SupportsDunderGT[Self] | SupportsDunderGT[Self]  # type: ignore[misc]

### LIST-SLOT ###


class MutableListSlot[Item]:
    """Provide easily customized, slotted, mutable list-like."""

    __slots__ = ("_slot",)

    _slot: tuple[Item, ...]

    def __add__[Item_](
        self: MutableListSlot[Item],
        other: MutableListSlot[Item_],
        /,
    ) -> MutableListSlot[Item | Item_]:
        if isinstance(other, MutableListSlot):
            return self.__type__(self.__frozen__() + other.__frozen__())
        else:
            return NotImplemented

    def __contains__(self: MutableListSlot[Item], other: object, /) -> bool:
        return other in self.__frozen__()

    @overload
    def __delitem__(
        self: MutableListSlot[Item],
        key: SupportsIndex,
        /,
    ) -> None: ...
    @overload
    def __delitem__(
        self: MutableListSlot[Item],
        key: Slice[SupportsIndex],
        /,
    ) -> None: ...
    def __delitem__(
        self: MutableListSlot[Item],
        key: Any,
        /,
    ) -> None:
        with self.__mutate__() as mutable:
            del mutable[key]

    def __eq__(
        self: MutableListSlot[Item], other: object, /
    ) -> NotImplementedType | bool:
        if isinstance(other, MutableListSlot):
            return self.__frozen__() == other.__frozen__()
        else:
            return NotImplemented

    def __frozen__(self: MutableListSlot[Item], /) -> tuple[Item, ...]:
        return self._slot

    def __ge__(
        self: MutableListSlot[Item],
        other: MutableListSlot[SupportsDunderLE[Item]],
        /,
    ) -> bool:
        return self.__frozen__() >= other.__frozen__()  # type: ignore[no-any-return, operator]

    @overload
    def __getitem__(
        self: MutableListSlot[Item], key: SupportsIndex, /
    ) -> Item: ...
    @overload
    def __getitem__(
        self: MutableListSlot[Item], key: Slice[SupportsIndex], /
    ) -> MutableListSlot[Item]: ...
    def __getitem__(self: MutableListSlot[Item], key: Any, /) -> Any:
        if isinstance(key, SupportsIndex):
            return self.__frozen__()[key]
        else:
            return self.__type__(self.__frozen__()[key])

    def __gt__(
        self: MutableListSlot[Item],
        other: MutableListSlot[SupportsDunderLT[Item]],
        /,
    ) -> bool:
        return self.__frozen__() > other.__frozen__()  # type: ignore[no-any-return, operator]

    def __iadd__(  # type: ignore[misc]
        self: MutableListSlot[Item],
        other: abc.Iterable[Item],
        /,
    ) -> MutableListSlot[Item]:
        with self.__mutate__() as mutable:
            mutable += other
        return self

    def __imul__(
        self: MutableListSlot[Item],
        other: SupportsIndex,
        /,
    ) -> MutableListSlot[Item]:
        with self.__mutate__() as mutable:
            mutable *= other
        return self

    def __init__(
        self: MutableListSlot[Item],
        other: abc.Iterable[Item] = (),
        /,
    ) -> None:
        self.extend(other)

    def __iter__(
        self: MutableListSlot[Item], /
    ) -> abc.Generator[Item, None, None]:
        i: int
        i = 0
        while True:
            try:
                v = self[i]
            except IndexError:
                return
            yield v
            i += 1

    def __le__(
        self: MutableListSlot[Item],
        other: MutableListSlot[SupportsDunderGE[Item]],
        /,
    ) -> bool:
        return self.__frozen__() <= other.__frozen__()  # type: ignore[no-any-return, operator]

    def __len__(self: MutableListSlot[Item], /) -> int:
        return len(self.__frozen__())

    def __lt__(
        self: MutableListSlot[Item],
        other: MutableListSlot[SupportsDunderGT[Item]],
        /,
    ) -> bool:
        return self.__frozen__() < other.__frozen__()  # type: ignore[no-any-return, operator]

    def __mul__(
        self: MutableListSlot[Item], other: SupportsIndex, /
    ) -> MutableListSlot[Item]:
        return self.__type__(self.__frozen__() * other)

    __rmul__ = __mul__

    @contextmanager
    def __mutate__(
        self: MutableListSlot[Item], /
    ) -> abc.Generator[list[Item]]:
        mutable: list[Item]
        mutable = list(getattr(self, "_slot", ()))
        yield mutable
        self._slot = tuple(mutable)

    def __repr__(self: MutableListSlot[Item], /) -> str:
        return f"{type(self).__name__}({list(self.__frozen__())})"

    def __reversed__(
        self: MutableListSlot[Item], /
    ) -> abc.Generator[Item, None, None]:
        i: int
        for i in reversed(range(len(self))):
            yield self[i]

    @overload
    def __setitem__(
        self: MutableListSlot[Item],
        key: SupportsIndex,
        value: Item,
        /,
    ) -> None: ...
    @overload
    def __setitem__(
        self: MutableListSlot[Item],
        key: Slice[SupportsIndex],
        value: abc.Iterable[Item],
        /,
    ) -> None: ...
    def __setitem__(
        self: MutableListSlot[Item],
        key: Any,
        value: Any,
        /,
    ) -> None:
        with self.__mutate__() as mutable:
            mutable[key] = value

    @classmethod
    def __type__[Item_](
        cls: type[MutableListSlot[Item]],
        other: abc.Iterable[Item_],
        /,
    ) -> MutableListSlot[Item_]:
        return MutableListSlot(other)

    def append(self: MutableListSlot[Item], item: Item, /) -> None:
        with self.__mutate__() as mutable:
            mutable.append(item)

    def clear(self: MutableListSlot[Item], /) -> None:
        with self.__mutate__() as mutable:
            mutable.clear()

    def copy(self: MutableListSlot[Item], /) -> MutableListSlot[Item]:
        return self.__type__(self.__frozen__())

    def count(self: MutableListSlot[Item], item: object, /) -> int:
        return self.__frozen__().count(item)

    def extend(
        self: MutableListSlot[Item], other: abc.Iterable[Item], /
    ) -> None:
        with self.__mutate__() as mutable:
            mutable.extend(other)

    def index(
        self: MutableListSlot[Item],
        item: Item,
        start: SupportsIndex = 0,
        stop: SupportsIndex = sys.maxsize,
        /,
    ) -> int:
        return self.__frozen__().index(item, start, stop)

    def insert(
        self: MutableListSlot[Item], index: SupportsIndex, item: Item, /
    ) -> None:
        with self.__mutate__() as mutable:
            mutable.insert(index, item)

    def pop(self: MutableListSlot[Item], index: SupportsIndex = -1, /) -> Item:
        with self.__mutate__() as mutable:
            return mutable.pop(index)

    def remove(self: MutableListSlot[Item], item: object, /) -> None:
        with self.__mutate__() as mutable:
            mutable.remove(
                item,  # type: ignore[arg-type]
            )

    def reverse(self: MutableListSlot[Item], /) -> None:
        with self.__mutate__() as mutable:
            mutable.reverse()

    @overload
    def sort[T: Sort](
        self: MutableListSlot[T],
        /,
        *,
        reverse: bool = False,
    ) -> None: ...
    @overload
    def sort[T: Sort](
        self: MutableListSlot[Item],
        /,
        *,
        key: abc.Callable[[Item], T],
        reverse: bool = False,
    ) -> None: ...
    def sort(
        self: MutableListSlot[Item],
        /,
        *,
        key: Any = None,
        reverse: bool = False,
    ) -> None:
        with self.__mutate__() as mutable:
            mutable.sort(key=key, reverse=reverse)


setdoc.Basics(
    excepts=(AttributeError, TypeError),
)(*MutableListSlot.__dict__)
