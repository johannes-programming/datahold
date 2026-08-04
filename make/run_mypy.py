__all__: list[str] = []
from typing import reveal_type

import datahold

reveal_type(list.__ge__)
reveal_type(list.sort)
reveal_type(datahold.MutableSequence.__frozen__)
reveal_type(datahold.MutableListLike.__frozen__)
