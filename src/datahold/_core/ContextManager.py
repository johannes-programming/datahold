from __future__ import annotations

__all__: list[str] = [
    "ContextManager",
]

from types import TracebackType
from typing import Protocol, Self

### TYPING ###


class ContextManager[Enter](Protocol):
    def __enter__(self: Self, /) -> Enter: ...

    def __exit__(
        self: Self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
        /,
    ) -> object: ...
