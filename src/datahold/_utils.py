import functools
from typing import *

__all__ = [
    "getHoldFunc",
    "getHoldType",
]


def getHoldFunc(cls: type, name: str) -> Any:
    old: Any = getattr(cls, name)

    def new(self, *args: Any, **kwargs: Any) -> Any:
        data: Any = self.data
        ans: Any = old(data, *args, **kwargs)
        self.data = data
        return ans

    functools.wraps(old)(new)
    return new


def getHoldType(
    *funcnames: str,
    name: str,
    bases: tuple[type],
    datacls: type,
) -> type:
    funcs: dict = dict()
    n: str
    for n in funcnames:
        funcs[n] = getHoldFunc(datacls, n)
    ans = type(name, bases, funcs)
    ans.__annotations__ = dict(data=datacls)
    return ans
