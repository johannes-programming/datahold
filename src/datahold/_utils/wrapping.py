import inspect as ins
from functools import partial
from types import FunctionType
from typing import *

__all__ = ["wraps"]


def wraps(cls: type) -> partial:
    return partial(update, cls)


def update(cls: type, member: FunctionType | classmethod) -> FunctionType | classmethod:
    func: Callable
    if type(member) is classmethod:
        func = member.__func__
    else:
        func = member
    update_func(cls, func, type(member))
    return member


def update_func(cls: type, func: FunctionType, Member: type) -> None:
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
        return
    params = list()
    if Member is classmethod:
        params = list(ins.signature(func).parameters.values())
        p = params[0]
        params.clear()
        params.append(p)
    for n, p in enumerate(oldsig.parameters.values()):
        if n != 0 or Member is classmethod:
            a = getNonEmpty(p.annotation)
        else:
            a = Self
        q = p.replace(annotation=a)
        params.append(q)
    a = getNonEmpty(oldsig.return_annotation)
    func.__signature__ = ins.Signature(params, return_annotation=a)
    func.__annotations__ = getAnnotationsDict(func.__signature__)
    return


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
