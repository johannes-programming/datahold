__all__:list[str]=["DataCopyable"]

from typing import Self
import setdoc
from abc import abstractmethod, ABCMeta

class DataCopyable(metaclass=ABCMeta):
    __slots__=()
    
    @abstractmethod
    @setdoc.basic
    def __init__(self:Self, data: Self, /) -> None:
        ...

    @setdoc.basic
    def copy(self:Self) -> Self:
        return type(self)(self)