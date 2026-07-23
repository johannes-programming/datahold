"""Provide BaseDataAbstractSet."""

__all__: list[str] = ["BaseDataAbstractSet"]

from collections import abc

from .BaseDataCollection import BaseDataCollection


class BaseDataAbstractSet[Item](
    BaseDataCollection[Item],
    abc.Set[Item],
):
    """Provide an easy abc for a custom (abstract) set."""

    __slots__ = ()
