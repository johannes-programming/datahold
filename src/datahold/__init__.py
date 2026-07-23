"""Provide easy abc for custom collections."""

from __future__ import annotations

__all__: list[str] = [
    "BaseDataAbstractSet",
    "BaseDataCollection",
    "BaseDataDict",
    "BaseDataList",
    "BaseDataMapping",
    "BaseDataSequence",
    "BaseDataSet",
    "BaseHoldCollection",
    "DataDict",
    "DataList",
    "DataSet",
    "FrozenDataDict",
    "FrozenDataList",
    "FrozenDataSet",
    "FrozenHoldDict",
    "FrozenHoldList",
    "FrozenHoldSet",
    "HoldDict",
    "HoldList",
    "HoldSet",
]

import enum
from abc import ABCMeta, abstractmethod
from collections import abc
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


class Missing(enum.Enum):
    missing = None


type Slice[Index] = slice[Optional[Index], Optional[Index], Optional[Index]]


class SupportsKeysAndGetitem[Key, Value](Protocol):

    @setdoc.basic
    def __getitem__(self: Self, key: Never, /) -> Value: ...

    @setdoc.basic
    def keys(self: Self) -> abc.Iterable[Key]: ...


### COLLECTION ###


class BaseDataCollection[Item](
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
        try:
            return other in self.__fget__()
        except TypeError:
            return other in (x for x in self.__fget__())  # type: ignore[operator]

    @setdoc.basic
    def __iter__(self: Self, /) -> abc.Iterator[Item]:
        return iter(self.__fget__())

    @setdoc.basic
    def __len__(self: Self, /) -> int:
        return len(self.__fget__())

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> Data[Item]: ...


class BaseHoldCollection[Item](BaseDataCollection[Item]):
    """Provide abc for usable classes with slots."""

    __slots__ = ("_data",)


### ABSTRACT SET ###


class BaseDataAbstractSet[Item](
    BaseDataCollection[Item],
    abc.Set[Item],
):
    """Provide an easy abc for a custom (abstract) set."""

    __slots__ = ()


### SET ###


class BaseDataSet[Item: abc.Hashable](BaseDataAbstractSet[Item]):
    """Provide an easy abc for custom set-like."""

    __slots__ = ()

    type Data[DataItem] = set[DataItem]
    type Init[InitItem] = abc.Iterable[InitItem]

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> set[Item]: ...

    @abstractmethod
    @setdoc.basic
    def __fset__(self: Self, data: Data[Item], /) -> None: ...

    @setdoc.basic
    def __init__(self: Self, data: Init[Item] = (), /) -> None:
        self.__fset__(set(data))

    @setdoc.basic
    def __repr__(self: Self, /) -> str:
        return f"{type(self).__name__}({set(self.__fget__())!r})"

    @setdoc.basic
    def difference(self: Self, /, *others: abc.Iterable[abc.Hashable]) -> Self:
        return type(self)(self.__fget__().difference(*others))

    @setdoc.basic
    def intersection(
        self: Self, /, *others: abc.Iterable[abc.Hashable]
    ) -> Self:
        return type(self)(self.__fget__().intersection(*others))

    @setdoc.basic
    def issubset(self: Self, other: abc.Iterable[abc.Hashable], /) -> bool:
        return self.__fget__().issubset(other)

    @setdoc.basic
    def issuperset(self: Self, other: abc.Iterable[abc.Hashable], /) -> bool:
        return self.__fget__().issuperset(other)

    @setdoc.basic
    def symmetric_difference(
        self: Self,
        other: abc.Iterable[Item],
        /,
    ) -> Self:
        return type(self)(self.__fget__().symmetric_difference(other))

    @setdoc.basic
    def union(self: Self, /, *others: abc.Iterable[Item]) -> Self:
        return type(self)(self.__fget__().union(*others))


class FrozenDataSet[Item: abc.Hashable](BaseDataSet[Item], abc.Hashable):
    """Provide easy abc for custom frozen set-like."""

    __slots__ = ()

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(frozenset(self.__fget__()))


class FrozenHoldSet[Item: abc.Hashable](
    FrozenDataSet[Item],
    BaseHoldCollection[Item],
):
    """Provide usable frozen set-like with slots."""

    __slots__ = ()

    @setdoc.basic
    def __fget__(self: Self) -> FrozenHoldSet.Data[Item]:
        return set(self._data)

    @setdoc.basic
    def __fset__(self: Self, data: FrozenHoldSet.Data[Item], /) -> None:
        self._data: FrozenHoldSet.Data[Item] = data


class DataSet[Item: abc.Hashable](
    BaseDataSet[Item],
    abc.MutableSet[Item],
):
    """Provide easy abc for custom mutable set-like."""

    __slots__ = ()

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> DataSet.Data[Item]: ...

    @abstractmethod
    @setdoc.basic
    def __fset__(
        self: Self,
        value: DataSet.Data[Item],
        /,
    ) -> None: ...

    @setdoc.basic
    def add(self: Self, item: Item, /) -> None:
        self.__fset__(self.__fget__() | {item})

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self)

    @setdoc.basic
    def difference_update(
        self: Self,
        /,
        *others: abc.Iterable[abc.Hashable],
    ) -> None:
        data: set[Item]
        data = set(self.__fget__())
        data.difference_update(*others)
        self.__fset__(set(data))

    @setdoc.basic
    def discard(self: Self, item: abc.Hashable, /) -> None:
        data: set[Item]
        data = set(self.__fget__())
        data.discard(item)
        self.__fset__(set(data))

    @setdoc.basic
    def intersection_update(
        self: Self, /, *others: abc.Iterable[abc.Hashable]
    ) -> None:
        data: set[Item]
        data = set(self.__fget__())
        data.intersection_update(*others)
        self.__fset__(set(data))

    @setdoc.basic
    def symmetric_difference_update(
        self: Self, other: abc.Iterable[Item], /
    ) -> None:
        data: set[Item]
        data = set(self.__fget__())
        data.symmetric_difference_update(other)
        self.__fset__(set(data))

    @setdoc.basic
    def update(self: Self, /, *others: abc.Iterable[Item]) -> None:
        self.__fset__(self.__fget__().union(*others))


class HoldSet[Item: abc.Hashable](
    DataSet[Item],
    BaseHoldCollection[Item],
):
    """Provide usable mutable set-like with slots."""

    __slots__ = ()

    @setdoc.basic
    def __fget__(self: Self) -> HoldSet.Data[Item]:
        return set(self._data)

    @setdoc.basic
    def __fset__(self: Self, value: HoldSet.Data[Item], /) -> None:
        self._data: HoldSet.Data[Item] = value


### MAPPING ###
class BaseDataMapping[Key, Value](
    BaseDataCollection[Key], abc.Mapping[Key, Value]
):
    """Provide an easy abc for a custom mapping."""

    __slots__ = ()

    @setdoc.basic
    class Data[DataKey, DataValue](
        BaseDataCollection.Data[DataKey],
        Protocol,
    ):
        @setdoc.basic
        def __getitem__(self: Self, key: Never, /) -> DataValue:
            pass

    @setdoc.basic
    def __getitem__(self: Self, key: object, /) -> Value:
        try:
            return self.__fget__()[key]  # type: ignore[index]
        except TypeError:
            raise KeyError(key) from None

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> Data[Key, Value]: ...


### DICT ###


class BaseDataDict[Key: abc.Hashable, Value](
    BaseDataMapping[Key | str, Optional[Value]],
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
    def __fset__(self: Self, data: Data[Key, Value], /) -> None: ...

    @setdoc.basic
    def __init__(
        self: Self,
        data: Init[Key, Value] = (),
        /,
        **kwargs: Optional[Value],
    ) -> None:
        data_: BaseDataDict.Data[Key, Value]
        data_ = dict(  # type: ignore[assignment]
            data,  # type: ignore[arg-type]
            **kwargs,
        )
        self.__fset__(data_)

    @setdoc.basic
    def __or__(
        self: Self,
        other: BaseDataDict[Key, Value],
        /,
    ) -> Self:
        return type(self)(self.__fget__() | other.__fget__())

    @setdoc.basic
    def __repr__(self: Self, /) -> str:
        return f"{type(self).__name__}({dict(self)!r})"

    # __ror__ is unnecessary because of how __or__ is defined

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> Data[Key, Value]: ...

    @classmethod
    @setdoc.basic
    def fromkeys(
        cls: type[Self],
        iterable: abc.Iterable[Key | str],
        value: Optional[Value] = None,
        /,
    ) -> Self:
        return cls(dict.fromkeys(iterable, value))


class FrozenDataDict[Key: abc.Hashable, Value](
    BaseDataDict[Key, Value],
    abc.Hashable,
):
    """Provide easy abc for custom frozen dict-like."""

    __slots__ = ()

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(frozendict(self.__fget__()))


class FrozenHoldDict[Key: abc.Hashable, Value](
    FrozenDataDict[Key, Value],
    BaseHoldCollection[Key | str],
):
    """Provide usable frozen dict-like with slots."""

    __slots__ = ()

    @setdoc.basic
    def __fget__(self: Self) -> FrozenHoldDict.Data[Key, Value]:
        return dict(self._data)

    @setdoc.basic
    def __fset__(self: Self, data: FrozenHoldDict.Data[Key, Value], /) -> None:
        self._data: FrozenHoldDict.Data[Key, Value] = data


class DataDict[Key: abc.Hashable, Value](
    BaseDataDict[Key, Value],
    abc.MutableMapping[Key | str, Optional[Value]],
):
    """Provide easy abc for custom mutable dict-like."""

    __slots__ = ()

    @setdoc.basic
    def __delitem__(self: Self, key: Key | str, /) -> None:
        data: DataDict.Data[Key, Value]
        data = self.__fget__()
        del data[key]
        self.__fset__(data)

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> DataDict.Data[Key, Value]: ...

    @abstractmethod
    @setdoc.basic
    def __fset__(self: Self, data: DataDict.Data[Key, Value], /) -> None: ...

    @setdoc.basic
    def __ior__(
        self: Self,
        other: BaseDataDict[Key, Value],
        /,
    ) -> Self:
        self.__fset__(self.__fget__() | other.__fget__())
        return self

    @setdoc.basic
    def __setitem__(
        self: Self,
        key: Key | str,
        value: Optional[Value],
        /,
    ) -> None:
        # what to do if Key includes unhashable types?
        data: DataDict.Data[Key, Value]
        data = self.__fget__()
        data[key] = value
        self.__fset__(data)

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self)


class HoldDict[Key: abc.Hashable, Value](
    DataDict[Key, Value],
    BaseHoldCollection[Key | str],
):
    """Provide usable mutable dict-like with slots."""

    __slots__ = ()

    @setdoc.basic
    def __fget__(self: Self) -> HoldDict.Data[Key, Value]:
        return dict(self._data)

    @setdoc.basic
    def __fset__(
        self: Self,
        value: HoldDict.Data[Key, Value],
        /,
    ) -> None:
        self._data: HoldDict.Data[Key, Value] = value


### SEQUENCE ###


class BaseDataSequence[Item](
    BaseDataCollection[Item],
    abc.Sequence[Item],
):
    """Provide an easy abc for a custom sequence."""

    __slots__ = ()

    @setdoc.basic
    class Data[DataItem](
        BaseDataCollection.Data[DataItem],
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
        return self.__fget__()[key]

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> Data[Item]: ...


### LIST ###


class BaseDataList[Item](BaseDataSequence[Item]):
    """Provide an easy abc for custom list-like."""

    __slots__ = ()

    type Data[DataItem] = list[DataItem]
    type Init[InitItem] = abc.Iterable[InitItem]

    @setdoc.basic
    def __add__(self: Self, other: BaseDataList[Item], /) -> Self:
        # list.__add__ reveals Overload(
        #     def [_T] (list[_T], list[_T]) -> list[_T],
        #     def [_T, _S] (list[_T], list[_S]) -> list[_S | _T],
        # )
        # tuple.__add__ reveals Overload(
        #     def [_T_co] (tuple[_T_co, ...], tuple[_T_co, ...]) -> tuple[_T_co, ...],
        #     def [_T_co, _T] (tuple[_T_co, ...], tuple[_T, ...]) -> tuple[_T_co | _T, ...],
        # )
        if isinstance(other, BaseDataList):
            return type(self)(self.__fget__() + other.__fget__())
        else:
            return NotImplemented

    @setdoc.basic
    def __eq__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, BaseDataList):
            return self.__fget__() == other.__fget__()
        else:
            return NotImplemented

    @abstractmethod
    @setdoc.basic
    def __fset__(self: Self, value: list[Item], /) -> None: ...

    @setdoc.basic
    def __ge__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, BaseDataList):
            return self.__fget__() >= other.__fget__()
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
            return self.__fget__()[index]
        else:
            return type(self)(self.__fget__()[index])

    @setdoc.basic
    def __gt__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, BaseDataList):
            return self.__fget__() > other.__fget__()
        else:
            return NotImplemented

    @setdoc.basic
    def __init__(self: Self, data: Init[Item] = (), /) -> None:
        self.__fset__(list(data))

    @setdoc.basic
    def __le__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, BaseDataList):
            return self.__fget__() <= other.__fget__()
        else:
            return NotImplemented

    @setdoc.basic
    def __lt__(self: Self, other: object, /) -> NotImplementedType | bool:
        if isinstance(other, BaseDataList):
            return self.__fget__() < other.__fget__()
        else:
            return NotImplemented

    @setdoc.basic
    def __mul__(self: Self, other: SupportsIndex, /) -> Self:
        return type(self)(self.__fget__() * other)

    @setdoc.basic
    def __repr__(self: Self, /) -> str:
        return f"{type(self).__name__}({list(self.__fget__())!r})"

    __rmul__ = __mul__

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> Data[Item]: ...


class FrozenDataList[Item](
    BaseDataList[Item],
    abc.Hashable,
):
    """Provide easy abc for custom frozen list-like."""

    __slots__ = ()

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(tuple(self.__fget__()))


class FrozenHoldList[Item](
    FrozenDataList[Item],
    BaseHoldCollection[Item],
):
    """Provide usable frozen list-like with slots."""

    __slots__ = ()

    @setdoc.basic
    def __fget__(self: Self) -> FrozenHoldList.Data[Item]:
        return list(self._data)

    @setdoc.basic
    def __fset__(self: Self, data: FrozenHoldList.Data[Item], /) -> None:
        self._data: FrozenHoldList.Data[Item] = data


class DataList[Item](
    BaseDataList[Item],
    abc.MutableSequence[Item],
):
    """Provide easy abc for custom mutable list-like."""

    __slots__ = ()

    @setdoc.basic
    def __delitem__(
        self: Self, other: SupportsIndex | Slice[SupportsIndex], /
    ) -> None:
        data: list[Item]
        data = self.__fget__()
        del data[other]
        self.__fset__(data)

    @abstractmethod
    @setdoc.basic
    def __fget__(self: Self) -> DataList.Data[Item]: ...

    @abstractmethod
    @setdoc.basic
    def __fset__(
        self: Self,
        value: DataList.Data[Item],
        /,
    ) -> None: ...

    @setdoc.basic
    def __imul__(self: Self, other: SupportsIndex, /) -> Self:
        self.__fset__(self.__fget__() * other)
        return self

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
        data: list[Item]
        data = self.__fget__()
        data[key] = value  # type: ignore[index, assignment]
        self.__fset__(data)

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self)

    @setdoc.basic
    def insert(self: Self, index: SupportsIndex, item: Item, /) -> None:
        data: list[Item]
        data = self.__fget__()
        data.insert(index, item)
        self.__fset__(data)

    @setdoc.basic
    def sort(self: Self, *, key: Any = None, reverse: bool = False) -> None:
        data: list[Item]
        data = self.__fget__()
        data.sort(key=key, reverse=reverse)
        self.__fset__(data)


class HoldList[Item](
    DataList[Item],
    BaseHoldCollection[Item],
):
    """Provide usable mutable list-like with slots."""

    __slots__ = ()

    @setdoc.basic
    def __fget__(self: Self) -> HoldList.Data[Item]:
        return list(self._data)

    @setdoc.basic
    def __fset__(self: Self, value: HoldList.Data[Item], /) -> None:
        self._data: HoldList.Data[Item] = value
