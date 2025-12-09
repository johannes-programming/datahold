from .BaseDataList import BaseDataList
from .DataObject import DataObject
from typing import *
from datahold._utils import unfrozen
from datahold._utils.Cfg import Cfg
import setdoc
import collections
__all__ = ["DataList"]

Item = TypeVar("Item")

@unfrozen.funcDeco(
    funcnames=Cfg.cfg.data["unfrozen"]["list"],
    NonFrozen=list[Item],
)
class DataList(DataObject, BaseDataList[Item], collections.abc.MutableSequence[Item]):
    data:tuple[Item, ...]
    __slots__ = ()
    @setdoc.basic
    def __init__(self:Self, data:Iterable, /) -> None:
        self.data = tuple[Item, ...](data)

    



