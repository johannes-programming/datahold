"""Provide BaseDataAbstractSet."""

__all__ = ["BaseDataAbstractSet"]


from collections.abc import Set

from .BaseDataCollection import BaseDataCollection


class BaseDataAbstractSet[Item](
    BaseDataCollection[Item],
    Set[Item],
):
    __slots__ = ()
