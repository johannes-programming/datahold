from collections.abc import Hashable, Iterable
from typing import Optional, Self, TypeVar

import setdoc
from frozendict import frozendict

from ..base.BaseHoldDict import BaseHoldDict
from ..typing.SupportsKeysAndGetitem import SupportsKeysAndGetitem
from .FrozenDataDict import FrozenDataDict
from .FrozenHoldObject import FrozenHoldObject

__all__ = ["FrozenHoldDict"]

Key = TypeVar("Key", bound=Hashable, covariant=True)
Value = TypeVar("Value", covariant=True)


class FrozenHoldDict(
    FrozenHoldObject, FrozenDataDict[Key, Value], BaseHoldDict[Key, Value]
):

    __slots__ = ()

    @setdoc.basic
    def __init__(
        self: Self,
        data: (
            SupportsKeysAndGetitem[Key | str, Optional[Value]]
            | Iterable[tuple[Key | str, Optional[Value]]]
        ),
        /,
        **kwargs: Optional[Value],
    ) -> None:
        self._data = frozendict(data, **kwargs)  # type: ignore[arg-type]
