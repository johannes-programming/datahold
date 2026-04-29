import collections
from typing import *

import setdoc
from namings import FrozenNaming, Naming

from datahold._utils.wrapping import wraps

from .BaseDataNaming import BaseDataNaming
from .DataObject import DataObject

__all__ = ["DataNaming"]

Value = TypeVar("Value")


class DataNaming(
    DataObject, BaseDataNaming[Value], collections.abc.MutableMapping[str, Value]
):
    data: FrozenNaming[Value]
    __slots__ = ()

    @wraps(Naming[Value])
    def __delitem__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        ans: Any
        data: Naming[Value]
        data = Naming[Value](self.data)
        ans = data.__delitem__(*args, **kwargs)
        self.data = FrozenNaming[Value](data)
        return ans

    @setdoc.basic
    def __init__(self: Self, data: Any = (), /, **kwargs: Any) -> None:
        self.data = FrozenNaming[Value](data, **kwargs)

    @wraps(Naming[Value])
    def __ior__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        ans: Any
        data: Naming[Value]
        data = Naming[Value](self.data)
        ans = data.__ior__(*args, **kwargs)
        self.data = FrozenNaming[Value](data)
        return ans

    @wraps(Naming[Value])
    def __setitem__(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        ans: Any
        data: Naming[Value]
        data = Naming[Value](self.data)
        ans = data.__setitem__(*args, **kwargs)
        self.data = FrozenNaming[Value](data)
        return ans

    @wraps(Naming[Value])
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        ans: Any
        data: Naming[Value]
        data = Naming[Value](self.data)
        ans = data.clear(*args, **kwargs)
        self.data = FrozenNaming[Value](data)
        return ans

    @wraps(Naming[Value])
    def pop(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        ans: Any
        data: Naming[Value]
        data = Naming[Value](self.data)
        ans = data.pop(*args, **kwargs)
        self.data = FrozenNaming[Value](data)
        return ans

    @wraps(Naming[Value])
    def popitem(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        ans: Any
        data: Naming[Value]
        data = Naming[Value](self.data)
        ans = data.popitem(*args, **kwargs)
        self.data = FrozenNaming[Value](data)
        return ans

    @wraps(Naming[Value])
    def setdefault(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        ans: Any
        data: Naming[Value]
        data = Naming[Value](self.data)
        ans = data.setdefault(*args, **kwargs)
        self.data = FrozenNaming[Value](data)
        return ans

    @wraps(Naming[Value])
    def update(self: Self, *args: Any, **kwargs: Any) -> Any:
        "This doc string is overwritten together with the signature to match the original as closely as possible."
        ans: Any
        data: Naming[Value]
        data = Naming[Value](self.data)
        ans = data.update(*args, **kwargs)
        self.data = FrozenNaming[Value](data)
        return ans
