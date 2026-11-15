from __future__ import annotations

__all__: list[str] = [
    "MutableListLike",
]

from abc import abstractmethod
from collections import abc
from typing import Any, Self, SupportsIndex, TypeVar, overload

from typing_extensions import TypeAliasType

from datahold._core.ContextManager import ContextManager
from datahold._core.ListLike import ListLike
from datahold._core.SupportsGTSelf import SupportsGTSelf
from datahold._core.SupportsLTSelf import SupportsLTSelf

Item = TypeVar("Item")
MutableItem = TypeVar("MutableItem")
TypeItem = TypeVar("TypeItem")
SortGTItem = TypeVar("SortGTItem", bound=SupportsGTSelf)
SortLTItem = TypeVar("SortLTItem", bound=SupportsLTSelf)


class MutableListLike(ListLike[Item], abc.MutableSequence[Item]):
    """Mutable sequence operations committed through a temporary list."""

    Mutable = TypeAliasType(
        "Mutable",
        list[MutableItem],
        type_params=(MutableItem,),
    )

    __slots__ = ()

    def __delitem__(self: Self, index: SupportsIndex | slice, /) -> None:
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
    def __getitem__(self: Self, index: slice, /) -> MutableListLike[Item]: ...

    def __getitem__(self: Self, index: SupportsIndex | slice, /) -> Any:
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

    def __init__(self: Self, other: abc.Iterable[Item] = (), /) -> None:
        self.extend(other)

    @abstractmethod
    def __mutate__(self: Self, /) -> ContextManager[list[Item]]:
        """Yield a mutable working list and commit on successful exit."""

    @overload
    def __setitem__(
        self: Self, index: SupportsIndex, data: Item, /
    ) -> None: ...

    @overload
    def __setitem__(
        self: Self,
        index: slice,
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
    def __type__(
        cls: type[Any],
        other: abc.Iterable[TypeItem],
        /,
    ) -> MutableListLike[TypeItem]:
        # redoing the same method is necessary because copy must return MutableListLike[Item]
        return cls(other)  # type: ignore[no-any-return]

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
    def sort(
        self: MutableListLike[SortGTItem],
        /,
        *,
        key: None = None,
        reverse: bool = False,
    ) -> None: ...
    @overload
    def sort(
        self: MutableListLike[SortLTItem],
        /,
        *,
        key: None = None,
        reverse: bool = False,
    ) -> None: ...
    @overload
    def sort(
        self: Self,
        /,
        *,
        key: abc.Callable[[Item], SortGTItem],
        reverse: bool = False,
    ) -> None: ...
    @overload
    def sort(
        self: Self,
        /,
        *,
        key: abc.Callable[[Item], SortLTItem],
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
