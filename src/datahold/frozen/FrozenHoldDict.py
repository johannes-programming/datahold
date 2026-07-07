"""Provide FrozenHoldDict."""

__all__: list[str] = ["FrozenHoldDict"]

from collections.abc import Hashable, Iterable
from typing import Optional, Self, TypeVar

import setdoc
from frozendict import frozendict

from ..base.BaseHoldDict import BaseHoldDict
from ..typing.SupportsKeysAndGetitem import SupportsKeysAndGetitem
from .FrozenDataDict import FrozenDataDict
from .FrozenHoldObject import FrozenHoldObject

Key = TypeVar("Key", bound=Hashable, covariant=True)
Value = TypeVar("Value", covariant=True)


class FrozenHoldDict(
    FrozenDataDict[Key, Value], FrozenHoldObject, BaseHoldDict[Key, Value]
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
