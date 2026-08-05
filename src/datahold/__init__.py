"""Provide provides base classes for customized collections."""

from __future__ import annotations

__all__: list[str] = [
    "Collection",
    "DictLike",
    "DictSlot",
    "FrozenDictLike",
    "FrozenDictSlot",
    "FrozenListLike",
    "FrozenListSlot",
    "FrozenSetLike",
    "FrozenSetSlot",
    "ListLike",
    "ListSlot",
    "Mapping",
    "MutableDictLike",
    "MutableDictSlot",
    "MutableListLike",
    "MutableListSlot",
    "MutableMapping",
    "MutableSequence",
    "MutableSet",
    "MutableSetLike",
    "MutableSetSlot",
    "Sequence",
    "Set",
    "SetLike",
    "SetSlot",
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


class SupportsKeysAndGetitem[Key, Value](Protocol):
    """Provide protocol supporting keys and __getitem__."""

    @setdoc.basic
    def __getitem__(self: Self, key: Key, /) -> Value: ...
    @setdoc.basic
    def keys(self: Self, /) -> abc.Iterable[Key]: ...


type DictInit[Key, Value] = (
    SupportsKeysAndGetitem[Key | str, Optional[Value]]
    | abc.Iterable[tuple[Key | str, Optional[Value]]]
)

type Slice[Index] = slice[Optional[Index], Optional[Index], Optional[Index]]


### OBJECT


class Object[Frozen](metaclass=ABCMeta):
    __slots__ = ()

    @abstractmethod
    @setdoc.basic
    def __frozen__(self: Self, /) -> Frozen: ...


class FrozenObject[Frozen](Object[Frozen], abc.Hashable):
    __slots__ = ()


class MutableObject[Frozen, Mutable](Object[Frozen]):
    __slots__=()
    @abstractmethod
    @setdoc.basic
    def __mutate__(self: Self, /) -> ContextManager[Mutable]: ...


### OBJECT-LIKE ###


class ObjectLike[Frozen](Object[Frozen]):
    __slots__ = ()

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Self, /) -> None: ...


class FrozenObjectLike[Frozen](ObjectLike[Frozen], FrozenObject[Frozen]):
    __slots__ =()
    
class MutableObjectLike[Frozen, Mutable](
    ObjectLike[Frozen], 
    MutableObject[Frozen, Mutable],
):
    __slots__ = ()

    @setdoc.basic
    def copy(self: Self, /) -> Self:
        return type(self)(self)

### OBJECT-SLOT
class ObjectSlot[Frozen](ObjectLike[Frozen]):
    __slots__=("_data")
    _data:Frozen

class FrozenObjectSlot[Frozen](ObjectSlot[Frozen], FrozenObjectLike[Frozen]):
    __slots__=()

class MutableObjectSlot[Frozen, Mutable](
    ObjectSlot[Frozen], 
    MutableObjectLike[Frozen, Mutable],
):
    __slots__=()

### COLLECTION ###


class __Collection_Frozen__[Item](
    abc.Sized,
    abc.Iterable[Item],
    Protocol,
):
    @setdoc.basic
    def __contains__(self: Self, other: Never, /) -> bool: ...
class Collection[Item](
    Object[__Collection_Frozen__[Item]],
    abc.Sized,
    abc.Iterable[Item],
    abc.Container[object],
):
    """Provide abc for custom collection."""

    type __Frozen__[Item] = __Collection_Frozen__[Item]

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


class Set[Item: abc.Hashable](
    Collection[Item], 
    abc.Set[Item],
):
    """Provide abc for custom set."""

    __slots__ = ()


class __MutableSet_Mutable__[Item_: abc.Hashable](Protocol):
    @setdoc.basic
    def add(self: Self, item: Item_, /) -> object: ...
    @setdoc.basic
    def discard(self: Self, item: abc.Hashable, /) -> object: ...
class MutableSet[Item: abc.Hashable](
    Set[Item], 
    MutableObject[__Collection_Frozen__[Item], __MutableSet_Mutable__[Item]],
    abc.MutableSet[Item],
):
    """Provide abc for custom mutable set."""

    __slots__ = ()

    type __Mutable__[Item] = __MutableSet_Mutable__[Item]

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
    type __Frozen__[Item_] = frozenset[Item_]

    @abstractmethod
    @setdoc.basic
    def __frozen__(self: Self, /) -> __Frozen__[Item]: ...
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
    def issubset(self: Self, other: abc.Iterable[abc.Hashable], /) -> Self:
        return type(self)(self.__frozen__().issubset(other))  # type: ignore

    @setdoc.basic
    def issuperset(self: Self, other: abc.Iterable[abc.Hashable], /) -> Self:
        return type(self)(self.__frozen__().issuperset(other))  # type: ignore

    @setdoc.basic
    def symmetric_difference(self: Self, other: abc.Iterable[Item], /) -> Self:
        return type(self)(self.__frozen__().symmetric_difference(other))

    @setdoc.basic
    def union(self: Self, /, *others: abc.Iterable[Item]) -> Self:
        return type(self)(self.__frozen__().union(others))  # type: ignore


class FrozenSetLike[Item: abc.Hashable](SetLike[Item], abc.Hashable):
    """Provide abc for custom frozen set-like."""

    __slots__ = ()

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(self.__frozen__())


class MutableSetLike[Item: abc.Hashable](
    SetLike[Item],
    MutableSet[Item],
    MutableLike[frozenset[Item], set[Item]],
):
    """Provide abc for custom mutable set-like."""

    __slots__ = ()
    type __Mutable__[Item_] = set[Item_]

    @setdoc.basic
    def __frozen__(self: Self, /) -> MutableSetLike.__Frozen__[Item]:
        with self.__mutate__() as mutable:
            return frozenset(mutable)

    @setdoc.basic
    def __init__(self: Self, data: abc.Iterable[Item] = (), /) -> None:
        with self.__mutate__() as mutable:
            mutable.update(data)

    @abstractmethod
    @setdoc.basic
    def __mutate__(self: Self, /) -> ContextManager[__Mutable__[Item]]: ...

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

class FrozenSetSlot[Item](FrozenSetLike[Item], Slot[frozenset[Item]]):
    """Provide slotted frozen set-like."""

    __slots__ = ()

    @setdoc.basic
    def __frozen__(self: Self) -> FrozenSetSlot.__Frozen__[Item]:
        return self._slot

    @setdoc.basic
    def __init__(self: Self, data: abc.Iterable[Item] = (), /) -> None:
        self._slot : FrozenSetSlot.__Frozen__[Item]= frozenset(data)


class MutableSetSlot[Item](MutableSetLike[Item], Slot[frozenset[Item]]):
    """Provide slotted mutable set-like."""

    __slots__ = ()

    @contextmanager
    @setdoc.basic
    def __mutate__(
        self: Self,
        /,
    ) -> abc.Generator[MutableSetSlot.__Mutable__[Item], None, None]:
        mutable: MutableSetSlot.__Mutable__[Item]
        mutable = set(getattr(self, "_slot", ()))
        yield mutable
        self._slot = frozenset(mutable)


### MAPPING ###


class Mapping[Key: abc.Hashable, Value](
    Collection[Key],
    abc.Mapping[Key, Value],
):
    """Provide abc for custom mapping."""

    __slots__ = ()

    @setdoc.basic
    class __Frozen__[FrozenKey, FrozenValue](
        Collection.__Frozen__[FrozenKey], Protocol
    ):
        @setdoc.basic
        def __getitem__(self: Self, key: abc.Hashable, /) -> FrozenValue: ...
    @abstractmethod
    @setdoc.basic
    def __frozen__(self: Self, /) -> __Frozen__[Key, Value]: ...
    @setdoc.basic
    def __getitem__(self: Self, key: abc.Hashable, /) -> Value:
        return self.__frozen__()[key]


class MutableMapping[Key: abc.Hashable, Value](
    Mapping[Key, Value],
    abc.MutableMapping[Key | str, Optional[Value]],
):
    """Provide abc for custom mutable mapping."""

    __slots__ = ()

    @setdoc.basic
    class __Mutable__[Key_, Value_](
        Protocol,
    ):
        @setdoc.basic
        def __delitem__(self: Self, key: Key_ | str, /) -> object: ...
        @setdoc.basic
        def __setitem__(
            self: Self, key: Key_ | str, value: Optional[Value_], /
        ) -> object: ...

    @setdoc.basic
    def __delitem__(self: Self, key: Key | str, /) -> None:
        with self.__mutate__() as mutable:
            del mutable[key]

    @abstractmethod
    @setdoc.basic
    def __mutate__(self: Self) -> ContextManager[__Mutable__[Key, Value]]: ...
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
    type __Frozen__[FrozenKey, FrozenValue] = frozendict[
        FrozenKey | str, Optional[FrozenValue]
    ]

    @abstractmethod
    @setdoc.basic
    def __frozen__(self: Self, /) -> __Frozen__[Key, Value]: ...  # type: ignore[override]
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
        data: DictLike.__Frozen__[Key_, Value_]
        try:
            data = frozendict(other)  # type: ignore[arg-type]
        except TypeError:
            return NotImplemented
        return type(self)(  # type: ignore[return-value]
            self.__frozen__() | data  # type: ignore[operator]
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
    MutableMapping[Key, Value],
    MutableLike[
        frozendict[Key | str, Optional[Value]],
        dict[Key | str, Optional[Value]],
    ],
):
    """Provide abc for custom mutable dict-like."""

    __slots__ = ()
    type __Mutable__[Key_: abc.Hashable, Value_] = dict[
        Key_ | str, Optional[Value_]
    ]

    @setdoc.basic
    def __frozen__(  # type: ignore[override]
        self: Self,
        /,
    ) -> MutableDictLike.__Frozen__[Key, Value]:
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

    @abstractmethod
    @setdoc.basic
    def __mutate__(
        self: Self, /
    ) -> ContextManager[__Mutable__[Key, Value]]: ...


### DICT-SLOT ###



class FrozenDictSlot[Key: abc.Hashable, Value](
    FrozenDictLike[Key, Value],
    Slot[FrozenDictLike.__Frozen__[Key, Value]]
):
    """Provide slotted frozen dict-like."""

    __slots__ = ()

    @setdoc.basic
    def __frozen__(  # type: ignore[override]
        self: Self,
    ) -> FrozenDictLike.__Frozen__[Key, Value]:
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
    Slot[MutableDictLike.__Mutable__[Key, Value]],
):
    """Provide slotted mutable dict-like."""

    __slots__ = ()

    @contextmanager
    @setdoc.basic
    def __mutate__(
        self: Self,
        /,
    ) -> abc.Generator[MutableDictSlot.__Mutable__[Key, Value], None, None]:
        mutable: MutableDictSlot.__Mutable__[Key, Value]
        mutable = dict(getattr(self, "_slot", ()))
        yield mutable
        self._slot = frozendict(mutable)


### SEQUENCE ###


class Sequence[Item](Collection[Item], abc.Sequence[Item]):
    """Provide abc for customized sequence."""

    __slots__ = ()

    @setdoc.basic
    class __Frozen__[Item_](
        Collection.__Frozen__[Item_],
        Protocol,
    ):
        @overload
        @setdoc.basic
        def __getitem__(self: Self, key: int, /) -> Item_: ...
        @overload
        @setdoc.basic
        def __getitem__(
            self: Self, key: Slice[int], /
        ) -> abc.Sequence[Item_]: ...
        @setdoc.basic
        def __getitem__(
            self: Self,
            key: int | Slice[int],
            /,
        ) -> Item_ | abc.Sequence[Item_]: ...
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
    """Provide abc for custom mutable sequence."""

    __slots__ = ()

    @setdoc.basic
    class __Mutable__[Item_](Protocol):
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
        def __getitem__(self: Self, key: int, /) -> Item_: ...
        @overload
        @setdoc.basic
        def __getitem__(
            self: Self, key: Slice[int], /
        ) -> abc.MutableSequence[Item_]: ...
        @setdoc.basic
        def __getitem__(
            self: Self,
            key: int | Slice[int],
            /,
        ) -> Item_ | abc.MutableSequence[Item_]: ...
        @overload
        @setdoc.basic
        def __setitem__(self: Self, key: int, value: Item_, /) -> None: ...
        @overload
        @setdoc.basic
        def __setitem__(
            self: Self, key: Slice[int], value: abc.Iterable[Item_], /
        ) -> None: ...
        @setdoc.basic
        def __setitem__(
            self: Self,
            key: int | Slice[int],
            value: Item_ | abc.Iterable[Item_],
            /,
        ) -> None: ...
        @setdoc.basic
        def insert(self: Self, index: int, item: Item_, /) -> None: ...

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
    """Provide abc for custom list-like."""

    __slots__ = ()

    type __Frozen__[Item_] = tuple[Item_, ...]
    # Frozen has to be tuple to allow covariance

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
    MutableSequence[Item],
    MutableLike[tuple[Item, ...], list[Item]],
):
    """Provide abc for custom mutable list-like."""

    __slots__ = ()

    type __Mutable__[Item_] = list[Item_]

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
    Slot[FrozenListLike.__Frozen__[Item]],
):
    """Provide slotted frozen list-like."""

    __slots__ = ()

    @setdoc.basic
    def __frozen__(self: Self) -> FrozenListSlot.__Frozen__[Item]:
        return self._slot
    
    @setdoc.basic
    def __init__(self: Self, data: abc.Iterable[Item] = (), /) -> None:
        self._slot = tuple(data)


class MutableListSlot[Item](
    MutableListLike[Item],
    Slot[MutableListLike.__Frozen__[Item]],
):
    """Provide slotted mutable list-like."""

    __slots__ = ()

    @contextmanager
    @setdoc.basic
    def __mutate__(self: Self, /) -> abc.Generator[list[Item], None, None]:
        mutable = list(getattr(self, "_slot", ()))
        yield mutable
        self._slot = tuple(mutable)
