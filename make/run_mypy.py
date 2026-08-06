__all__: list[str] = []
from collections import abc
from typing import reveal_type

from frozendict import frozendict

import datahold

reveal_type(list.__ge__)
reveal_type(list.sort)
reveal_type(datahold.MutableSequence.__frozen__)
reveal_type(datahold.MutableListLike.__frozen__)


def cast_as_Mapping_Frozen[Key: abc.Hashable, Value](
    value: frozendict[Key | str, Value | None],
) -> datahold.Mapping_Frozen[Key | str, Value | None]:
    return value
