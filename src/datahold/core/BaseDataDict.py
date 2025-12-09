import collections
from typing import *

from frozendict import frozendict

from datahold._utils import frozen
from datahold._utils.Cfg import Cfg
from .BaseDataObject import BaseDataObject
from abc import abstractmethod

__all__ = ["BaseDataDict"]

Key = TypeVar("Key")
Value = TypeVar("Value")


@frozen.funcDeco(
    funcnames=Cfg.cfg.data["frozen"]["dict"],
    NonFrozen=dict[Key, Value],
)
class BaseDataDict(
    BaseDataObject,
    collections.abc.Mapping[Key, Value],
):
    __slots__ = ()
    data: frozendict[Key, Value]

    @abstractmethod
    def __init__(self:Self, data: Any, /, **kwargs:Any) -> None: ...

    @classmethod
    def fromkeys(cls: type, keys: Iterable, value: Any = None, /) -> Self:
        'Create a new dictionary with keys from iterable and values set to value.'
        return cls(frozendict.fromkeys(keys, value))
