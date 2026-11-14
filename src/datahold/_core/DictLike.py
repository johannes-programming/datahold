from __future__ import annotations

__all__: list[str] = [
    "DictLike",
]

from abc import abstractmethod
from collections import abc
from reprlib import recursive_repr
from typing import Any, Self, overload

from frozendict import frozendict

from datahold._core.Collection import Collection
from datahold._core.typing import DictInit

### DICT-LIKE ###


class DictLike[Key: abc.Hashable, Value](
    Collection[Key], abc.Mapping[Key, Value]
):
    """Shared read-only dictionary interface."""

    type Frozen[FrozenKey: abc.Hashable, FrozenValue] = frozendict[
        FrozenKey, FrozenValue
    ]

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
        other: DictInit[Key, Value] = (),
        /,
    ) -> None: ...

    @overload
    def __init__[Key_: abc.Hashable](
        self: DictLike[Key_ | str, Value],
        other: DictInit[Key_ | str, Value] = (),
        /,
        **kwargs: Value,
    ) -> None: ...

    @abstractmethod
    def __init__(
        self: Any,
        other: Any = (),
        /,
        **kwargs: Any,
    ) -> None:
        """Construct the mapping from pairs, a mapping and/or keywords."""

    # __iter__ is inherited
    # __len__ is inherited
    # __ne__ is inherited from object (negates __eq__).
    def __or__[Key_: abc.Hashable, Value_](
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
    def fromkeys[Key_: abc.Hashable](
        cls: type[Any], keys: abc.Iterable[Key_], /
    ) -> DictLike[Key_, None]: ...

    @overload
    @classmethod
    def fromkeys[Key_: abc.Hashable, Value_](
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
