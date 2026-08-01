from __future__ import annotations

__all__: list[str] = ["TestIssubclass"]

import unittest
from typing import Self

from Lazy import Lazy

import datahold


class TestIssubclass(unittest.TestCase):
    def _test_issubclass(self: Self, name: str, /, **kwargs: bool) -> None:
        datatype = getattr(datahold, name)
        for x, y in kwargs.items():
            superclass = Lazy.get_import(x)
            answer = issubclass(datatype, superclass)
            with self.subTest(superclass=x, answer=answer, solution=y):
                self.assertEqual(answer, y)

    def test_issubclass(self: Self, /) -> None:
        for name, data in Lazy.lazy.datatypes.items():
            with self.subTest(datatype=name):
                self._test_issubclass(name, **data["issubclass"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
