from __future__ import annotations

__all__: list[str] = ["BaseDataAbstractSet"]
from collections.abc import Set

from .BaseDataCollection import BaseDataCollection


class BaseDataAbstractSet[Item](
    BaseDataCollection[Item],
    Set[Item],
):
    """Act as base class for (abstract) set implementation which only needs overriding of __data__ to work immediately."""

    __slots__ = ()
