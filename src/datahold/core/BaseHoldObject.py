from typing import *

from .BaseDataObject import BaseDataObject

__all__ = ["BaseHoldObject"]


class BaseHoldObject(BaseDataObject):
    __slots__ = ("_data",)
