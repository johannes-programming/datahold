from __future__ import annotations

__all__: list[str] = [
    "ContextManager",
]

from types import TracebackType
from typing import Protocol, Self, TypeVar

Enter = TypeVar("Enter", covariant=True)

### TYPING ###


class ContextManager(Protocol[Enter]):
    def __enter__(self: Self, /) -> Enter: ...

    def __exit__(
        self: Self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
        /,
    ) -> object: ...
