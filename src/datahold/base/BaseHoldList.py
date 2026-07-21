"""Provide BaseHoldList."""

__all__: list[str] = ["BaseHoldList"]


from .BaseDataList import BaseDataList
from .BaseHoldCollection import BaseHoldCollection


class BaseHoldList[Item](
    BaseDataList[Item], 
    BaseHoldCollection[Item],
):
    __slots__ = ()
