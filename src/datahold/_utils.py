import functools
from typing import *

__all__ = [
    "getHoldFunc",
    "getHoldType",
    "wraps",
]


def getHoldFunc(cls: type, name: str) -> Any:
    old: Any = getattr(cls, name)

    def new(self: Self, *args: Any, **kwargs: Any) -> Any:
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


WRAPPER_ASSIGNMENTS = (
    "__module__",
    "__name__",
    "__qualname__",
    "__annotations__",
    "__type_params__",
)
WRAPPER_UPDATES = ("__dict__",)


def wraps(wrapped):
    """Decorator factory to apply update_wrapper() to a wrapper function

    Returns a decorator that invokes update_wrapper() with the decorated
    function as the wrapper argument and the arguments to wraps() as the
    remaining arguments. Default arguments are as for update_wrapper().
    This is a convenience function to simplify applying partial() to
    update_wrapper().
    """
    return functools.partial(
        functools.update_wrapper,
        wrapped=wrapped,
        assigned=WRAPPER_ASSIGNMENTS,
        updated=WRAPPER_UPDATES,
    )
