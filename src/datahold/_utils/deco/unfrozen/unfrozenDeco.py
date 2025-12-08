import abc
from functools import partial
from types import FunctionType
from typing import *

from datahold._utils.deco.wrapping import wrap

__all__ = ["unfrozenDeco"]


def unfrozenDeco(**kwargs: type) -> partial:
    return partial(update, **kwargs)


def update(
    Target: type,
    *,
    funcnames: str,
    Frozen: type,
    NonFrozen: type,
) -> type:
    name: str
    for name in funcnames:
        setupFunc(
            Target=Target,
            name=name,
            Frozen=Frozen,
            NonFrozen=NonFrozen,
        )
    abc.update_abstractmethods(Target)
    return Target


def setupFunc(
    *,
    Target: type,
    NonFrozen: type,
    Frozen: type,
    name: str,
) -> None:
    old: Callable
    new: FunctionType
    old = getattr(NonFrozen, name)
    new = makeFunc(
        old=old,
        NonFrozen=NonFrozen,
        Frozen=Frozen,
    )
    new.__module__ = Target.__module__
    new.__name__ = name
    new.__qualname__ = Target.__qualname__ + "." + name
    setattr(Target, name, new)


def makeFunc(*, old: FunctionType, NonFrozen: type, Frozen: type) -> Any:
    def new(self: Self, *args: Any, **kwargs: Any) -> Any:
        data: Any
        ans: Any
        data = NonFrozen(self.data)
        ans = old(data, *args, **kwargs)
        self.data = Frozen(data)
        return ans

    wrap(new=new, old=old)

    return new
