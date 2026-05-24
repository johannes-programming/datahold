import types
from abc import abstractmethod
from collections.abc import Hashable, Iterable, Mapping
from typing import Any, Generic, Optional, Self, TypeVar

import setdoc

from ..typing.SupportsKeysAndGetitem import SupportsKeysAndGetitem
from .BaseDataObject import BaseDataObject

__all__ = ["BaseDataDict"]

Key = TypeVar("Key", covariant=True)
Key_ = TypeVar("Key_")
Value = TypeVar("Value", covariant=True)
Value_ = TypeVar("Value_")


class BaseDataDict(BaseDataObject, Generic[Key, Value]):

    __slots__ = ()

    @setdoc.setdoc(dict.__contains__.__doc__)
    def __contains__(self: Self, key: object, /) -> bool:
        return dict(self.data).__contains__(key)

    @setdoc.setdoc(dict.__getitem__.__doc__)
    def __getitem__(self: Self, key: Hashable, /) -> Value:
        key_: Any
        key_ = key
        return dict(self.data).__getitem__(key_)

    @abstractmethod
    @setdoc.setdoc(dict.__init__.__doc__)
    def __init__(
        self: Self,
        data: Iterable | SupportsKeysAndGetitem[Key, Value] = (),
        /,
        **kwargs: Value,
    ) -> None: ...

    @setdoc.setdoc(dict.__iter__.__doc__)
    def __iter__(self: Self, /) -> Iterable[Key]:
        return dict(self.data).__iter__()

    @setdoc.setdoc(dict.__len__.__doc__)
    def __len__(self: Self, /) -> int:
        return dict(self.data).__len__()

    @setdoc.setdoc(dict.__or__.__doc__)
    def __or__(
        self: Self, value: dict[Key_, Value_], /
    ) -> dict[Key | Key_, Value | Value_]:
        return dict(self.data).__or__(value)

    @setdoc.setdoc(dict.__repr__.__doc__)
    def __repr__(self: Self, /) -> str:
        return dict(self.data).__repr__()

    @setdoc.setdoc(dict.__reversed__.__doc__)
    def __reversed__(self: Self, /) -> Iterable[Key]:
        return dict(self.data).__reversed__()

    @setdoc.setdoc(dict.__ror__.__doc__)
    def __ror__(
        self: Self, value: dict[Key_, Value_], /
    ) -> dict[Key | Key_, Value | Value_]:
        return dict(self.data).__ror__(value)

    @property
    @abstractmethod
    def data(self: Self) -> types.MappingProxyType[Key, Value]: ...

    @classmethod
    @setdoc.setdoc(dict.fromkeys.__doc__)
    def fromkeys(
        cls: type[Self], iterable: Iterable[Key], value: Any = None, /
    ) -> Self:
        return cls(dict.fromkeys(iterable, value))

    @setdoc.setdoc(dict.get.__doc__)
    def get(
        self: Self,
        key: Hashable,
        default: Optional[Value_] = None,
        /,
    ) -> Optional[Value | Value_]:
        key_: Any
        key_ = key
        return dict(self.data).get(key_, default)

    @setdoc.setdoc(dict.items.__doc__)
    def items(self: Self, /) -> Iterable[tuple[Key, Value]]:
        return dict(self.data).items()

    @setdoc.setdoc(dict.keys.__doc__)
    def keys(self: Self, /) -> Iterable[Key]:
        return dict(self.data).keys()

    @setdoc.setdoc(dict.values.__doc__)
    def values(self: Self, /) -> Iterable[Value]:
        return dict(self.data).values()


Mapping.register(BaseDataDict)
