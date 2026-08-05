"""Provide provides base classes for customized collections."""

from __future__ import annotations

__all__: list[str] = [
    "Collection",
    "DictLike",
    "FrozenDictLike",
    "FrozenDictSlot",
    "FrozenListLike",
    "FrozenListSlot",
    "FrozenSetLike",
    "FrozenSetSlot",
    "ListLike",
    "Mapping",
    "MutableDictLike",
    "MutableDictSlot",
    "MutableListLike",
    "MutableListSlot",
    "MutableMapping",
    "MutableObjectLike",
    "MutableSequence",
    "MutableSet",
    "MutableSetLike",
    "MutableSetSlot",
    "Object",
    "Sequence",
    "Set",
    "SetLike",
]

from abc import ABCMeta, abstractmethod
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
from frozendict import frozendict

### PROTOCOLS ###


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


class SupportsKeysAndGetitem[Key, Value](Protocol):
    """Provide protocol supporting keys and __getitem__."""

    @setdoc.basic
    def __getitem__(self: Self, key: Key, /) -> Value: ...
    @setdoc.basic
    def keys(self: Self, /) -> abc.Iterable[Key]: ...


class Collection_Frozen[Item](
    abc.Sized,
    abc.Iterable[Item],
    Protocol,
):
    @setdoc.basic
    def __contains__(self: Self, other: Never, /) -> bool: ...


class MutableSet_Mutable[Item: abc.Hashable](Protocol):
    @setdoc.basic
    def add(self: Self, item: Item, /) -> object: ...
    @setdoc.basic
    def discard(self: Self, item: abc.Hashable, /) -> object: ...


class Mapping_Frozen[Key, Value](Collection_Frozen[Key], Protocol):
    @setdoc.basic
    def __getitem__(self: Self, key: abc.Hashable, /) -> Value: ...
class MutableMapping_Mutable[Key_, Value_](
    Protocol,
):
    @setdoc.basic
    def __delitem__(self: Self, key: Key_ | str, /) -> object: ...
    @setdoc.basic
    def __setitem__(
        self: Self, key: Key_ | str, value: Optional[Value_], /
    ) -> object: ...
class Sequence_Frozen[Item](
    Collection_Frozen[Item],
    Protocol,
):
    @overload
    @setdoc.basic
    def __getitem__(self: Self, key: int, /) -> Item: ...
    @overload
    @setdoc.basic
    def __getitem__(self: Self, key: Slice[int], /) -> abc.Sequence[Item]: ...
    @setdoc.basic
    def __getitem__(
        self: Self,
        key: int | Slice[int],
        /,
    ) -> Item | abc.Sequence[Item]: ...


class MutableSequence_Mutable[Item](Protocol):
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
    def __getitem__(self: Self, key: int, /) -> Item: ...
    @overload
    @setdoc.basic
    def __getitem__(
        self: Self, key: Slice[int], /
    ) -> abc.MutableSequence[Item]: ...
    @setdoc.basic
    def __getitem__(
        self: Self,
        key: int | Slice[int],
        /,
    ) -> Item | abc.MutableSequence[Item]: ...
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
    ) -> None: ...
    @setdoc.basic
    def insert(self: Self, index: int, item: Item, /) -> None: ...


### TYPE ALIASES ###

type Dict[Key, Value] = dict[Key | str, Optional[Value]]

type DictInit[Key, Value] = (
    SupportsKeysAndGetitem[Key | str, Optional[Value]]
    | abc.Iterable[tuple[Key | str, Optional[Value]]]
)

type FrozenDict[Key, Value] = frozendict[Key | str, Optional[Value]]

type Slice[Index] = slice[Optional[Index], Optional[Index], Optional[Index]]


### OBJECT ###
class Object[Frozen](metaclass=ABCMeta):
    """Provide abc for custom object."""

    __slots__ = ()

    @abstractmethod
    @setdoc.basic
    def __frozen__(self: Self, /) -> Frozen: ...


class MutableObject[Frozen, Mutable](Object[Frozen]):
    """Provide abc for custom mutable object."""

    __slots__ = ()

    @abstractmethod
    @setdoc.basic
    def __mutate__(self: Self, /) -> ContextManager[Mutable]: ...


### OBJECT-LIKE ###


class MutableObjectLike[Frozen, Mutable](
    MutableObject[Frozen, Mutable],
):
    """Provide abc for custom mutable object-like."""

    __slots__ = ()

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, other: Self, /) -> None: ...
    @setdoc.basic
    def copy(self: Self, /) -> Self:
        return type(self)(self)


### OBJECT-HOLD ###


class ObjectSlot[Frozen](
    Object[Frozen],
):
    """Provide slotted abc for custom object-like."""

    __slots__ = ("_slot",)
    _slot: Frozen


### COLLECTION ###


class Collection[Item](
    abc.Sized,
    abc.Iterable[Item],
    abc.Container[object],
    Object[Collection_Frozen[Item]],
):
    """Provide abc for custom collection."""

    @setdoc.basic
    def __contains__(self: Self, other: object, /) -> bool:
        try:
            return other in self.__frozen__()  # type: ignore[operator]
        except TypeError:
            return other in (x for x in self)  # type: ignore[operator]

    @setdoc.basic
    def __iter__(self: Self, /) -> abc.Iterator[Item]:
        return iter(self.__frozen__())

    @setdoc.basic
    def __len__(self: Self, /) -> int:
        return len(self.__frozen__())


### SET ###


class Set[Item: abc.Hashable](Collection[Item], abc.Set[Item]):
    """Provide abc for custom set."""

    __slots__ = ()


class MutableSet[Item: abc.Hashable](
    Set[Item],
    abc.MutableSet[Item],
    MutableObject[Collection_Frozen[Item], MutableSet_Mutable[Item]],
):
    """Provide abc for custom mutable set."""

    __slots__ = ()

    @setdoc.basic
    def add(self: Self, item: Item, /) -> None:
        with self.__mutate__() as mutable:
            mutable.add(item)

    @setdoc.basic
    def discard(self: Self, item: abc.Hashable, /) -> None:
        with self.__mutate__() as mutable:
            mutable.discard(item)


### SET-LIKE ###


class SetLike[Item: abc.Hashable](Set[Item]):
    """Provide abc for custom set-like."""

    __slots__ = ()

    @abstractmethod
    @setdoc.basic
    def __frozen__(self: Self, /) -> frozenset[Item]: ...
    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: abc.Iterable[Item] = (), /) -> None: ...
    @setdoc.basic
    def difference(self: Self, /, *others: abc.Iterable[abc.Hashable]) -> Self:
        return type(self)(self.__frozen__().difference(*others))

    @setdoc.basic
    def intersection(
        self: Self, /, *others: abc.Iterable[abc.Hashable]
    ) -> Self:
        return type(self)(self.__frozen__().intersection(*others))

    @setdoc.basic
    def issubset(self: Self, other: abc.Iterable[abc.Hashable], /) -> bool:
        return self.__frozen__().issubset(other)

    @setdoc.basic
    def issuperset(self: Self, other: abc.Iterable[abc.Hashable], /) -> bool:
        return self.__frozen__().issuperset(other)

    @setdoc.basic
    def symmetric_difference(self: Self, other: abc.Iterable[Item], /) -> Self:
        return type(self)(self.__frozen__().symmetric_difference(other))

    @setdoc.basic
    def union(self: Self, /, *others: abc.Iterable[Item]) -> Self:
        return type(self)(self.__frozen__().union(*others))


class FrozenSetLike[Item: abc.Hashable](SetLike[Item], abc.Hashable):
    """Provide abc for custom frozen set-like."""

    __slots__ = ()

    @setdoc.basic
    def __hash__(self: Self, /) -> int:
        return hash(self.__frozen__())


class MutableSetLike[Item: abc.Hashable](
    SetLike[Item],
    MutableObjectLike[frozenset[Item], set[Item]],
    MutableSet[Item],
):
    """Provide abc for custom mutable set-like."""

    __slots__ = ()

    @setdoc.basic
    def __frozen__(self: Self, /) -> frozenset[Item]:
        with self.__mutate__() as mutable:
            return frozenset(mutable)

    @setdoc.basic
    def __init__(self: Self, data: abc.Iterable[Item] = (), /) -> None:
        with self.__mutate__() as mutable:
            mutable.update(data)

    @setdoc.basic
    def difference_update(
        self: Self, /, *others: abc.Iterable[abc.Hashable]
    ) -> None:
        with self.__mutate__() as mutable:
            mutable.difference_update(*others)

    @setdoc.basic
    def intersection_update(
        self: Self, /, *others: abc.Iterable[abc.Hashable]
    ) -> None:
        with self.__mutate__() as mutable:
            mutable.intersection_update(*others)

    @setdoc.basic
    def symmetric_difference_update(
        self: Self, other: abc.Iterable[Item], /
    ) -> None:
        with self.__mutate__() as mutable:
            mutable.symmetric_difference_update(other)

    @setdoc.basic
    def update(self: Self, /, *others: abc.Iterable[Item]) -> None:
        with self.__mutate__() as mutable:
            mutable.update(*others)


### SET-SLOT ###


class FrozenSetSlot[Item](
    FrozenSetLike[Item],
    ObjectSlot[frozenset[Item]],
):
    """Provide slotted frozen set-like."""

    __slots__ = ()

    @setdoc.basic
    def __frozen__(self: Self, /) -> frozenset[Item]:
        return self._slot

    @setdoc.basic
    def __init__(self: Self, data: abc.Iterable[Item] = (), /) -> None:
        self._slot = frozenset(data)


class MutableSetSlot[Item](
    MutableSetLike[Item],
    ObjectSlot[frozenset[Item]],
):
    """Provide slotted mutable set-like."""

    __slots__ = ()

    @contextmanager
    @setdoc.basic
    def __mutate__(
        self: Self,
        /,
    ) -> abc.Generator[set[Item], None, None]:
        slot: set[Item]
        slot = set(getattr(self, "_slot", ()))
        yield slot
        self._slot = frozenset(slot)


### MAPPING ###


class Mapping[Key: abc.Hashable, Value](
    Collection[Key],
    abc.Mapping[Key, Value],
):
    """Provide abc for custom mapping."""

    __slots__ = ()

    @abstractmethod
    @setdoc.basic
    def __frozen__(self: Self, /) -> Mapping_Frozen[Key, Value]: ...
    @setdoc.basic
    def __getitem__(self: Self, key: abc.Hashable, /) -> Value:
        return self.__frozen__()[key]


class MutableMapping[Key: abc.Hashable, Value](
    Mapping[Key, Value],
    abc.MutableMapping[Key | str, Optional[Value]],
    MutableObject[FrozenDict[Key, Value], Dict[Key, Value]],
):
    """Provide abc for custom mutable mapping."""

    __slots__ = ()

    @setdoc.basic
    def __delitem__(self: Self, key: Key | str, /) -> None:
        with self.__mutate__() as mutable:
            del mutable[key]

    @setdoc.basic
    def __setitem__(
        self: Self, key: Key | str, value: Optional[Value], /
    ) -> None:
        with self.__mutate__() as mutable:
            mutable[key] = value


### DICT-LIKE ###


class DictLike[Key: abc.Hashable, Value](
    Mapping[Key | str, Optional[Value]],
):
    """Provide abc for custom dict-like."""

    __slots__ = ()

    @abstractmethod
    @setdoc.basic
    def __frozen__(self: Self, /) -> FrozenDict[Key, Value]:  # type: ignore[override]
        ...

    @abstractmethod
    @setdoc.basic
    def __init__(
        self: Self,
        data: DictInit[Key, Value] = (),
        /,
        **kwargs: Value,
    ): ...
    @setdoc.basic
    def __or__[Key_, Value_](
        self: Self,
        other: DictInit[Key_, Value_],
        /,
    ) -> DictLike[Key | Key_, Value | Value_]:
        data: FrozenDict[Key, Value]
        try:
            data = frozendict(other)  # type: ignore[arg-type]
        except TypeError:
            return NotImplemented
        return type(self)(  # type: ignore[return-value]
            self.__frozen__() | data
        )

    @classmethod
    @setdoc.basic
    def fromkeys(
        cls: type[Self],
        iterable: abc.Iterable[Key | str],
        value: Optional[Value] = None,
        /,
    ) -> Self:
        return cls(dict.fromkeys(iterable, value))


class FrozenDictLike[Key: abc.Hashable, Value](
    DictLike[Key, Value],
    abc.Hashable,
):
    """Provide abc for custom frozen dict-like."""

    __slots__ = ()

    @setdoc.basic
    def __hash__(self: Self, /) -> int:
        return hash(self.__frozen__())


class MutableDictLike[Key: abc.Hashable, Value](
    DictLike[Key, Value],
    MutableObjectLike[FrozenDict[Key, Value], Dict[Key, Value]],
    MutableMapping[Key, Value],
):
    """Provide abc for custom mutable dict-like."""

    __slots__ = ()

    @setdoc.basic
    def __frozen__(  # type: ignore[override]
        self: Self,
        /,
    ) -> FrozenDict[Key, Value]:
        with self.__mutate__() as mutable:
            return frozendict(mutable)

    @setdoc.basic
    def __init__(
        self: Self,
        data: DictInit[Key, Value] = (),
        /,
        **kwargs: Optional[Value],
    ):
        self.update(data, **kwargs)

    @setdoc.basic
    def __ior__(  # type: ignore[override]
        self: Self,
        other: DictInit[Key, Value],
        /,
    ) -> Self:
        with self.__mutate__() as mutable:
            mutable |= other
        return self

    @setdoc.basic
    def popitem(self: Self, /) -> tuple[Key | str, Optional[Value]]:
        # for most dict d
        # dict.popitem(d) and collections.abc.MutableMapping.popitem(d)
        # behave differently
        with self.__mutate__() as mutable:
            return mutable.popitem()


### DICT-SLOT ###


class FrozenDictSlot[Key: abc.Hashable, Value](
    FrozenDictLike[Key, Value],
    ObjectSlot[FrozenDict[Key, Value]],
):
    """Provide slotted frozen dict-like."""

    __slots__ = ()

    @setdoc.basic
    def __frozen__(  # type: ignore[override]
        self: Self,
    ) -> FrozenDict[Key, Value]:
        return self._slot

    @setdoc.basic
    def __init__(
        self: Self,
        data: DictInit[Key, Value] = (),
        /,
        **kwargs: Optional[Value],
    ) -> None:
        self._slot = frozendict(data, **kwargs)  # type: ignore[arg-type]


class MutableDictSlot[Key: abc.Hashable, Value](
    MutableDictLike[Key, Value],
    ObjectSlot[FrozenDict[Key, Value]],
):
    """Provide slotted mutable dict-like."""

    __slots__ = ()

    @contextmanager
    @setdoc.basic
    def __mutate__(
        self: Self,
        /,
    ) -> abc.Generator[Dict[Key, Value], None, None]:
        slot: Dict[Key, Value]
        slot = dict(getattr(self, "_slot", ()))
        yield slot
        self._slot = frozendict(slot)


### SEQUENCE ###


class Sequence[Item](Collection[Item], abc.Sequence[Item]):
    """Provide abc for customized sequence."""

    __slots__ = ()

    @abstractmethod
    @setdoc.basic
    def __frozen__(self: Self, /) -> Sequence_Frozen[Item]: ...
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


class MutableSequence[Item](
    Sequence[Item],
    abc.MutableSequence[Item],
    MutableObject[Sequence_Frozen[Item], MutableSequence_Mutable[Item]],
):
    """Provide abc for custom mutable sequence."""

    __slots__ = ()

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
        with self.__mutate__() as mutable:
            return mutable[key]

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
    """Provide abc for custom list-like."""

    __slots__ = ()

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
    def __frozen__(self: Self, /) -> tuple[Item, ...]:
        # __frozen__ has to be tuple to allow covariance
        ...

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
    def __init__(self: Self, data: abc.Iterable[Item] = (), /) -> None: ...

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
    """Provide abc for custom frozen list-like."""

    __slots__ = ()

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.__frozen__())


class MutableListLike[Item](
    ListLike[Item],
    MutableObjectLike[tuple[Item, ...], list[Item]],
    MutableSequence[Item],
):
    """Provide abc for custom mutable list-like."""

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
        with self.__mutate__() as mutable:
            del mutable[key]

    @setdoc.basic
    def __frozen__(self: Self) -> tuple[Item, ...]:
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


class FrozenListSlot[Item](
    FrozenListLike[Item],
    ObjectSlot[tuple[Item, ...]],
):
    """Provide slotted frozen list-like."""

    __slots__ = ()

    @setdoc.basic
    def __frozen__(self: Self) -> tuple[Item, ...]:
        return self._slot

    @setdoc.basic
    def __init__(self: Self, data: abc.Iterable[Item] = (), /) -> None:
        self._slot = tuple(data)


class MutableListSlot[Item](
    MutableListLike[Item],
    ObjectSlot[tuple[Item, ...]],
):
    """Provide slotted mutable list-like."""

    __slots__ = ()

    @contextmanager
    @setdoc.basic
    def __mutate__(self: Self, /) -> abc.Generator[list[Item], None, None]:
        slot = list(getattr(self, "_slot", ()))
        yield slot
        self._slot = tuple(slot)
