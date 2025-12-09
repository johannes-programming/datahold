from .BaseDataDict import BaseDataDict
from .DataObject import DataObject
from typing import *
from frozendict import frozendict
from datahold._utils import unfrozen
from datahold._utils.Cfg import Cfg
import setdoc
import collections

__all__ = ["DataDict"]

Key = TypeVar("Key")
Value = TypeVar("Value")

@unfrozen.funcDeco(
    funcnames=Cfg.cfg.data["unfrozen"]["dict"],
    NonFrozen=dict[Key, Value],
)
class DataDict(DataObject, BaseDataDict[Key, Value], collections.abc.MutableMapping[Key, Value]):
    data:frozendict[Key, Value]
    __slots__ = ()
    @setdoc.basic
    def __init__(self:Self, data:Any, /, **kwargs:Any) -> None:
        self.data = frozendict[Key, Value](data, **kwargs)

    



