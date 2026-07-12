__all__: list[str] = []
from collections.abc import Sequence
from typing import reveal_type

reveal_type(Sequence.__getitem__)
