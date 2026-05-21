import collections
from typing import *

import setdoc
import types

from .BaseDataDict import BaseDataDict
from .DataObject import DataObject

__all__ = ["DataDict"]

Key = TypeVar("Key")
Key_ = TypeVar("Key_")
Value = TypeVar("Value")
Value_ = TypeVar("Value_")

MISSING = object()


class DataDict(
    DataObject, BaseDataDict[Key, Value], collections.abc.MutableMapping[Key, Value]
):
    data: types.MappingProxyType[Key, Value]
    __slots__ = ()

    @setdoc.setdoc(dict.__delitem__.__doc__)
    def __delitem__(self: Self, key: Key, /) -> None:
        data: dict[Key, Value]
        data = dict(self.data)
        data.__delitem__(key)
        self.data = types.MappingProxyType(data)

    @setdoc.basic
    def __init__(self: Self, data: Any = (), /, **kwargs: Value) -> None:
        self.data = types.MappingProxyType(dict(data, **kwargs))

    @setdoc.setdoc(dict.__ior__.__doc__)
    def __ior__(
        self: Self, value: dict[Key_, Value_], /
    ) -> dict[Key | Key_, Value | Value_]:
        ans: dict[Key | Key_, Value | Value_]
        data: Any
        data = dict(self.data)
        ans = data.__ior__(value)
        self.data = types.MappingProxyType(data)
        return ans

    @setdoc.setdoc(dict.__setitem__.__doc__)
    def __setitem__(self: Self, key: Key, value: Value, /) -> None:
        data: dict[Key, Value]
        data = dict(self.data)
        data.__setitem__(key, value)
        self.data = types.MappingProxyType(data)

    @setdoc.setdoc(dict.clear.__doc__)
    def clear(self: Self, /) -> None:
        data: dict[Key, Value]
        data = dict(self.data)
        data.clear()
        self.data = types.MappingProxyType(data)

    @overload
    @setdoc.setdoc(dict.pop.__doc__)
    def pop(self: Self, key: Key, /) -> Value: ...

    @overload
    @setdoc.setdoc(dict.pop.__doc__)
    def pop(self: Self, key: Hashable, default: Value_, /) -> Value | Value_: ...

    @setdoc.setdoc(dict.pop.__doc__)
    def pop(
        self: Self, key: Hashable, default: Value_ | object = MISSING, /
    ) -> Value | Value_:
        ans: Value | Value_
        data: Any
        data = dict(self.data)
        if default is MISSING:
            ans = data.pop(key)
        else:
            ans = data.pop(key, default)
        self.data = types.MappingProxyType(data)
        return ans

    @setdoc.setdoc(dict.popitem.__doc__)
    def popitem(self: Self, /) -> tuple[Key, Value]:
        data: dict[Key, Value]
        data = dict(self.data)
        ans = data.popitem()
        self.data = types.MappingProxyType(data)
        return ans

    @setdoc.setdoc(dict.setdefault.__doc__)
    def setdefault(self: Self, key: Key, default: Any = None, /) -> Any:
        ans: Any
        data: dict[Key, Value]
        data = dict(self.data)
        ans = data.setdefault(key, default)
        self.data = types.MappingProxyType(data)
        return ans

    @setdoc.setdoc(dict.update.__doc__)
    def update(self: Self, other: Any, /, **kwargs: Any) -> Any:
        ans: Any
        data: dict[Key, Value]
        data = dict(self.data)
        ans = data.update(other, **kwargs)
        self.data = types.MappingProxyType(data)
        return ans
