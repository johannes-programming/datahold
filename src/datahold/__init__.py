"""Provide provides base classes for customized collections."""

from __future__ import annotations

__all__: list[str] = [
    "FrozenListLike",
    "FrozenListSlot",
    "ListLike",
    "ListSlot",
    "MutableListLike",
    "MutableListSlot",
    "Sequence",
]

from abc import abstractmethod
from collections import abc
from contextlib import contextmanager
from types import NotImplementedType, TracebackType
from typing import Any, Optional, Protocol, Self, SupportsIndex, overload

import setdoc

### UTILS ###

type Slice[Index] = slice[Optional[Index], Optional[Index], Optional[Index]]


### SEQUENCE ###


class Sequence[Item](abc.Sequence[Item]):
    """Provide a base class for customized sequence."""

    __slots__ = ()

    @setdoc.basic
    class Frozen[FrozenItem](Protocol):
        @overload
        @setdoc.basic
        def __getitem__(self: Self, key: int, /) -> FrozenItem: ...
        @overload
        @setdoc.basic
        def __getitem__(
            self: Self, key: Slice[int], /
        ) -> abc.Sequence[FrozenItem]: ...
        @setdoc.basic
        def __getitem__(
            self: Self,
            key: int | Slice[int],
            /,
        ) -> FrozenItem | abc.Sequence[FrozenItem]: ...
        @setdoc.basic
        def __len__(self: Self, /) -> int: ...
    @abstractmethod
    @setdoc.basic
    def __frozen__(self: Self, /) -> Frozen[Item]: ...
    @overload
    @setdoc.basic
    def __getitem__(self: Self, key: int, /) -> Item: ...
    @overload
    @setdoc.basic
    def __getitem__(self: Self, key: Slice[int], /) -> abc.Sequence[Item]: ...
    @setdoc.basic
    def __getitem__(
        self: Self, key: int | Slice[int], /
    ) -> Item | abc.Sequence[Item]:
        return self.__frozen__()[key]

    @setdoc.basic
    def __len__(self: Self) -> int:
        return len(self.__frozen__())


### LIST-LIKE ###
class ListLike[Item](Sequence[Item]):
    """Provide a base class for customized list-likes."""

    __slots__ = ()

    type Frozen[FrozenItem] = tuple[FrozenItem, ...]
    # Frozen has to be tuple to allow covariance

    type Init[InitItem] = abc.Iterable[InitItem]

    @setdoc.basic
    def __add__[Item_](
        self: Self, other: ListLike[Item_], /
    ) -> ListLike[Item | Item_]:
        if isinstance(other, ListLike):
            return type(self)(self.__frozen__() + other.__frozen__())  # type: ignore[operator]
        else:
            raise TypeError

    @setdoc.basic
    def __contains__(self: Self, other: object, /) -> bool:
        return other in self.__frozen__()

    @setdoc.basic
    def __eq__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, ListLike):
            return self.__frozen__() == other.__frozen__()
        else:
            return NotImplemented

    @abstractmethod
    @setdoc.basic
    def __frozen__(self: Self, /) -> Frozen[Item]: ...

    @setdoc.basic
    def __ge__(self: Self, other: ListLike[Any], /) -> bool:
        if isinstance(other, ListLike):
            return self.__frozen__() >= other.__frozen__()
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
            return self.__frozen__()[key]
        else:
            return type(self)(self.__frozen__()[key])

    @setdoc.basic
    def __gt__(self: Self, other: ListLike[Any], /) -> bool:
        if isinstance(other, ListLike):
            return self.__frozen__() > other.__frozen__()
        else:
            return NotImplemented

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Init[Item] = (), /) -> None: ...

    @setdoc.basic
    def __le__(self: Self, other: ListLike[Any], /) -> bool:
        if isinstance(other, ListLike):
            return self.__frozen__() <= other.__frozen__()
        else:
            return NotImplemented

    @setdoc.basic
    def __len__(self: Self, /) -> int:
        return len(self.__frozen__())

    @setdoc.basic
    def __lt__(self: Self, other: ListLike[Any], /) -> bool:
        if isinstance(other, ListLike):
            return self.__frozen__() < other.__frozen__()
        else:
            return NotImplemented

    @setdoc.basic
    def __mul__(self: Self, other: SupportsIndex, /) -> Self:
        if isinstance(other, SupportsIndex):
            return type(self)(self.__frozen__() * other)
        else:
            raise TypeError

    __rmul__ = __mul__

    @setdoc.basic
    def __repr__(self: Self, /) -> str:
        return f"{type(self).__name__}({list(self)!r})"


class ListSlot[Item](ListLike[Item]):
    """Provide slotted list-like class."""

    __slots__ = ("_slot",)

    _slot: ListSlot.Frozen[Item]

    @setdoc.basic
    def __frozen__(self: Self) -> ListSlot.Frozen[Item]:
        return self._slot


class FrozenListLike[Item](ListLike[Item], abc.Hashable):
    """Provide a base class for customized frozen list-likes."""

    __slots__ = ()

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.__frozen__())


class FrozenListSlot[Item](ListSlot[Item], FrozenListLike[Item]):
    """Provide a base class for customized frozen data-holds."""

    __slots__ = ()

    @setdoc.basic
    def __init__(self: Self, data: abc.Iterable[Item] = (), /) -> None:
        self._slot = tuple(data)


class MutableListLike[Item](ListLike[Item], abc.MutableSequence[Item]):
    """Provide a base class for customized mutable list-likes."""

    __slots__ = ()

    @setdoc.basic
    class Mutable[MutableItem](Protocol):
        @setdoc.basic
        def __enter__(self: Self, /) -> list[MutableItem]: ...
        @setdoc.basic
        def __exit__(
            self,
            exc_type: type[BaseException] | None,
            exc_value: BaseException | None,
            traceback: TracebackType | None,
            /,
        ) -> object: ...

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
        with self.__mutable__() as mutable:
            del mutable[key]

    @setdoc.basic
    def __imul__(self: Self, other: SupportsIndex, /) -> Self:
        with self.__mutable__() as mutable:
            mutable *= other
        return self

    @setdoc.basic
    def __init__(self: Self, data: abc.Iterable[Item] = (), /) -> None:
        with self.__mutable__() as mutable:
            mutable.extend(data)

    @abstractmethod
    @setdoc.basic
    def __mutable__(self: Self, /) -> Mutable[Item]: ...

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
        with self.__mutable__() as mutable:
            mutable[key] = value  # type: ignore

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self.__frozen__())

    @setdoc.basic
    def insert(self: Self, index: SupportsIndex, item: Item, /) -> None:
        with self.__mutable__() as mutable:
            mutable.insert(index, item)

    @setdoc.basic
    def sort(self: Self, /, *, key: Any = None, reverse: bool = False) -> None:
        # list.sort reveals Overload(
        #     def [_T, SupportsRichComparisonT <: _typeshed.SupportsDunderLT[Any] | _typeshed.SupportsDunderGT[Any]] (self: list[SupportsRichComparisonT], *, key: None =, reverse: bool =),
        #     def [_T] (self: list[_T], *, key: def (_T) -> _typeshed.SupportsDunderLT[Any] | _typeshed.SupportsDunderGT[Any], reverse: bool =),
        # )
        with self.__mutable__() as mutable:
            mutable.sort(key=key, reverse=reverse)


class MutableListSlot[Item](ListSlot[Item], MutableListLike[Item]):
    """Provide slotted mutable list-like class."""

    __slots__ = ()

    @contextmanager
    @setdoc.basic
    def __mutable__(self: Self, /) -> abc.Generator[list[Item], None, None]:
        slot = list(getattr(self, "_slot", ()))
        yield slot
        self._slot = tuple(slot)
