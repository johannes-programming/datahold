import collections
from typing import *

from datahold._utils import frozen
from datahold._utils.Cfg import Cfg
from .BaseDataObject import BaseDataObject
from abc import abstractmethod
__all__ = ["BaseDataSet"]

Item = TypeVar("Item")


@frozen.funcDeco(
    funcnames=Cfg.cfg.data["frozen"]["set"],
    NonFrozen=frozenset[Item],
)
class BaseDataSet(
    BaseDataObject,
    collections.abc.Set[Item],
):
    __slots__ = ()
    data: frozenset[Item]
    
    @abstractmethod
    def __init__(self:Self, data: Iterable, /) -> None: ...

