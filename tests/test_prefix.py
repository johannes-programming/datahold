from __future__ import annotations

__all__: list[str] = ["TestPrefix"]

import unittest
from collections import abc
from typing import Self

from Lazy import Lazy

import datahold


class TestPrefix(unittest.TestCase):
    def _test_prefix(self: Self, name: str, /) -> None:
        datatype = getattr(datahold, name)
        self.assertEqual(datatype.__name__, name)
        self.assertTrue(hasattr(datatype, "__Frozen__"))
        self.assertTrue(hasattr(datatype, "__frozen__"))
        if name.startswith("Frozen"):
            self.assertIsNot(datatype.__hash__, object.__hash__)
            self.assertTrue(issubclass(datatype, abc.Hashable))
            self.assertFalse(hasattr(datatype, "__Mutable__"))
            self.assertFalse(hasattr(datatype, "__mutate__"))
            return
        self.assertIn(datatype.__hash__, [None, object.__hash__])
        if name.startswith("Mutable"):
            self.assertTrue(hasattr(datatype, "__Mutable__"))
            self.assertTrue(hasattr(datatype, "__mutate__"))
            return
        self.assertFalse(hasattr(datatype, "__Mutable__"))
        self.assertFalse(hasattr(datatype, "__mutate__"))

    def test_prefix(self: Self, /) -> None:
        for name in Lazy.lazy.datatypes.keys():
            with self.subTest(datatype=name):
                self._test_prefix(name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
