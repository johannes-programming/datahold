from .BaseDataSet import BaseDataSet
from .DataObject import DataObject
from typing import *
from datahold._utils import unfrozen
from datahold._utils.Cfg import Cfg
import setdoc
import collections
__all__ = ["DataSet"]

Item = TypeVar("Item")

@unfrozen.funcDeco(
    funcnames=Cfg.cfg.data["unfrozen"]["set"],
    NonFrozen=set[Item],
)
class DataSet(DataObject, BaseDataSet[Item]):
    data:frozenset[Item]
    __slots__ = ()
    @setdoc.basic
    def __init__(self:Self, data:Iterable, /) -> None:
        self.data = frozenset[Item](data)

    



