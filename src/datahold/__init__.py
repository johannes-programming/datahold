"""Provide provides base classes for customized collections."""

from __future__ import annotations

__all__: list[str] = [
    "Collection",
    "FrozenListLike",
    "FrozenListSlot",
    "ListLike",
    "ListSlot",
    "MutableListLike",
    "MutableListSlot",
    "MutableSequence",
    "Sequence",
]

from abc import abstractmethod
from collections import abc
from contextlib import contextmanager
from types import NotImplementedType, TracebackType
from typing import (
    Any,
    Never,
    Optional,
    Protocol,
    Self,
    SupportsIndex,
    overload,
)

import setdoc

### UTILS ###


class ContextManager[Enter](Protocol):
    """Provide context manager protocol."""

    @setdoc.basic
    def __enter__(self: Self, /) -> Enter: ...

    @setdoc.basic
    def __exit__(
        self: Self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
        /,
    ) -> object: ...


type Slice[Index] = slice[Optional[Index], Optional[Index], Optional[Index]]


### COLLECTION ###


class Collection[Item](
    abc.Sized,
    abc.Iterable[Item],
    abc.Container[object],
):
    """Provide abc for custom collections."""

    @setdoc.basic
    class __Frozen__[FrozenItem](
        abc.Sized,
        abc.Iterable[FrozenItem],
        Protocol,
    ):
        @setdoc.basic
        def __contains__(self: Self, other: Never, /) -> bool: ...

    @setdoc.basic
    def __contains__(self: Self, other: object, /) -> bool:
        try:
            return other in self.__frozen__()
        except TypeError:
            return other in (x for x in self)

    @abstractmethod
    @setdoc.basic
    def __frozen__(self: Self, /) -> __Frozen__[Item]: ...

    @setdoc.basic
    def __iter__(self: Self) -> abc.Iterator[Item]:
        return iter(self.__frozen__())

    @setdoc.basic
    def __len__(self: Self, /) -> int:
        return len(self.__frozen__())


### SEQUENCE ###


class Sequence[Item](Collection[Item], abc.Sequence[Item]):
    """Provide a base class for customized sequence."""

    __slots__ = ()

    @setdoc.basic
    class __Frozen__[FrozenItem](
        Collection.__Frozen__[FrozenItem],
        Protocol,
    ):
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

    @abstractmethod
    @setdoc.basic
    def __frozen__(self: Self, /) -> __Frozen__[Item]: ...

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


class MutableSequence[Item](Sequence[Item], abc.MutableSequence[Item]):
    """Provide a base class for customized mutable list-likes."""

    __slots__ = ()

    @setdoc.basic
    class __Frozen__[FrozenItem](
        Collection.__Frozen__[FrozenItem],
        Protocol,
    ):
        @overload
        @setdoc.basic
        def __getitem__(self: Self, key: int, /) -> FrozenItem: ...
        @overload
        @setdoc.basic
        def __getitem__(
            self: Self, key: Slice[int], /
        ) -> abc.MutableSequence[FrozenItem]: ...
        @setdoc.basic
        def __getitem__(
            self: Self,
            key: int | Slice[int],
            /,
        ) -> FrozenItem | abc.MutableSequence[FrozenItem]: ...
    @setdoc.basic
    class __Mutable__[MutableItem](Protocol):

        @overload
        @setdoc.basic
        def __delitem__(self: Self, key: SupportsIndex, /) -> None: ...
        @overload
        @setdoc.basic
        def __delitem__(self: Self, key: Slice[SupportsIndex], /) -> None: ...
        @setdoc.basic
        def __delitem__(
            self: Self, key: SupportsIndex | Slice[SupportsIndex], /
        ) -> None: ...

        @overload
        @setdoc.basic
        def __setitem__(
            self: Self, key: int, value: MutableItem, /
        ) -> None: ...
        @overload
        @setdoc.basic
        def __setitem__(
            self: Self, key: Slice[int], value: abc.Iterable[MutableItem], /
        ) -> None: ...
        @setdoc.basic
        def __setitem__(
            self: Self,
            key: int | Slice[int],
            value: MutableItem | abc.Iterable[MutableItem],
            /,
        ) -> None:
            with self.__mutate__() as mutable:
                mutable[key] = value  # type: ignore

        @setdoc.basic
        def insert(self: Self, index: int, item: MutableItem, /) -> None: ...

    @overload
    @setdoc.basic
    def __delitem__(self: Self, key: int, /) -> None: ...
    @overload
    @setdoc.basic
    def __delitem__(self: Self, key: Slice[int], /) -> None: ...
    @setdoc.basic
    def __delitem__(self: Self, key: int | Slice[int], /) -> None:
        with self.__mutate__() as mutable:
            del mutable[key]

    @abstractmethod
    @setdoc.basic
    def __frozen__(self: Self) -> __Frozen__[Item]: ...

    @overload
    @setdoc.basic
    def __getitem__(self: Self, key: int, /) -> Item: ...
    @overload
    @setdoc.basic
    def __getitem__(
        self: Self, key: Slice[int], /
    ) -> abc.MutableSequence[Item]: ...
    @setdoc.basic
    def __getitem__(
        self: Self, key: int | Slice[int], /
    ) -> Item | abc.MutableSequence[Item]:
        return self.__frozen__()[key]

    @abstractmethod
    @setdoc.basic
    def __mutate__(self: Self, /) -> ContextManager[__Mutable__[Item]]: ...

    @overload
    @setdoc.basic
    def __setitem__(self: Self, key: int, value: Item, /) -> None: ...
    @overload
    @setdoc.basic
    def __setitem__(
        self: Self, key: Slice[int], value: abc.Iterable[Item], /
    ) -> None: ...
    @setdoc.basic
    def __setitem__(
        self: Self,
        key: int | Slice[int],
        value: Item | abc.Iterable[Item],
        /,
    ) -> None:
        with self.__mutate__() as mutable:
            mutable[key] = value  # type: ignore

    @setdoc.basic
    def insert(self: Self, index: int, item: Item, /) -> None:
        with self.__mutate__() as mutable:
            mutable.insert(index, item)


### LIST-LIKE ###
class ListLike[Item](Sequence[Item]):
    """Provide a base class for customized list-likes."""

    __slots__ = ()

    type __Frozen__[FrozenItem] = tuple[FrozenItem, ...]
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
    def __eq__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, ListLike):
            return self.__frozen__() == other.__frozen__()
        else:
            return NotImplemented

    @abstractmethod
    @setdoc.basic
    def __frozen__(self: Self, /) -> __Frozen__[Item]: ...

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


class FrozenListLike[Item](ListLike[Item], abc.Hashable):
    """Provide a base class for customized frozen list-likes."""

    __slots__ = ()

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.__frozen__())


class MutableListLike[Item](ListLike[Item], MutableSequence[Item]):
    """Provide a base class for customized mutable list-likes."""

    __slots__ = ()

    type __Mutable__[MutableItem] = list[MutableItem]

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
        with self.__mutate__() as mutable:
            del mutable[key]

    @setdoc.basic
    def __frozen__(self: Self) -> MutableListLike.__Frozen__[Item]:
        with self.__mutate__() as mutable:
            return tuple(mutable)

    @setdoc.basic
    def __imul__(self: Self, other: SupportsIndex, /) -> Self:
        with self.__mutate__() as mutable:
            mutable *= other
        return self

    @setdoc.basic
    def __init__(self: Self, data: abc.Iterable[Item] = (), /) -> None:
        with self.__mutate__() as mutable:
            mutable.extend(data)

    @abstractmethod
    @setdoc.basic
    def __mutate__(self: Self, /) -> ContextManager[__Mutable__[Item]]: ...

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
        with self.__mutate__() as mutable:
            mutable[key] = value  # type: ignore

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self)

    @setdoc.basic
    def insert(self: Self, index: SupportsIndex, item: Item, /) -> None:
        with self.__mutate__() as mutable:
            mutable.insert(index, item)

    @setdoc.basic
    def sort(self: Self, /, *, key: Any = None, reverse: bool = False) -> None:
        # list.sort reveals Overload(
        #     def [_T, SupportsRichComparisonT <: _typeshed.SupportsDunderLT[Any] | _typeshed.SupportsDunderGT[Any]] (self: list[SupportsRichComparisonT], *, key: None =, reverse: bool =),
        #     def [_T] (self: list[_T], *, key: def (_T) -> _typeshed.SupportsDunderLT[Any] | _typeshed.SupportsDunderGT[Any], reverse: bool =),
        # )
        with self.__mutate__() as mutable:
            mutable.sort(key=key, reverse=reverse)


### LIST-SLOT ###


class ListSlot[Item](ListLike[Item]):
    """Provide slotted list-like class."""

    __slots__ = ("_slot",)

    _slot: ListSlot.__Frozen__[Item]

    @setdoc.basic
    def __frozen__(self: Self) -> ListSlot.__Frozen__[Item]:
        return self._slot


class FrozenListSlot[Item](ListSlot[Item], FrozenListLike[Item]):
    """Provide a base class for customized frozen data-holds."""

    __slots__ = ()

    @setdoc.basic
    def __init__(self: Self, data: abc.Iterable[Item] = (), /) -> None:
        self._slot = tuple(data)


class MutableListSlot[Item](ListSlot[Item], MutableListLike[Item]):
    """Provide slotted mutable list-like class."""

    __slots__ = ()

    @contextmanager
    @setdoc.basic
    def __mutate__(self: Self, /) -> abc.Generator[list[Item], None, None]:
        slot = list(getattr(self, "_slot", ()))
        yield slot
        self._slot = tuple(slot)
