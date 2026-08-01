from __future__ import annotations

__all__: list[str] = ["TestAbstractmethods"]

import inspect as ins
import unittest
from typing import Any, Optional, Self

from Lazy import Lazy

import datahold


class TestAbstractmethods(unittest.TestCase):
    def _test(
        self: Self, name: str, abstractmethods: Optional[list[str]] = None, /
    ) -> None:
        datatype: Any
        if abstractmethods is None:
            return
        datatype = getattr(datahold, name)
        self.assertSetEqual(datatype.__abstractmethods__, set(abstractmethods))
        self.assertEqual(ins.isabstract(datatype), bool(abstractmethods))

    def test_abstractmethods(self: Self, /) -> None:
        data: Any
        name: Any
        for name, data in Lazy.lazy.datatypes.items():
            with self.subTest(datatype=name):
                self._test(name, data.get("abstractmethods"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
