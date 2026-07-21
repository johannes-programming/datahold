"""Provide BaseDataAbstractSet."""

__all__ = ["BaseDataAbstractSet"]


from collections.abc import Set

from .BaseDataCollection import BaseDataCollection


class BaseDataAbstractSet[Item](
    BaseDataCollection[Item],
    Set[Item],
):
    """Provide an easy abc for a custom (abstract) set."""

    __slots__ = ()
