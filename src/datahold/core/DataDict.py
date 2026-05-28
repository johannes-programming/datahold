from abc import abstractmethod
from collections.abc import Hashable, Iterable, MutableMapping
from typing import Any, Self, TypeVar, overload

import setdoc
from frozendict import frozendict

from ..base.BaseDataDict import BaseDataDict
from .DataObject import DataObject

__all__ = ["DataDict"]

Key = TypeVar("Key")
Value = TypeVar("Value")

MISSING = object()


class DataDict(DataObject, BaseDataDict[Key, Value]):
    __slots__ = ()

    @setdoc.setdoc(dict.__delitem__.__doc__)
    def __delitem__(self: Self, key: Any, /) -> None:
        data: Any
        data = dict(self.data)
        data.__delitem__(key)
        self.data = frozendict(data)

    @setdoc.basic
    def __init__(
        self: Self,
        data: Any = (),
        /,
        **kwargs: Value,
    ) -> None:
        data_: Any
        data_ = data
        self.data = frozendict(data_, **kwargs)

    @setdoc.setdoc(dict.__ior__.__doc__)
    def __ior__(self: Self, value: Any, /) -> Any:
        ans: Any
        data: Any
        data = dict(self.data)
        ans = data.__ior__(value)
        self.data = frozendict(data)
        return ans

    @setdoc.setdoc(dict.__setitem__.__doc__)
    def __setitem__(self: Self, key: Any, value: Any, /) -> None:
        data: Any
        data = dict(self.data)
        data.__setitem__(key, value)
        self.data = frozendict(data)

    @setdoc.setdoc(dict.clear.__doc__)
    def clear(self: Self, /) -> None:
        data: Any
        data = dict(self.data)
        data.clear()
        self.data = frozendict(data)

    @overload
    @setdoc.setdoc(dict.pop.__doc__)
    def pop(self: Self, key: Any, /) -> Any: ...

    @overload
    @setdoc.setdoc(dict.pop.__doc__)
    def pop(self: Self, key: Any, default: Any, /) -> Any: ...

    @setdoc.setdoc(dict.pop.__doc__)
    def pop(self: Self, key: Any, default: Any = MISSING, /) -> Any:
        ans: Any
        data: Any
        data = dict(self.data)
        if default is MISSING:
            ans = data.pop(key)
        else:
            ans = data.pop(key, default)
        self.data = frozendict(data)
        return ans

    @setdoc.setdoc(dict.popitem.__doc__)
    def popitem(self: Self, /) -> Any:
        data: Any
        data = dict(self.data)
        ans = data.popitem()
        self.data = frozendict(data)
        return ans

    @setdoc.setdoc(dict.setdefault.__doc__)
    def setdefault(self: Self, key: Any, default: Any = None, /) -> Any:
        ans: Any
        data: Any
        data = dict(self.data)
        ans = data.setdefault(key, default)
        self.data = frozendict(data)
        return ans

    @setdoc.setdoc(dict.update.__doc__)
    def update(
        self: Self,
        other: Any,
        /,
        **kwargs: Any,
    ) -> Any:
        data: Any
        data = dict(self.data)
        data.update(other, **kwargs)
        self.data = frozendict(data)


MutableMapping.register(DataDict)
