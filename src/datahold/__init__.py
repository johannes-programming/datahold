"""Provide easy abc for custom collections."""

from __future__ import annotations

__all__: list[str] = [
    "Collection",
    "DictLike",
    "FrozenDictLike",
    "FrozenListLike",
    "FrozenMapping",
    "FrozenSet",
    "FrozenSetLike",
    "ListLike",
    "Mapping",
    "MutableDictLike",
    "MutableListLike",
    "MutableMapping",
    "MutableSequence",
    "MutableSet",
    "MutableSetLike",
    "Sequence",
    "Set",
    "SetLike",
]

import enum
from abc import ABCMeta, abstractmethod
from collections import abc
from contextlib import contextmanager
from types import NotImplementedType
from typing import (
    Any,
    Never,
    Optional,
    Protocol,
    Self,
    SupportsIndex,
    cast,
    overload,
)

import setdoc
from frozendict import frozendict

### UTILS ###


class Copyable(Protocol):
    @setdoc.basic
    def copy(self: Self) -> Self: ...


class DataContextManager[Data](Protocol):
    @setdoc.basic
    def __enter__(self: Self) -> Data: ...
    @setdoc.basic
    def __exit__(
        self: Self, exc_type: Any, exc_value: Any, traceback: Any
    ) -> None: ...


class DataSlot[Data](Protocol):
    def __data__(self: Self) -> DataContextManager[Data]: ...


class Missing(enum.Enum):
    missing = None


type Slice[Index] = slice[Optional[Index], Optional[Index], Optional[Index]]


class SupportsKeysAndGetitem[Key, Value](Protocol):

    @setdoc.basic
    def __getitem__(self: Self, key: Never, /) -> Value: ...

    @setdoc.basic
    def keys(self: Self) -> abc.Iterable[Key]: ...


###


def getDataSlot[Data: Copyable](
    *,
    factory: abc.Callable[[], Data],
    slotname: str,
) -> type[DataSlot[Data]]:
    class Ans:
        __slots__ = (slotname,)

        @contextmanager
        @setdoc.basic
        def __data__(
            self: Self,
        ) -> abc.Generator[Data, None, None]:
            data: Data | Missing
            data = getattr(self, slotname, Missing.missing)
            if isinstance(data, Missing):
                data = factory()
            else:
                data = cast(Data, data.copy())
            yield data
            setattr(self, slotname, data)

    Ans.__name__ = "DataSlot"
    return Ans  # type: ignore[return-value]


### COLLECTION ###


class Collection[Item](
    abc.Sized,
    abc.Iterable[Item],
    abc.Container[object],
    metaclass=ABCMeta,
):
    """Provide an easy abc for a custom collection."""

    __slots__ = ()

    @setdoc.basic
    class OneWay[OneWayItem](
        abc.Sized,
        abc.Iterable[OneWayItem],
        abc.Container[Never],
        Protocol,
    ): ...

    @setdoc.basic
    def __contains__(self: Self, other: object, /) -> bool:
        data = self.__one_way__()
        try:
            return other in data
        except TypeError:
            return other in (x for x in data)  # type: ignore[operator]

    @setdoc.basic
    def __iter__(self: Self, /) -> abc.Iterator[Item]:
        return iter(self.__one_way__())

    @setdoc.basic
    def __len__(self: Self, /) -> int:
        return len(self.__one_way__())

    @abstractmethod
    @setdoc.basic
    def __one_way__(self: Self) -> OneWay[Item]: ...


### SET ###


class Set[Item](
    Collection[Item],
    abc.Set[Item],
):
    """Provide an easy abc for a custom (abstract) set."""

    __slots__ = ()


class FrozenSet[Item: abc.Hashable](Set[Item], abc.Hashable):
    """Provide easy abc for custom frozen set."""

    __slots__ = ()

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return self._hash()


class MutableSet[Item: abc.Hashable](
    Set[Item],
    abc.MutableSet[Item],
):
    """Provide easy abc for custom mutable set-like."""

    __slots__ = ()

    @setdoc.basic
    class Mutable[MutableItem](Protocol):
        @setdoc.basic
        def add(self: Self, item: MutableItem, /) -> object: ...
        @setdoc.basic
        def discard(self: Self, item: abc.Hashable, /) -> object: ...

    @abstractmethod
    @setdoc.basic
    def __mutable__(self: Self) -> DataContextManager[Mutable[Item]]: ...

    @setdoc.basic
    def add(self: Self, item: Item, /) -> None:
        with self.__mutable__() as data:
            data.add(item)

    @setdoc.basic
    def discard(self: Self, item: abc.Hashable, /) -> None:
        with self.__mutable__() as data:
            data.discard(item)


### SET LIKE ###


class SetLike[Item: abc.Hashable](Set[Item]):
    """Provide an easy abc for custom set-like."""

    __slots__ = ()

    type Init[InitItem] = abc.Iterable[InitItem]

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Init[Item] = (), /) -> None: ...

    @setdoc.basic
    def __repr__(self: Self, /) -> str:
        return f"{type(self).__name__}({set(self)!r})"

    @setdoc.basic
    def difference(self: Self, /, *others: abc.Iterable[abc.Hashable]) -> Self:
        return type(self)(set(self).difference(*others))

    @setdoc.basic
    def intersection(
        self: Self, /, *others: abc.Iterable[abc.Hashable]
    ) -> Self:
        return type(self)(set(self).intersection(*others))

    @setdoc.basic
    def issubset(self: Self, other: abc.Iterable[abc.Hashable], /) -> bool:
        return set(self).issubset(other)

    @setdoc.basic
    def issuperset(self: Self, other: abc.Iterable[abc.Hashable], /) -> bool:
        return set(self).issuperset(other)

    @setdoc.basic
    def symmetric_difference(
        self: Self,
        other: abc.Iterable[Item],
        /,
    ) -> Self:
        return type(self)(set(self).symmetric_difference(other))

    @setdoc.basic
    def union(self: Self, /, *others: abc.Iterable[Item]) -> Self:
        return type(self)(set(self).union(*others))


class FrozenSetLike[Item: abc.Hashable](SetLike[Item], FrozenSet[Item]):
    """Provide easy abc for custom frozen set-like."""

    __slots__ = ()


class MutableSetLike[Item: abc.Hashable](
    SetLike[Item],
    MutableSet[Item],
):
    """Provide easy abc for custom mutable set-like."""

    __slots__ = ()

    @setdoc.basic
    class Mutable[MutableData](
        MutableSet.Mutable[MutableData],
        Protocol,
    ):
        @setdoc.basic
        def difference_update(
            self: Self,
            /,
            *others: abc.Iterable[abc.Hashable],
        ) -> object: ...

        @setdoc.basic
        def intersection_update(
            self: Self, /, *others: abc.Iterable[abc.Hashable]
        ) -> object: ...

        @setdoc.basic
        def symmetric_difference_update(
            self: Self, other: abc.Iterable[Item], /
        ) -> object: ...

        @setdoc.basic
        def update(self: Self, /, *others: abc.Iterable[Item]) -> object: ...

    @abstractmethod
    @setdoc.basic
    def __mutable__(self: Self) -> DataContextManager[Mutable[Item]]: ...

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self)

    @setdoc.basic
    def difference_update(
        self: Self,
        /,
        *others: abc.Iterable[abc.Hashable],
    ) -> None:
        with self.__mutable__() as data:
            data.difference_update(*others)

    @setdoc.basic
    def intersection_update(
        self: Self, /, *others: abc.Iterable[abc.Hashable]
    ) -> None:
        with self.__mutable__() as data:
            data.intersection_update(*others)

    @setdoc.basic
    def symmetric_difference_update(
        self: Self, other: abc.Iterable[Item], /
    ) -> None:
        with self.__mutable__() as data:
            data.symmetric_difference_update(other)

    @setdoc.basic
    def update(self: Self, /, *others: abc.Iterable[Item]) -> None:
        with self.__mutable__() as data:
            data.update(*others)

    __init__ = update


### MAPPING ###
class Mapping[Key: abc.Hashable, Value](
    Collection[Key], abc.Mapping[Key, Value]
):
    """Provide an easy abc for a custom mapping."""

    __slots__ = ()

    @setdoc.basic
    class OneWay[OneWayKey, OneWayValue](
        Collection.OneWay[OneWayKey],
        Protocol,
    ):
        """Provide set data protocol."""

        @setdoc.basic
        def __getitem__(self: Self, key: Never, /) -> OneWayValue: ...

    @setdoc.basic
    def __getitem__(self: Self, key: object, /) -> Value:
        data = self.__one_way__()
        try:
            return data[key]  # type: ignore[index]
        except TypeError:
            raise KeyError(key) from None

    @abstractmethod
    @setdoc.basic
    def __one_way__(self: Self) -> OneWay[Key, Value]: ...


class FrozenMapping[Key: abc.Hashable, Value](
    Mapping[Key, Value],
    abc.Hashable,
):
    """Provide an easy abc for a custom frozen mapping."""

    __slots__ = ()

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(frozendict(self.items()))


class MutableMapping[Key: abc.Hashable, Value](
    Mapping[Key, Value],
    abc.MutableMapping[Key, Value],
):
    """Provide easy abc for custom mutable mapping."""

    __slots__ = ()

    @setdoc.basic
    class Mutable[MutableKey, MutableValue](Protocol):
        """Provide mutable mapping data protocol."""

        @setdoc.basic
        def __delitem__(self: Self, key: MutableKey, /) -> object: ...
        @setdoc.basic
        def __setitem__(
            self: Self, key: MutableKey, value: MutableValue, /
        ) -> object: ...

    @setdoc.basic
    def __delitem__(self: Self, key: Key, /) -> None:
        with self.__mutable__() as data:
            del data[key]

    @abstractmethod
    @setdoc.basic
    def __mutable__(self: Self) -> DataContextManager[Mutable[Key, Value]]: ...

    @setdoc.basic
    def __setitem__(
        self: Self,
        key: Key,
        value: Value,
        /,
    ) -> None:
        # what to do if Key includes unhashable types?
        with self.__mutable__() as data:
            data[key] = value


### DICT LIKE ###


class DictLike[Key: abc.Hashable, Value](
    Mapping[Key | str, Optional[Value]],
):
    """Provide an easy abc for custom dict-like."""

    __slots__ = ()

    type Init[DataKey, DataValue] = (
        SupportsKeysAndGetitem[DataKey | str, Optional[DataValue]]
        | abc.Iterable[tuple[DataKey | str, Optional[DataValue]]]
    )

    @setdoc.basic
    class OneWay[OneWayKey, OneWayValue](
        Mapping.OneWay[OneWayKey | str, Optional[OneWayValue]],
        Protocol,
    ):
        ...

        @setdoc.basic
        def __or__(
            self: Self,
            other: DictLike.OneWay[OneWayKey, OneWayValue],
            /,
        ) -> Self: ...

        # __ror__ is unnecessary because of how __or__ is defined

    @abstractmethod
    @setdoc.basic
    def __init__(
        self: Self,
        data: Init[Key, Value] = (),
        /,
        **kwargs: Optional[Value],
    ) -> None: ...

    @abstractmethod
    @setdoc.basic
    def __one_way__(self: Self) -> OneWay[Key, Value]: ...

    @setdoc.basic
    def __or__(
        self: Self,
        other: object,
        /,
    ) -> NotImplementedType | Self:
        if isinstance(other, DictLike):
            return type(self)(dict(self) | dict(other))
        else:
            return NotImplemented

    @setdoc.basic
    def __repr__(self: Self, /) -> str:
        return f"{type(self).__name__}({dict(self)!r})"

    # __ror__ is unnecessary because of how __or__ is defined

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
    FrozenMapping[Key | str, Optional[Value]],
):
    """Provide easy abc for custom frozen dict-like."""

    __slots__ = ()


class MutableDictLike[Key: abc.Hashable, Value](
    DictLike[Key, Value],
    MutableMapping[Key | str, Optional[Value]],
):
    """Provide easy abc for custom mutable dict-like."""

    __slots__ = ()

    @setdoc.basic
    class Mutable[MutableKey, MutableValue](
        MutableMapping.Mutable[MutableKey | str, Optional[MutableValue]],
        Protocol,
    ):
        @setdoc.basic
        def __ior__(
            self: Self,
            other: DictLike.OneWay[MutableKey, MutableValue],
            /,
        ) -> object: ...

    __init__ = MutableMapping.update
    # dict.update reveals the overloads
    #     def [_KT, _VT] (typing.MutableMapping[_KT, _VT], _typeshed.SupportsKeysAndGetItem[_KT, _VT]),
    #     def [_KT, _VT] (_typeshed.SupportsGetItem[str, _VT], _typeshed.SupportsKeysAndGetItem[str, _VT], **kwargs: _VT),
    #     def [_KT, _VT] (typing.MutableMapping[_KT, _VT], typing.Iterable[tuple[_KT, _VT]]),
    #     def [_KT, _VT] (_typeshed.SupportsGetItem[str, _VT], typing.Iterable[tuple[str, _VT]], **kwargs: _VT),
    #     def [_KT, _VT] (_typeshed.SupportsGetItem[str, _VT], **kwargs: _VT)

    @setdoc.basic
    def __ior__(
        self: Self,
        other: DictLike[Key, Value],
        /,
    ) -> Self:
        with self.__mutable__() as data:
            data.__ior__(other.__one_way__())
        return self

    @abstractmethod
    @setdoc.basic
    def __mutable__(self: Self) -> DataContextManager[Mutable[Key, Value]]: ...

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self)


### SEQUENCE ###


class Sequence[Item](
    Collection[Item],
    abc.Sequence[Item],
):
    """Provide an easy abc for a custom sequence."""

    __slots__ = ()

    @setdoc.basic
    class OneWay[OneWayItem](
        Collection.OneWay[OneWayItem],
        Protocol,
    ):
        @overload
        @setdoc.basic
        def __getitem__(self: Self, key: int, /) -> OneWayItem: ...
        @overload
        @setdoc.basic
        def __getitem__(
            self: Self, key: Slice[int], /
        ) -> abc.Sequence[OneWayItem]: ...
        @setdoc.basic
        def __getitem__(
            self: Self, key: int | Slice[int], /
        ) -> OneWayItem | abc.Sequence[OneWayItem]: ...

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
        return self.__one_way__()[key]

    @abstractmethod
    @setdoc.basic
    def __one_way__(self: Self) -> OneWay[Item]: ...


class MutableSequence[Item](
    Sequence[Item],
    abc.MutableSequence[Item],
):
    """Provide easy abc for custom mutable sequence."""

    __slots__ = ()

    @setdoc.basic
    class Mutable[MutableItem](Protocol):
        """Provide mutable sequence data protocol."""

        @setdoc.basic
        def __delitem__(
            self: Self, key: SupportsIndex | Slice[SupportsIndex], /
        ) -> object: ...
        @overload
        @setdoc.basic
        def __setitem__(
            self: Self, key: SupportsIndex, value: MutableItem, /
        ) -> object: ...
        @overload
        @setdoc.basic
        def __setitem__(
            self: Self,
            key: Slice[SupportsIndex],
            value: abc.Iterable[MutableItem],
            /,
        ) -> object: ...
        @setdoc.basic
        def __setitem__(
            self: Self,
            key: SupportsIndex | Slice[SupportsIndex],
            value: MutableItem | abc.Iterable[MutableItem],
            /,
        ) -> object: ...
        @setdoc.basic
        def insert(
            self: Self, index: SupportsIndex, item: MutableItem, /
        ) -> object: ...

    @setdoc.basic
    class OneWay[OneWayItem](Sequence.OneWay[OneWayItem], Protocol):
        @overload
        @setdoc.basic
        def __getitem__(self: Self, key: int, /) -> OneWayItem: ...
        @overload
        @setdoc.basic
        def __getitem__(
            self: Self, key: Slice[int], /
        ) -> abc.MutableSequence[OneWayItem]: ...
        @setdoc.basic
        def __getitem__(
            self: Self, key: int | Slice[int], /
        ) -> OneWayItem | abc.MutableSequence[OneWayItem]: ...

    @setdoc.basic
    def __delitem__(
        self: Self, other: SupportsIndex | Slice[SupportsIndex], /
    ) -> None:
        with self.__mutable__() as data:
            del data[other]

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
        return self.__one_way__()[key]

    @abstractmethod
    @setdoc.basic
    def __mutable__(self: Self) -> DataContextManager[Mutable[Item]]: ...

    @abstractmethod
    @setdoc.basic
    def __one_way__(self: Self) -> OneWay[Item]: ...

    @overload
    @setdoc.basic
    def __setitem__(
        self: Self, key: SupportsIndex, value: Item, /
    ) -> None: ...

    @overload
    @setdoc.basic
    def __setitem__(
        self: Self,
        key: Slice[SupportsIndex],
        value: abc.Iterable[Item],
        /,
    ) -> None: ...

    @setdoc.basic
    def __setitem__(
        self: Self,
        key: SupportsIndex | Slice[SupportsIndex],
        value: Item | abc.Iterable[Item],
        /,
    ) -> None:
        with self.__mutable__() as data:
            data[key] = value  # type: ignore[index, assignment]

    @setdoc.basic
    def insert(self: Self, index: SupportsIndex, item: Item, /) -> None:
        with self.__mutable__() as data:
            data.insert(index, item)


### LIST LIKE ###


class ListLike[Item](Sequence[Item]):
    """Provide an easy abc for custom list-like."""

    __slots__ = ()

    type Init[InitItem] = abc.Iterable[InitItem]

    @setdoc.basic
    def __add__(self: Self, other: object, /) -> Self:
        # list.__add__ reveals Overload(
        #     def [_T] (list[_T], list[_T]) -> list[_T],
        #     def [_T, _S] (list[_T], list[_S]) -> list[_S | _T],
        # )
        # tuple.__add__ reveals Overload(
        #     def [_T_co] (tuple[_T_co, ...], tuple[_T_co, ...]) -> tuple[_T_co, ...],
        #     def [_T_co, _T] (tuple[_T_co, ...], tuple[_T, ...]) -> tuple[_T_co | _T, ...],
        # )
        if isinstance(other, ListLike):
            return type(self)(list(self) + list(other))
        else:
            return NotImplemented

    @setdoc.basic
    def __eq__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, ListLike):
            return list(self) == list(other)
        else:
            return NotImplemented

    @setdoc.basic
    def __ge__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, ListLike):
            return list(self) >= list(other)
        else:
            return NotImplemented

    @overload
    @setdoc.basic
    def __getitem__(self: Self, index: SupportsIndex, /) -> Item: ...

    @overload
    @setdoc.basic
    def __getitem__(self: Self, index: Slice[SupportsIndex], /) -> Self: ...

    @setdoc.basic
    def __getitem__(
        self: Self, index: SupportsIndex | Slice[SupportsIndex], /
    ) -> Item | Self:
        if isinstance(index, SupportsIndex):
            return list(self)[index]
        else:
            return type(self)(list(self)[index])

    @setdoc.basic
    def __gt__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, ListLike):
            return list(self) > list(other)
        else:
            return NotImplemented

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Init[Item] = (), /) -> None: ...

    @setdoc.basic
    def __le__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, ListLike):
            return list(self) <= list(other)
        else:
            return NotImplemented

    @setdoc.basic
    def __lt__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, ListLike):
            return list(self) < list(other)
        else:
            return NotImplemented

    @setdoc.basic
    def __mul__(self: Self, other: SupportsIndex, /) -> Self:
        return type(self)(list(self) * other)

    @setdoc.basic
    def __repr__(self: Self, /) -> str:
        return f"{type(self).__name__}({list(self)!r})"

    __rmul__ = __mul__


class FrozenListLike[Item](
    ListLike[Item],
    abc.Hashable,
):
    """Provide easy abc for custom frozen list-like."""

    __slots__ = ()

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(tuple(self))


class MutableListLike[Item](
    ListLike[Item],
    MutableSequence[Item],
):
    """Provide easy abc for custom mutable list-like."""

    __slots__ = ()

    @setdoc.basic
    class Mutable[Item](MutableSequence.Mutable[Item], Protocol):
        @setdoc.basic
        def __imul__(self: Self, other: SupportsIndex, /) -> object: ...
        @setdoc.basic
        def sort(
            self: Self, *, key: Any = None, reverse: bool = False
        ) -> object: ...

    @setdoc.basic
    def __imul__(self: Self, other: SupportsIndex, /) -> Self:
        with self.__mutable__() as data:
            data.__imul__(other)
        return self

    __init__ = MutableSequence.extend

    @abstractmethod
    @setdoc.basic
    def __mutable__(self: Self) -> DataContextManager[Mutable[Item]]: ...

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self)

    @setdoc.basic
    def sort(self: Self, *, key: Any = None, reverse: bool = False) -> None:
        with self.__mutable__() as data:
            data.sort(key=key, reverse=reverse)
