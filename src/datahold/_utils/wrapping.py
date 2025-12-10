import inspect as ins
from functools import partial
from types import FunctionType
from typing import *

__all__ = ["wrap"]


def wraps(cls: type) -> partial:
    return partial(update, cls)


def update(cls: type, func: FunctionType) -> FunctionType:
    params: list
    a: Any
    n: int
    p: ins.Parameter
    q: ins.Parameter
    oldsig: ins.Signature
    old: Callable
    old = getattr(cls, func.__name__)
    func.__doc__ = old.__doc__
    try:
        oldsig = ins.signature(old)
    except ValueError:
        return func
    params = list()
    for n, p in enumerate(oldsig.parameters.values()):
        if n == 0:
            a = Self
        else:
            a = getNonEmpty(p.annotation)
        q = p.replace(annotation=a)
        params.append(q)
    a = getNonEmpty(oldsig.return_annotation)
    func.__signature__ = ins.Signature(params, return_annotation=a)
    func.__annotations__ = getAnnotationsDict(func.__signature__)
    return func


def wrap(
    *,
    old: Callable,
    new: FunctionType,
) -> ins.Signature:
    params: list
    a: Any
    n: int
    p: ins.Parameter
    q: ins.Parameter
    oldsig: ins.Signature
    new.__doc__ = old.__doc__
    try:
        oldsig = ins.signature(old)
    except ValueError:
        return
    params = list()
    for n, p in enumerate(oldsig.parameters.values()):
        if n == 0:
            a = Self
        else:
            a = getNonEmpty(p.annotation)
        q = p.replace(annotation=a)
        params.append(q)
    a = ins.signature(new).return_annotation
    a = getNonEmpty(oldsig.return_annotation, backup=a)
    new.__signature__ = ins.Signature(params, return_annotation=a)
    new.__annotations__ = getAnnotationsDict(new.__signature__)


def getAnnotationsDict(sig: ins.Signature) -> dict:
    ans: dict
    p: ins.Parameter
    ans = dict()
    for p in sig.parameters.values():
        ans[p.name] = p.annotation
    ans["return"] = sig.return_annotation
    return ans


def getNonEmpty(value: Any, backup: Any = Any) -> Any:
    if value is ins.Parameter.empty:
        return backup
    else:
        return value
