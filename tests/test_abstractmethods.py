from __future__ import annotations

__all__: list[str] = ["TestAbstractmethods"]

import inspect as ins
import unittest
from typing import Any, Self

from Lazy import Lazy

import datahold


class TestAbstractmethods(unittest.TestCase):
    def _test(self: Self, name: str, abstractmethods: set[str], /) -> None:
        datatype: Any
        datatype = getattr(datahold, name)
        self.assertLessEqual(len(datatype.__abstractmethods__), 2)
        self.assertSetEqual(datatype.__abstractmethods__, abstractmethods)
        self.assertEqual(ins.isabstract(datatype), bool(abstractmethods))

    def test_abstractmethods(self: Self, /) -> None:
        name: str
        for name in Lazy.lazy.datatypes.keys():
            if "Object" in name:
                continue
            with self.subTest(datatype=name):
                self._test(name, Lazy.get_abstractmethods(name))


if __name__ == "__main__":
    unittest.main(verbosity=2)
