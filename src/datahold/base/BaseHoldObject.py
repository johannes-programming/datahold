import typing

from .BaseDataObject import BaseDataObject

__all__ = ["BaseHoldObject"]


class BaseHoldObject(BaseDataObject):
    data: typing.Any
    __slots__ = ("_data",)
