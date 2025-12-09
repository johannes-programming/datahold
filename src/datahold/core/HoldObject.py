from typing import * 
from .BaseHoldObject import BaseHoldObject
from .DataObject import DataObject

__all__=["HoldObject"]

class HoldObject(BaseHoldObject, DataObject):
    data:Any
    __slots__=()
    