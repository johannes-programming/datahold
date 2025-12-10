from abc import ABCMeta, abstractmethod
from typing import *

__all__ = ["BaseDataObject"]


class BaseDataObject(metaclass=ABCMeta):
    __slots__ = ()

    data: Any

    @property
    @abstractmethod
    def data(self: Self) -> Any: ...
