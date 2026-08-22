"""Provide easily customized collections."""

from __future__ import annotations

__all__: list[str] = ["ListLike", "MutableListLike", "MutableListSlot"]

import sys
from abc import abstractmethod
from collections import abc
from contextlib import contextmanager
from types import NotImplementedType, TracebackType
from typing import Any, Protocol, Self, SupportsIndex, overload

import setdoc

### PROTOCOLS ###


class ContextManager[Enter](Protocol):
    def __enter__(
        self: Any,
        /,
    ) -> Enter: ...
    def __exit__(
        self: Any,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
        /,
    ) -> object: ...
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


### HELPER ###


def init() -> None:
    x: str
    for x in __all__:
        setdoc.Basics(
            excepts=(AttributeError, TypeError),
        )(*globals()[x].__dict__.values())


def reverse_sequence[Item](
    sequence: ListLike[Item],
    length: int,
) -> abc.Generator[Item, None, None]:
    frozen: tuple[Item, ...]
    while True:
        frozen = sequence.__frozen__()
        length -= 1
        if 0 <= length < len(frozen):
            yield frozen[length]
        else:
            break


### LIST-LIKE ###


class ListLike[Item](abc.Sequence[Item]):
    """Provide easily customizable list-like."""

    __slots__ = ()

    def __add__[Item_](
        self: ListLike[Item],
        other: ListLike[Item_],
        /,
    ) -> ListLike[Item | Item_]:
        if isinstance(other, ListLike):
            return self.__type__(self.__frozen__() + other.__frozen__())
        else:
            return NotImplemented

    def __contains__(self: ListLike[Item], other: object, /) -> bool:
        return other in self.__frozen__()

    def __eq__(
        self: ListLike[Item], other: object, /
    ) -> NotImplementedType | bool:
        if isinstance(other, ListLike):
            return self.__frozen__() == other.__frozen__()
        else:
            return NotImplemented

    @abstractmethod
    def __frozen__(self: ListLike[Item], /) -> tuple[Item, ...]: ...

    @overload
    def __ge__[Item_](
        self: ListLike[SupportsDunderGE[Item_]],
        other: ListLike[Item_],
        /,
    ) -> bool: ...
    @overload
    def __ge__(
        self: ListLike[Item],
        other: ListLike[SupportsDunderLE[Item]],
        /,
    ) -> bool: ...
    def __ge__(
        self: ListLike[Any],
        other: ListLike[Any],
        /,
    ) -> bool:
        return self.__frozen__() >= other.__frozen__()

    @overload
    def __getitem__(self: ListLike[Item], key: SupportsIndex, /) -> Item: ...
    @overload
    def __getitem__(
        self: ListLike[Item], key: Slice[SupportsIndex], /
    ) -> ListLike[Item]: ...
    def __getitem__(self: ListLike[Item], key: Any, /) -> Any:
        if isinstance(key, SupportsIndex):
            return self.__frozen__()[key]
        else:
            return self.__type__(self.__frozen__()[key])

    @overload
    def __gt__[Item_](
        self: ListLike[SupportsDunderGT[Item_]],
        other: ListLike[Item_],
        /,
    ) -> bool: ...
    @overload
    def __gt__(
        self: ListLike[Item],
        other: ListLike[SupportsDunderLT[Item]],
        /,
    ) -> bool: ...
    def __gt__(
        self: ListLike[Any],
        other: ListLike[Any],
        /,
    ) -> bool:
        return self.__frozen__() > other.__frozen__()

    @abstractmethod
    def __init__(
        self: ListLike[Item],
        other: abc.Iterable[Item] = (),
        /,
    ) -> None: ...

    def __iter__(self: ListLike[Item], /) -> abc.Generator[Item, None, None]:
        frozen: tuple[Item, ...]
        i: int
        i = 0
        while True:
            frozen = self.__frozen__()
            if i < len(frozen):
                yield frozen[i]
                i += 1
            else:
                break

    @overload
    def __le__[Item_](
        self: ListLike[SupportsDunderLE[Item_]],
        other: ListLike[Item_],
        /,
    ) -> bool: ...
    @overload
    def __le__(
        self: ListLike[Item],
        other: ListLike[SupportsDunderGE[Item]],
        /,
    ) -> bool: ...
    def __le__(
        self: ListLike[Any],
        other: ListLike[Any],
        /,
    ) -> bool:
        return self.__frozen__() <= other.__frozen__()

    def __len__(self: ListLike[Item], /) -> int:
        return len(self.__frozen__())

    @overload
    def __lt__[Item_](
        self: ListLike[SupportsDunderLT[Item_]],
        other: ListLike[Item_],
        /,
    ) -> bool: ...
    @overload
    def __lt__(
        self: ListLike[Item],
        other: ListLike[SupportsDunderGT[Item]],
        /,
    ) -> bool: ...
    def __lt__(
        self: ListLike[Any],
        other: ListLike[Any],
        /,
    ) -> bool:
        return self.__frozen__() < other.__frozen__()

    def __mul__(
        self: ListLike[Item], other: SupportsIndex, /
    ) -> ListLike[Item]:
        return self.__type__(self.__frozen__() * other)

    __rmul__ = __mul__

    def __repr__(self: ListLike[Item], /) -> str:
        return f"{type(self).__name__}({list(self.__frozen__())})"

    def __reversed__(self: ListLike[Item], /) -> abc.Iterator[Item]:
        return reverse_sequence(
            sequence=self,
            length=len(self.__frozen__()),
        )

    @classmethod
    @abstractmethod
    def __type__[Item_](
        cls: type[ListLike[Item]],
        other: abc.Iterable[Item_],
        /,
    ) -> ListLike[Item_]: ...

    def count(self: ListLike[Item], item: object, /) -> int:
        return self.__frozen__().count(item)

    def index(
        self: ListLike[Item],
        item: Item,
        start: SupportsIndex = 0,
        stop: SupportsIndex = sys.maxsize,
        /,
    ) -> int:
        return self.__frozen__().index(item, start, stop)


### LIST-SLOT ###


class MutableListLike[Item](ListLike[Item]):
    """Provide easily customizable, slotted list-like."""

    __slots__ = ()

    @overload
    def __delitem__(
        self: MutableListLike[Item],
        key: SupportsIndex,
        /,
    ) -> None: ...
    @overload
    def __delitem__(
        self: MutableListLike[Item],
        key: Slice[SupportsIndex],
        /,
    ) -> None: ...
    def __delitem__(
        self: MutableListLike[Item],
        key: Any,
        /,
    ) -> None:
        with self.__mutate__() as mutable:
            del mutable[key]

    def __iadd__(  # type: ignore[misc, override]
        self: MutableListLike[Item],
        other: abc.Iterable[Item],  # type: ignore[override]
        /,
    ) -> MutableListLike[Item]:
        with self.__mutate__() as mutable:
            mutable += other
        return self

    def __imul__(
        self: MutableListLike[Item],
        other: SupportsIndex,
        /,
    ) -> MutableListLike[Item]:
        with self.__mutate__() as mutable:
            mutable *= other
        return self

    def __init__(
        self: MutableListLike[Item],
        other: abc.Iterable[Item] = (),
        /,
    ) -> None:
        self.extend(other)

    @abstractmethod
    def __mutate__(
        self: MutableListLike[Item], /
    ) -> ContextManager[list[Item]]: ...

    @overload
    def __setitem__(
        self: MutableListLike[Item],
        key: SupportsIndex,
        value: Item,
        /,
    ) -> None: ...
    @overload
    def __setitem__(
        self: MutableListLike[Item],
        key: Slice[SupportsIndex],
        value: abc.Iterable[Item],
        /,
    ) -> None: ...
    def __setitem__(
        self: MutableListLike[Item],
        key: Any,
        value: Any,
        /,
    ) -> None:
        with self.__mutate__() as mutable:
            mutable[key] = value

    def append(self: MutableListLike[Item], item: Item, /) -> None:
        with self.__mutate__() as mutable:
            mutable.append(item)

    def clear(self: MutableListLike[Item], /) -> None:
        with self.__mutate__() as mutable:
            mutable.clear()

    def copy(self: MutableListLike[Item], /) -> ListLike[Item]:
        return self.__type__(self.__frozen__())

    def extend(
        self: MutableListLike[Item], other: abc.Iterable[Item], /
    ) -> None:
        with self.__mutate__() as mutable:
            mutable.extend(other)

    def insert(
        self: MutableListLike[Item], index: SupportsIndex, item: Item, /
    ) -> None:
        with self.__mutate__() as mutable:
            mutable.insert(index, item)

    def pop(self: MutableListLike[Item], index: SupportsIndex = -1, /) -> Item:
        with self.__mutate__() as mutable:
            return mutable.pop(index)

    def remove(self: MutableListLike[Item], item: object, /) -> None:
        with self.__mutate__() as mutable:
            mutable.remove(
                item,  # type: ignore[arg-type]
            )

    def reverse(self: MutableListLike[Item], /) -> None:
        with self.__mutate__() as mutable:
            mutable.reverse()

    @overload
    def sort[T: Sort](
        self: MutableListLike[T],
        /,
        *,
        reverse: bool = False,
    ) -> None: ...
    @overload
    def sort[T: Sort](
        self: MutableListLike[Item],
        /,
        *,
        key: abc.Callable[[Item], T],
        reverse: bool = False,
    ) -> None: ...
    def sort(
        self: MutableListLike[Item],
        /,
        *,
        key: Any = None,
        reverse: bool = False,
    ) -> None:
        with self.__mutate__() as mutable:
            mutable.sort(key=key, reverse=reverse)


class MutableListSlot[Item](MutableListLike[Item]):
    """Provide easily customizable, mutable, slotted list-like."""

    __slots__ = ("_slot",)

    _slot: tuple[Item, ...]

    def __frozen__(self: MutableListSlot[Item], /) -> tuple[Item, ...]:
        return self._slot

    @contextmanager
    def __mutate__(
        self: MutableListSlot[Item], /
    ) -> abc.Generator[list[Item]]:
        mutable: list[Item]
        mutable = list(getattr(self, "_slot", ()))
        yield mutable
        self._slot = tuple(mutable)

    @classmethod
    def __type__[Item_](
        cls: type[MutableListSlot[Item]],
        other: abc.Iterable[Item_],
        /,
    ) -> MutableListSlot[Item_]:
        return MutableListSlot(other)


init()
