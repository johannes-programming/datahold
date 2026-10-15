"""Generic slot-backed sets, mappings, and sequences (Python 3.12+).

Install the required third-party dependency with ``pip install frozendict``.
"""

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
    "MutableDictLike",
    "MutableDictSlot",
    "MutableListLike",
    "MutableListSlot",
    "MutableSetLike",
    "MutableSetSlot",
    "SetLike",
]

from abc import abstractmethod
from collections import abc
from contextlib import AbstractContextManager, contextmanager
from reprlib import recursive_repr
from types import NotImplementedType
from typing import Any, Never, Protocol, Self, SupportsIndex, overload

from frozendict import frozendict

### TYPING ###


# the dublication is a concession to mypy mistyping Mapping.__getitem__ and frozendict.__getitem__
class SupportsKeysAndGetItem[Key: abc.Hashable, Value](Protocol):
    def __getitem__(self: Self, key: abc.Hashable, /) -> Value: ...
    def keys(self: Self, /) -> abc.Iterable[Key]: ...


type DictInit[Key, Value] = SupportsKeysAndGetItem[Key, Value] | abc.Iterable[
    tuple[Key, Value]
]
type Slice[Index] = slice[Index, Index, Index]


class SupportsGE[Other](Protocol):
    def __ge__(self: Self, other: Other, /) -> bool: ...
class SupportsGT[Other](Protocol):
    def __gt__(self: Self, other: Other, /) -> bool: ...
class SupportsLE[Other](Protocol):
    def __le__(self: Self, other: Other, /) -> bool: ...
class SupportsLT[Other](Protocol):
    def __lt__(self: Self, other: Other, /) -> bool: ...


class CollectionData[Item](
    abc.Sized, abc.Iterable[Item], abc.Container[Never], Protocol
): ...


### BASE ###


class Collection[Item](abc.Sized, abc.Iterable[Item], abc.Container[object]):
    __slots__ = ()

    def __contains__(self: Self, other: object, /) -> bool:
        try:
            return other in self.__frozen__()
        except TypeError:
            return False

    @abstractmethod
    def __frozen__(self: Self, /) -> CollectionData[Item]: ...
    def __iter__(self: Self, /) -> abc.Iterator[Item]:
        return iter(self.__frozen__())

    def __len__(self: Self, /) -> int:
        return len(self.__frozen__())


### SET-LIKE ###


class SetLike[Item: abc.Hashable](Collection[Item], abc.Set[Item]):
    """Shared read-only set API; construction and storage remain abstract."""

    __slots__ = ()

    # __and__ is inherited from abc.Set (via the overridable _from_iterable).
    # __contains__ is inherited
    # __eq__ is inherited from abc.Set.
    @abstractmethod
    def __frozen__(self: Self, /) -> frozenset[Item]:
        """Return a frozen snapshot of this set."""

    # __ge__ is inherited from abc.Set.
    # __gt__ is inherited from abc.Set.
    @abstractmethod
    def __init__(self: Self, data: abc.Iterable[Item] = (), /) -> None:
        """Initialize the set from data."""

    # __iter__ is inherited

    # __le__ is inherited from abc.Set.
    # __len__ is inherited

    # __lt__ is inherited from abc.Set.
    # __ne__ is inherited from object (negates __eq__).
    # __or__ is inherited from abc.Set (via _from_iterable).
    # __rand__ is inherited from abc.Set (via _from_iterable).
    @recursive_repr()
    def __repr__(self: Self, /) -> str:
        return f"{type(self).__name__}({set(self.__frozen__())})"

    # __ror__ is inherited from abc.Set (via _from_iterable).
    # __rsub__ is inherited from abc.Set (via _from_iterable).
    # __rxor__ is inherited from abc.Set (via _from_iterable).
    # __sub__ is inherited from abc.Set (via _from_iterable).
    @classmethod
    def __type__[Item_: abc.Hashable](
        cls: type[Any], data: abc.Iterable[Item_], /
    ) -> SetLike[Item_]:
        return cls(data)  # type: ignore[no-any-return]

    # __xor__ is inherited from abc.Set (via _from_iterable).
    @classmethod
    def _from_iterable[Item_: abc.Hashable](
        cls: type[Any], data: abc.Iterable[Item_], /
    ) -> SetLike[Item_]:
        return cls.__type__(data)  # type: ignore[no-any-return]

    def difference(
        self: Self, /, *others: abc.Iterable[Item]
    ) -> SetLike[Item]:
        return type(self).__type__(self.__frozen__().difference(*others))

    def intersection(
        self: Self, /, *others: abc.Iterable[Item]
    ) -> SetLike[Item]:
        return type(self).__type__(self.__frozen__().intersection(*others))

    # isdisjoint is inherited from abc.Set.
    def issubset(self: Self, other: abc.Iterable[Item], /) -> bool:
        return self.__frozen__().issubset(other)

    def issuperset(self: Self, other: abc.Iterable[Item], /) -> bool:
        return self.__frozen__().issuperset(other)

    def symmetric_difference(
        self: Self, other: abc.Iterable[Item], /
    ) -> SetLike[Item]:
        return type(self).__type__(
            self.__frozen__().symmetric_difference(other)
        )

    def union(self: Self, /, *others: abc.Iterable[Item]) -> SetLike[Item]:
        return type(self).__type__(self.__frozen__().union(*others))


class FrozenSetLike[Item: abc.Hashable](SetLike[Item]):
    """Hashable abstract set specialization."""

    __slots__ = ()

    # __frozen__ is inherited as an abstract requirement from SetLike.
    def __hash__(self: Self, /) -> int:
        return hash(self.__frozen__())

    # __init__ is inherited as an abstract requirement from SetLike.


class FrozenSetSlot[Item: abc.Hashable](FrozenSetLike[Item]):
    """A frozenset held in one instance slot."""

    __slots__ = ("_slot",)

    def __frozen__(self: Self, /) -> frozenset[Item]:
        return self._slot

    # __hash__ is inherited from FrozenSetLike.
    def __init__(self: Self, data: abc.Iterable[Item] = (), /) -> None:
        self._slot = frozenset(data)


class MutableSetLike[Item: abc.Hashable](SetLike[Item], abc.MutableSet[Item]):
    """Mutable set operations committed through a context manager."""

    __slots__ = ()

    def __frozen__(self: Self, /) -> frozenset[Item]:
        mutable: set[Item]
        with self.__mutate__() as mutable:
            return frozenset(mutable)

    __hash__ = None  # type: ignore[assignment]

    def __iand__(  # type: ignore[misc, unused-ignore]
        self: Self,
        other: abc.Set[Item],
        /,
    ) -> MutableSetLike[Item]:
        mutable: set[Item]
        if not isinstance(other, abc.Set):
            return NotImplemented
        with self.__mutate__() as mutable:
            mutable.intersection_update(other)
        return self

    def __init__(self: Self, data: abc.Iterable[Item] = (), /) -> None:
        self.update(data)

    def __ior__(  # type: ignore[misc,override]
        self: Self,
        other: abc.Set[Item],
        /,
    ) -> MutableSetLike[Item]:
        mutable: set[Item]
        if not isinstance(other, abc.Set):
            return NotImplemented
        with self.__mutate__() as mutable:
            mutable.update(other)
        return self

    def __isub__(  # type: ignore[misc, unused-ignore]
        self: Self,
        other: abc.Set[Item],
        /,
    ) -> MutableSetLike[Item]:
        mutable: set[Item]
        if not isinstance(other, abc.Set):
            return NotImplemented
        with self.__mutate__() as mutable:
            mutable.difference_update(other)
        return self

    def __ixor__(  # type: ignore[misc,override]
        self: Self,
        other: abc.Set[Item],
        /,
    ) -> MutableSetLike[Item]:
        mutable: set[Item]
        if not isinstance(other, abc.Set):
            return NotImplemented
        with self.__mutate__() as mutable:
            mutable.symmetric_difference_update(other)
        return self

    @abstractmethod
    def __mutate__(self: Self, /) -> AbstractContextManager[set[Item]]:
        """Yield a mutable working set and commit on successful exit."""

    @classmethod
    def __type__[Item_: abc.Hashable](
        cls: type[Any], data: abc.Iterable[Item_], /
    ) -> MutableSetLike[Item_]:
        # redoing the same method is necessary because copy must return MutableSetLike[Item]
        return cls(data)  # type: ignore[no-any-return]

    def add(self: Self, item: Item, /) -> None:
        mutable: set[Item]
        with self.__mutate__() as mutable:
            mutable.add(item)

    # clear is inherited from abc.MutableSet.
    def copy(self: Self, /) -> MutableSetLike[Item]:
        return type(self).__type__(self.__frozen__())

    def difference_update(self: Self, /, *others: abc.Iterable[Item]) -> None:
        mutable: set[Item]
        with self.__mutate__() as mutable:
            mutable.difference_update(*others)

    def discard(self: Self, item: abc.Hashable, /) -> None:
        mutable: set[Item]
        with self.__mutate__() as mutable:
            mutable.discard(item)

    def intersection_update(
        self: Self, /, *others: abc.Iterable[Item]
    ) -> None:
        mutable: set[Item]
        with self.__mutate__() as mutable:
            mutable.intersection_update(*others)

    def pop(self: Self, /) -> Item:
        mutable: set[Item]
        with self.__mutate__() as mutable:
            return mutable.pop()

    # remove is inherited from abc.MutableSet.
    def symmetric_difference_update(
        self: Self, other: abc.Iterable[Item], /
    ) -> None:
        mutable: set[Item]
        with self.__mutate__() as mutable:
            mutable.symmetric_difference_update(other)

    def update(self: Self, /, *others: abc.Iterable[Item]) -> None:
        mutable: set[Item]
        with self.__mutate__() as mutable:
            mutable.update(*others)


class MutableSetSlot[Item: abc.Hashable](MutableSetLike[Item]):
    """Mutable set with transactional replacement of a frozenset slot."""

    __slots__ = ("_slot",)

    def __frozen__(self: Self, /) -> frozenset[Item]:
        return self._slot

    # __init__ is inherited from MutableSetLike.
    @contextmanager
    def __mutate__(self: Self, /) -> abc.Iterator[set[Item]]:
        mutable: set[Item]
        mutable = set(getattr(self, "_slot", ()))
        yield mutable
        self._slot = frozenset(mutable)


### DICT-LIKE ###


class DictLike[Key: abc.Hashable, Value](
    Collection[Key], abc.Mapping[Key, Value]
):
    """Shared read-only dictionary interface."""

    __slots__ = ()

    # __contains__ is inherited
    # __eq__ is inherited from abc.Mapping.
    @abstractmethod
    def __frozen__(self: Self, /) -> frozendict[Key, Value]:
        """Return an immutable mapping snapshot."""

    def __getitem__(self: Self, key: abc.Hashable, /) -> Value:
        return self.__frozen__()[key]  # type: ignore[index]

    @overload
    def __init__(
        self: Self,
        data: DictInit[Key, Value] = (),
        /,
    ) -> None: ...

    @overload
    def __init__[Key_](
        self: DictLike[Key_ | str, Value],
        data: DictInit[Key_ | str, Value] = (),
        /,
        **kwargs: Value,
    ) -> None: ...

    @abstractmethod
    def __init__(
        self: Any,
        data: Any = (),
        /,
        **kwargs: Any,
    ) -> None:
        """Construct the mapping from pairs, a mapping and/or keywords."""

    # __iter__ is inherited
    # __len__ is inherited
    # __ne__ is inherited from object (negates __eq__).
    def __or__[Key_, Value_](
        self: Self, other: DictLike[Key_, Value_], /
    ) -> DictLike[Key | Key_, Value | Value_]:
        if not isinstance(other, DictLike):
            return NotImplemented
        return type(self).__type__(
            self.__frozen__() | other.__frozen__()  # type: ignore[arg-type]
        )

    @recursive_repr()
    def __repr__(self: Self, /) -> str:
        return f"{type(self).__name__}({dict(self.__frozen__())})"

    def __reversed__(self: Self, /) -> abc.Iterator[Key]:
        return reversed(tuple(self))

    # __ror__ is unnecessary because of __or__

    @classmethod
    def __type__[Key_: abc.Hashable, Value_](
        cls: type[Any], data: DictInit[Key_, Value_], /
    ) -> DictLike[Key_, Value_]:
        return cls(data)  # type: ignore[no-any-return]

    @overload
    @classmethod
    def fromkeys[Key_](
        cls: type[Any], keys: abc.Iterable[Key_], /
    ) -> DictLike[Key_, None]: ...

    @overload
    @classmethod
    def fromkeys[Key_, Value_](
        cls: type[Any], keys: abc.Iterable[Key_], value: Value_, /
    ) -> DictLike[Key_, Value_]: ...

    @classmethod
    def fromkeys(
        cls: type[Any], keys: Any, value: Any = None, /
    ) -> DictLike[Any, Any]:
        return cls.__type__(dict.fromkeys(keys, value))  # type: ignore[no-any-return]

    # get is inherited from abc.Mapping.
    # items is inherited from abc.Mapping.
    # keys is inherited from abc.Mapping.
    # values is inherited from abc.Mapping.


class FrozenDictLike[Key: abc.Hashable, Value](DictLike[Key, Value]):
    """Hashable abstract mapping specialization."""

    __slots__ = ()

    # __frozen__ is inherited as an abstract requirement from DictLike.
    def __hash__(self: Self, /) -> int:
        return hash(self.__frozen__())

    # __init__ is inherited as an abstract requirement from DictLike.


class FrozenDictSlot[Key: abc.Hashable, Value](FrozenDictLike[Key, Value]):
    """A frozendict held in one instance slot."""

    __slots__ = ("_slot",)

    def __frozen__(self: Self, /) -> frozendict[Key, Value]:
        return self._slot

    # __hash__ is inherited from FrozenDictLike.
    def __init__(
        self: Self, data: DictInit[Key, Value] = (), /, **kwargs: Value
    ) -> None:
        self._slot = frozendict(
            data,  # type: ignore[arg-type]
            **kwargs,
        )


class MutableDictLike[Key: abc.Hashable, Value](
    DictLike[Key, Value], abc.MutableMapping[Key, Value]
):
    """Mutable mapping operations performed on a temporary dict."""

    __slots__ = ()

    def __delitem__(self: Self, key: abc.Hashable, /) -> None:
        mutable: dict[Key, Value]
        with self.__mutate__() as mutable:
            del mutable[key]  # type: ignore[arg-type]

    def __frozen__(self: Self, /) -> frozendict[Key, Value]:
        mutable: dict[Key, Value]
        with self.__mutate__() as mutable:
            return frozendict(mutable)

    __hash__ = None  # type: ignore[assignment]

    def __init__(
        self: Self, data: DictInit[Key, Value] = (), /, **kwargs: Value
    ) -> None:
        self.update(data, **kwargs)

    def __ior__(  # type: ignore[misc, override]
        self: Self, other: DictInit[Key, Value], /
    ) -> MutableDictLike[Key, Value]:
        self.update(other)
        return self

    @abstractmethod
    def __mutate__(self: Self, /) -> AbstractContextManager[dict[Key, Value]]:
        """Yield a mutable working dictionary and commit on normal exit."""

    def __or__[Key_, Value_](
        self: Self, other: DictLike[Key_, Value_], /
    ) -> MutableDictLike[Key | Key_, Value | Value_]:
        if not isinstance(other, DictLike):
            return NotImplemented
        return type(self).__type__(
            self.__frozen__() | other.__frozen__()  # type: ignore[arg-type]
        )

    def __setitem__(self: Self, key: Key, value: Value, /) -> None:
        mutable: dict[Key, Value]
        with self.__mutate__() as mutable:
            mutable[key] = value

    @classmethod
    def __type__[Key_: abc.Hashable, Value_](
        cls: type[Any],
        data: DictInit[Key_, Value_],
        /,
    ) -> MutableDictLike[Key_, Value_]:
        # redoing the same method is necessary because copy must return MutableDictLike[Item]
        return cls(data)  # type: ignore[no-any-return]

    # clear is inherited from abc.MutableMapping.

    def copy(self: Self, /) -> DictLike[Key, Value]:
        return type(self).__type__(self.__frozen__())  # type: ignore[arg-type]

    # pop is inherited from abc.MutableMapping.
    def popitem(self: Self, /) -> tuple[Key, Value]:
        mutable: dict[Key, Value]
        with self.__mutate__() as mutable:
            return mutable.popitem()

    # setdefault is inherited from abc.MutableMapping.

    @overload  # type: ignore[override]
    def update(
        self: Self,
        other: DictInit[Key, Value] = (),
        /,
    ) -> None: ...
    @overload
    def update[Key_](
        self: MutableDictLike[Key_ | str, Value],
        other: DictInit[Key_ | str, Value] = (),
        /,
        **kwargs: Value,
    ) -> None: ...
    def update(
        self: Any, other: DictInit[Any, Any] = (), /, **kwargs: Value
    ) -> None:
        mutable: dict[Key, Value]
        with self.__mutate__() as mutable:
            mutable.update(other, **kwargs)


class MutableDictSlot[Key: abc.Hashable, Value](MutableDictLike[Key, Value]):
    """Mutable dictionary backed by a frozen dictionary slot."""

    __slots__ = ("_slot",)

    def __frozen__(self: Self, /) -> frozendict[Key, Value]:
        return self._slot

    # __init__ is inherited from MutableDictLike.
    @contextmanager
    def __mutate__(self: Self, /) -> abc.Iterator[dict[Key, Value]]:
        mutable: dict[Key, Value]
        mutable = dict(getattr(self, "_slot", ()))
        yield mutable
        self._slot = frozendict(mutable)


### LIST-LIKE ###


class ListLike[Item](Collection[Item], abc.Sequence[Item]):
    """Shared read-only sequence with cross-variant tuple-style comparison."""

    __slots__ = ()

    def __add__(self: Self, other: ListLike[Item], /) -> ListLike[Item]:
        if not isinstance(other, ListLike):
            return NotImplemented
        return type(self).__type__(self.__frozen__() + other.__frozen__())

    # __contains__ is inherited
    def __eq__(self: Self, other: object, /) -> NotImplementedType | bool:
        if not isinstance(other, ListLike):
            return NotImplemented
        return self.__frozen__() == other.__frozen__()

    @abstractmethod
    def __frozen__(self: Self, /) -> tuple[Item, ...]:
        """Return an immutable tuple snapshot."""

    @overload
    def __ge__[Item_](
        self: ListLike[SupportsGE[Item_]],
        other: ListLike[Item_],
        /,
    ) -> bool: ...
    @overload
    def __ge__(self: Self, other: ListLike[SupportsLE[Item]], /) -> bool: ...
    def __ge__(self: Any, other: ListLike[Any], /) -> Any:
        if not isinstance(other, ListLike):
            return NotImplemented
        return self.__frozen__() >= other.__frozen__()

    @overload
    def __getitem__(self: Self, index: SupportsIndex, /) -> Item: ...

    @overload
    def __getitem__(
        self: Self, index: Slice[None | SupportsIndex], /
    ) -> ListLike[Item]: ...

    def __getitem__(
        self: Self, index: SupportsIndex | Slice[None | SupportsIndex], /
    ) -> Any:
        if isinstance(index, SupportsIndex):
            return self.__frozen__()[index]
        else:
            return type(self).__type__(self.__frozen__()[index])

    @overload
    def __gt__[Item_](
        self: ListLike[SupportsGT[Item_]],
        other: ListLike[Item_],
        /,
    ) -> bool: ...
    @overload
    def __gt__(self: Self, other: ListLike[SupportsLT[Item]], /) -> bool: ...
    def __gt__(self: Any, other: ListLike[Any], /) -> Any:
        if not isinstance(other, ListLike):
            return NotImplemented
        return self.__frozen__() > other.__frozen__()

    @abstractmethod
    def __init__(self: Self, data: abc.Iterable[Item] = (), /) -> None:
        """Initialize from an iterable."""

    __iter__ = abc.Sequence.__iter__

    @overload
    def __le__[Item_](
        self: ListLike[SupportsLE[Item_]],
        other: ListLike[Item_],
        /,
    ) -> bool: ...
    @overload
    def __le__(self: Self, other: ListLike[SupportsGE[Item]], /) -> bool: ...
    def __le__(self: Any, other: ListLike[Any], /) -> Any:
        if not isinstance(other, ListLike):
            return NotImplemented
        return self.__frozen__() <= other.__frozen__()

    @overload
    def __lt__[Item_](
        self: ListLike[SupportsLT[Item_]],
        other: ListLike[Item_],
        /,
    ) -> bool: ...
    @overload
    def __lt__(self: Self, other: ListLike[SupportsGT[Item]], /) -> bool: ...
    def __lt__(self: Any, other: ListLike[Any], /) -> Any:
        if not isinstance(other, ListLike):
            return NotImplemented
        return self.__frozen__() < other.__frozen__()

    def __mul__(self: Self, other: SupportsIndex, /) -> ListLike[Item]:
        return type(self).__type__(self.__frozen__() * other)

    __rmul__ = __mul__

    # __ne__ is inherited from object (negates __eq__).
    @recursive_repr()
    def __repr__(self: Self, /) -> str:
        return f"{type(self).__name__}({list(self.__frozen__())})"

    # __reversed__ is inherited from abc.Sequence.

    @classmethod
    def __type__[Item_](
        cls: type[Any],
        data: abc.Iterable[Item_],
        /,
    ) -> ListLike[Item_]:
        return cls(data)  # type: ignore[no-any-return]

    # count is inherited from abc.Sequence.
    # index is inherited from abc.Sequence.


class FrozenListLike[Item](ListLike[Item]):
    """Hashable abstract sequence specialization."""

    __slots__ = ()

    # __frozen__ is inherited as an abstract requirement from ListLike.
    def __hash__(self: Self, /) -> int:
        return hash(self.__frozen__())

    # __init__ is inherited as an abstract requirement from ListLike.


class FrozenListSlot[Item](FrozenListLike[Item]):
    """A tuple stored in one instance slot."""

    __slots__ = ("_slot",)

    def __frozen__(self: Self, /) -> tuple[Item, ...]:
        return self._slot

    # __hash__ is inherited from FrozenListLike.
    def __init__(self: Self, data: abc.Iterable[Item] = (), /) -> None:
        self._slot = tuple(data)


class MutableListLike[Item](ListLike[Item], abc.MutableSequence[Item]):
    """Mutable sequence operations committed through a temporary list."""

    __slots__ = ()

    def __delitem__(
        self: Self, index: SupportsIndex | Slice[None | SupportsIndex], /
    ) -> None:
        mutable: list[Item]
        with self.__mutate__() as mutable:
            del mutable[index]

    def __frozen__(self: Self, /) -> tuple[Item, ...]:
        mutable: list[Item]
        with self.__mutate__() as mutable:
            return tuple(mutable)

    @overload
    def __getitem__(self: Self, index: SupportsIndex, /) -> Item: ...

    @overload
    def __getitem__(
        self: Self, index: Slice[None | SupportsIndex], /
    ) -> MutableListLike[Item]: ...

    def __getitem__(
        self: Self, index: SupportsIndex | Slice[None | SupportsIndex], /
    ) -> Any:
        if isinstance(index, SupportsIndex):
            return self.__frozen__()[index]
        else:
            return type(self).__type__(self.__frozen__()[index])

    __hash__ = None  # type: ignore[assignment]

    # __iadd__ is inherited from abc.MutableSequence.
    def __imul__(self: Self, other: SupportsIndex, /) -> MutableListLike[Item]:
        mutable: list[Item]
        with self.__mutate__() as mutable:
            mutable *= other
        return self

    def __init__(self: Self, data: abc.Iterable[Item] = (), /) -> None:
        self.extend(data)

    @abstractmethod
    def __mutate__(self: Self, /) -> AbstractContextManager[list[Item]]:
        """Yield a mutable working list and commit on successful exit."""

    @overload
    def __setitem__(
        self: Self, index: SupportsIndex, data: Item, /
    ) -> None: ...

    @overload
    def __setitem__(
        self: Self,
        index: Slice[None | SupportsIndex],
        data: abc.Iterable[Item],
        /,
    ) -> None: ...

    def __setitem__(
        self: Any,
        index: Any,
        data: Any,
        /,
    ) -> None:
        mutable: list[Item]
        with self.__mutate__() as mutable:
            mutable[index] = data

    @classmethod
    def __type__[Item_](
        cls: type[Any],
        data: abc.Iterable[Item_],
        /,
    ) -> MutableListLike[Item_]:
        # redoing the same method is necessary because copy must return MutableListLike[Item]
        return cls(data)  # type: ignore[no-any-return]

    # append is inherited from abc.MutableSequence.
    # clear is inherited from abc.MutableSequence.
    def copy(self: Self, /) -> MutableListLike[Item]:
        return type(self).__type__(self.__frozen__())

    def extend(self: Self, data: abc.Iterable[Item], /) -> None:
        mutable: list[Item]
        with self.__mutate__() as mutable:
            mutable.extend(data)

    def insert(self: Self, index: SupportsIndex, item: Item, /) -> None:
        mutable: list[Item]
        with self.__mutate__() as mutable:
            mutable.insert(index, item)

    # pop is inherited from abc.MutableSequence.
    # remove is inherited from abc.MutableSequence.
    # reverse is inherited from abc.MutableSequence.
    @overload
    def sort[Item_: SupportsGT[Self]](
        self: MutableListLike[Item_],
        /,
        *,
        key: None = None,
        reverse: bool = False,
    ) -> None: ...
    @overload
    def sort[Item_: SupportsLT[Self]](
        self: MutableListLike[Item_],
        /,
        *,
        key: None = None,
        reverse: bool = False,
    ) -> None: ...
    @overload
    def sort[T: SupportsLT[Self]](
        self: Self,
        /,
        *,
        key: abc.Callable[[Item], T],
        reverse: bool = False,
    ) -> None: ...
    @overload
    def sort[T: SupportsGT[Self]](
        self: Self,
        /,
        *,
        key: abc.Callable[[Item], T],
        reverse: bool = False,
    ) -> None: ...
    def sort(
        self: Any,
        /,
        *,
        key: Any = None,
        reverse: Any = False,
    ) -> None:
        mutable: list[Item]
        with self.__mutate__() as mutable:
            mutable.sort(key=key, reverse=reverse)


class MutableListSlot[Item](MutableListLike[Item]):
    """Mutable sequence with transactional replacement of a tuple slot."""

    __slots__ = ("_slot",)

    def __frozen__(self: Self, /) -> tuple[Item, ...]:
        return self._slot

    # __init__ is inherited from MutableListLike.
    @contextmanager
    def __mutate__(self: Self, /) -> abc.Iterator[list[Item]]:
        mutable: list[Item]
        mutable = list(getattr(self, "_slot", ()))
        yield mutable
        self._slot = tuple(mutable)
