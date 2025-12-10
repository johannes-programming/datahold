import abc
from functools import partial
from types import FunctionType
from typing import *

from datahold._utils.wrapping import wrap

__all__ = ["funcDeco"]


def funcDeco(**kwargs: type) -> partial:
    return partial(update, **kwargs)


def update(
    Target: type,
    *,
    funcnames: str,
    NonFrozen: type,
) -> type:
    name: str
    for name in funcnames:
        setupFunc(
            Target=Target,
            name=name,
            NonFrozen=NonFrozen,
        )
    abc.update_abstractmethods(Target)
    return Target


def setupFunc(
    *,
    Target: type,
    NonFrozen: type,
    name: str,
) -> None:
    old: Callable
    new: FunctionType
    old = getattr(NonFrozen, name)
    new = makeFunc(
        old=old,
        NonFrozen=NonFrozen,
    )
    new.__module__ = Target.__module__
    new.__name__ = name
    new.__qualname__ = Target.__qualname__ + "." + name
    setattr(Target, name, new)


def makeFunc(*, old: FunctionType, NonFrozen: type) -> Any:
    def new(self: Self, *args: Any, **kwargs: Any) -> Any:
        return old(NonFrozen(self.data), *args, **kwargs)

    wrap(new=new, old=old)

    return new
