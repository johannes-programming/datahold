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
    "MutableSequence",
    "MutableSet",
    "MutableSetLike",
    "Sequence",
    "Set",
    "SetLike",
    "attrdata",
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
    overload,
)

import setdoc
from frozendict import frozendict

### UTILS ###


class Copyable(Protocol):
    @setdoc.basic
    def copy(self: Self) -> Self: ...


class DataContextManager[Data]:
    @setdoc.basic
    def __enter__(self: Self) -> Data: ...
    @setdoc.basic
    def __exit__(
        self: Self, exc_type: Any, exc_value: Any, traceback: Any
    ) -> None: ...


class Missing(enum.Enum):
    missing = None


type Slice[Index] = slice[Optional[Index], Optional[Index], Optional[Index]]


class SupportsKeysAndGetitem[Key, Value](Protocol):

    @setdoc.basic
    def __getitem__(self: Self, key: Never, /) -> Value: ...

    @setdoc.basic
    def keys(self: Self) -> abc.Iterable[Key]: ...


###


def attrdata[Data: Copyable](
    *,
    factory: abc.Callable[[], Data],
    name: str,
) -> DataContextManager[Data]:
    @contextmanager
    @setdoc.basic
    def __data__(self: Self) -> abc.Generator[Data, None, None]:
        data: Data | Missing
        data = getattr(self, name, Missing.missing)
        if isinstance(data, Missing):
            data = factory()
        else:
            data = data.copy()
        yield data
        setattr(self, name, data)

    return __data__


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
    class Data[DataItem](
        abc.Sized,
        abc.Iterable[DataItem],
        abc.Container[Never],
        Protocol,
    ):
        """Provide collection data protocol."""

    @setdoc.basic
    def __contains__(self: Self, other: object, /) -> bool:
        with self.__data__() as data:
            try:
                return other in data
            except TypeError:
                return other in (x for x in data)  # type: ignore[operator]

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> DataContextManager[Data[Item]]: ...

    @setdoc.basic
    def __iter__(self: Self, /) -> abc.Iterator[Item]:
        with self.__data__() as data:
            return iter(data)

    @setdoc.basic
    def __len__(self: Self, /) -> int:
        with self.__data__() as data:
            return len(data)


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

    class Data[DataItem](Set.Data[DataItem], Protocol):
        """Provide mutable set data protocol."""

        @setdoc.basic
        def add(self: Self, item: DataItem, /) -> None: ...
        @setdoc.basic
        def discard(self: Self, item: abc.Hashable, /) -> None: ...

    @setdoc.basic
    def add(self: Self, item: Item, /) -> None:
        with self.__data__() as data:
            data.add(item)

    @setdoc.basic
    def discard(self: Self, item: abc.Hashable, /) -> None:
        with self.__data__() as data:
            data.discard(item)


### SET LIKE ###


class SetLike[Item: abc.Hashable](Set[Item]):
    """Provide an easy abc for custom set-like."""

    __slots__ = ()

    type Data[DataItem] = set[DataItem]
    type Init[InitItem] = abc.Iterable[InitItem]

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> DataContextManager[Data[Item]]: ...

    @setdoc.basic
    def __init__(self: Self, data: Init[Item] = (), /) -> None:
        with self.__data__() as data_:
            data_.update(data)

    @setdoc.basic
    def __repr__(self: Self, /) -> str:
        with self.__data__() as data:
            return f"{type(self).__name__}({set(data)!r})"

    @setdoc.basic
    def difference(self: Self, /, *others: abc.Iterable[abc.Hashable]) -> Self:
        with self.__data__() as data:
            return type(self)(data.difference(*others))

    @setdoc.basic
    def intersection(
        self: Self, /, *others: abc.Iterable[abc.Hashable]
    ) -> Self:
        with self.__data__() as data:
            return type(self)(data.intersection(*others))

    @setdoc.basic
    def issubset(self: Self, other: abc.Iterable[abc.Hashable], /) -> bool:
        with self.__data__() as data:
            return data.issubset(other)

    @setdoc.basic
    def issuperset(self: Self, other: abc.Iterable[abc.Hashable], /) -> bool:
        with self.__data__() as data:
            return data.issuperset(other)

    @setdoc.basic
    def symmetric_difference(
        self: Self,
        other: abc.Iterable[Item],
        /,
    ) -> Self:
        with self.__data__() as data:
            return type(self)(data.symmetric_difference(other))

    @setdoc.basic
    def union(self: Self, /, *others: abc.Iterable[Item]) -> Self:
        with self.__data__() as data:
            return type(self)(data.union(*others))


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
    def add(self: Self, item: Item, /) -> None:
        with self.__data__() as data:
            data.add(item)

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self)

    @setdoc.basic
    def difference_update(
        self: Self,
        /,
        *others: abc.Iterable[abc.Hashable],
    ) -> None:
        with self.__data__() as data:
            data.difference(*others)

    @setdoc.basic
    def discard(self: Self, item: abc.Hashable, /) -> None:
        with self.__data__() as data:
            data.discard(item)

    @setdoc.basic
    def intersection_update(
        self: Self, /, *others: abc.Iterable[abc.Hashable]
    ) -> None:
        with self.__data__() as data:
            data.intersection_update(*others)

    @setdoc.basic
    def symmetric_difference_update(
        self: Self, other: abc.Iterable[Item], /
    ) -> None:
        with self.__data__() as data:
            data.symmetric_difference_update(other)

    @setdoc.basic
    def update(self: Self, /, *others: abc.Iterable[Item]) -> None:
        with self.__data__() as data:
            data.update(*others)


### MAPPING ###
class Mapping[Key: abc.Hashable, Value](
    Collection[Key], abc.Mapping[Key, Value]
):
    """Provide an easy abc for a custom mapping."""

    __slots__ = ()

    @setdoc.basic
    class Data[DataKey, DataValue](
        Collection.Data[DataKey],
        Protocol,
    ):
        @setdoc.basic
        def __getitem__(self: Self, key: Never, /) -> DataValue: ...

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> DataContextManager[Data[Key, Value]]: ...

    @setdoc.basic
    def __getitem__(self: Self, key: object, /) -> Value:
        with self.__data__() as data:
            try:
                return data[key]  # type: ignore[index]
            except TypeError:
                raise KeyError(key) from None


class FrozenMapping[Key: abc.Hashable, Value](
    Mapping[Key, Value],
    abc.Hashable,
):
    """Provide an easy abc for a custom frozen mapping."""

    __slots__ = ()

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(frozendict(self.items()))


### DICT LIKE ###


class DictLike[Key: abc.Hashable, Value](
    Mapping[Key | str, Optional[Value]],
):
    """Provide an easy abc for custom dict-like."""

    __slots__ = ()

    type Data[DataKey, DataValue] = dict[DataKey | str, Optional[DataValue]]
    type Init[DataKey, DataValue] = (
        SupportsKeysAndGetitem[DataKey | str, Optional[DataValue]]
        | abc.Iterable[tuple[DataKey | str, Optional[DataValue]]]
    )

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> DataContextManager[Data[Key, Value]]: ...

    @setdoc.basic
    def __init__(
        self: Self,
        data: Init[Key, Value] = (),
        /,
        **kwargs: Optional[Value],
    ) -> None:
        with self.__data__() as data_:
            data_.update(
                data,  # type: ignore[arg-type]
                **kwargs,
            )

    @setdoc.basic
    def __or__(
        self: Self,
        other: DictLike[Key, Value],
        /,
    ) -> Self:
        with self.__data__() as data, other.__data__() as data_:
            return type(self)(data | data_)

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
    abc.MutableMapping[Key | str, Optional[Value]],
):
    """Provide easy abc for custom mutable dict-like."""

    __slots__ = ()

    @setdoc.basic
    def __delitem__(self: Self, key: Key | str, /) -> None:
        with self.__data__() as data:
            del data[key]

    @setdoc.basic
    def __ior__(
        self: Self,
        other: DictLike[Key, Value],
        /,
    ) -> Self:
        with self.__data__() as data, other.__data__() as data_:
            data.__ior__(data_)
        return self

    @setdoc.basic
    def __setitem__(
        self: Self,
        key: Key | str,
        value: Optional[Value],
        /,
    ) -> None:
        # what to do if Key includes unhashable types?
        with self.__data__() as data:
            data[key] = value

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
    class Data[DataItem](
        Collection.Data[DataItem],
        Protocol,
    ):
        """Provide sequence data protocol."""

        @overload
        @setdoc.basic
        def __getitem__(self: Self, key: int, /) -> DataItem: ...
        @overload
        @setdoc.basic
        def __getitem__(
            self: Self, key: Slice[int], /
        ) -> abc.Sequence[DataItem]: ...
        @setdoc.basic
        def __getitem__(
            self: Self, key: int | Slice[int], /
        ) -> DataItem | abc.Sequence[DataItem]: ...

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> DataContextManager[Data[Item]]: ...

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
        with self.__data__() as data:
            return data[key]


class MutableSequence[Item](
    Sequence[Item],
    abc.MutableSequence[Item],
):
    """Provide easy abc for custom mutable sequence."""

    __slots__ = ()

    @setdoc.basic
    def __delitem__(
        self: Self, other: SupportsIndex | Slice[SupportsIndex], /
    ) -> None:
        with self.__data__() as data:
            del data[other]

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
        with self.__data__() as data:
            data[key] = value  # type: ignore[index, assignment]

    @setdoc.basic
    def insert(self: Self, index: SupportsIndex, item: Item, /) -> None:
        with self.__data__() as data:
            data.insert(index, item)


### LIST LIKE ###


class ListLike[Item](Sequence[Item]):
    """Provide an easy abc for custom list-like."""

    __slots__ = ()

    type Data[DataItem] = list[DataItem]
    type Init[InitItem] = abc.Iterable[InitItem]

    @setdoc.basic
    def __add__(self: Self, other: ListLike[Item], /) -> Self:
        # list.__add__ reveals Overload(
        #     def [_T] (list[_T], list[_T]) -> list[_T],
        #     def [_T, _S] (list[_T], list[_S]) -> list[_S | _T],
        # )
        # tuple.__add__ reveals Overload(
        #     def [_T_co] (tuple[_T_co, ...], tuple[_T_co, ...]) -> tuple[_T_co, ...],
        #     def [_T_co, _T] (tuple[_T_co, ...], tuple[_T, ...]) -> tuple[_T_co | _T, ...],
        # )
        if isinstance(other, ListLike):
            with self.__data__() as data, other.__data__() as data_:
                return type(self)(data + data_)
        else:
            return NotImplemented

    @abstractmethod
    @setdoc.basic
    def __data__(self: Self) -> DataContextManager[Data[Item]]: ...

    @setdoc.basic
    def __eq__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, ListLike):
            with self.__data__() as data, other.__data__() as data_:
                return data == data_
        else:
            return NotImplemented

    @setdoc.basic
    def __ge__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, ListLike):
            with self.__data__() as data, other.__data__() as data_:
                return data >= data_
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
        with self.__data__() as data:
            if isinstance(index, SupportsIndex):
                return data[index]
            else:
                return type(self)(data[index])

    @setdoc.basic
    def __gt__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, ListLike):
            with self.__data__() as data, other.__data__() as data_:
                return data > data_
        else:
            return NotImplemented

    @setdoc.basic
    def __init__(self: Self, data: Init[Item] = (), /) -> None:
        with self.__data__() as data_:
            data_.extend(data)

    @setdoc.basic
    def __le__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, ListLike):
            with self.__data__() as data, other.__data__() as data_:
                return data <= data_
        else:
            return NotImplemented

    @setdoc.basic
    def __lt__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, ListLike):
            with self.__data__() as data, other.__data__() as data_:
                return data < data_
        else:
            return NotImplemented

    @setdoc.basic
    def __mul__(self: Self, other: SupportsIndex, /) -> Self:
        with self.__data__() as data:
            return type(self)(data * other)

    @setdoc.basic
    def __repr__(self: Self, /) -> str:
        with self.__data__() as data:
            return f"{type(self).__name__}({list(data)!r})"

    __rmul__ = __mul__


class FrozenListLike[Item](
    ListLike[Item],
    abc.Hashable,
):
    """Provide easy abc for custom frozen list-like."""

    __slots__ = ()

    @setdoc.basic
    def __hash__(self: Self) -> int:
        with self.__data__() as data:
            return hash(tuple(data))


class MutableListLike[Item](
    ListLike[Item],
    MutableSequence[Item],
):
    """Provide easy abc for custom mutable list-like."""

    __slots__ = ()

    @setdoc.basic
    def __imul__(self: Self, other: SupportsIndex, /) -> Self:
        with self.__data__() as data:
            data.__imul__(data * other)
        return self

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self)

    @setdoc.basic
    def sort(self: Self, *, key: Any = None, reverse: bool = False) -> None:
        with self.__data__() as data:
            data.sort(key=key, reverse=reverse)
