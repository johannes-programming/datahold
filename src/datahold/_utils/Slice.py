__all__: list[str] = ["Slice"]

from typing import Optional

type Slice[Index] = slice[Optional[Index], Optional[Index], Optional[Index]]
