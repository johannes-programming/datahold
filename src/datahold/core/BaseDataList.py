import collections
from typing import *

from datahold._utils import frozen
from datahold._utils.Cfg import Cfg
from .BaseDataObject import BaseDataObject
from abc import abstractmethod
__all__ = ["BaseDataList"]

Item = TypeVar("Item")


@frozen.funcDeco(
    funcnames=Cfg.cfg.data["frozen"]["list"],
    NonFrozen=tuple[Item, ...],
)
class BaseDataList(
    BaseDataObject,
    collections.abc.Sequence[Item],
):
    __slots__ = ()
    data: tuple[Item, ...]
    @abstractmethod
    def __init__(self:Self, data: Iterable, /) -> None: ...

