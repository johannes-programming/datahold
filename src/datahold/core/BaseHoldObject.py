from typing import *

from .BaseDataObject import BaseDataObject

__all__ = ["HoldBase"]


class BaseHoldObject(BaseDataObject):
    __slots__ = ("_data",)
    data: Any
