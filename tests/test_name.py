from __future__ import annotations

__all__: list[str] = ["TestName"]

import unittest
from collections import abc
from typing import Self

from Lazy import Lazy

import datahold


class TestName(unittest.TestCase):

    def _test_name(self: Self, name: str, /) -> None:
        prefix: str
        suffix: str
        if name.startswith("Frozen"):
            prefix = "Frozen"
        elif name.startswith("Mutable"):
            prefix = "Mutable"
        else:
            prefix = ""
        if name.endswith("Like"):
            suffix = "Like"
        elif name.endswith("Slot"):
            suffix = "Slot"
        else:
            suffix = ""
        # all
        datatype = getattr(datahold, name)
        self.assertEqual(datatype.__name__, name)
        self.assertTrue(issubclass(datatype, datahold.Object))
        if "Object" in name:
            return
        self.assertTrue(issubclass(datatype, datahold.Collection))
        self.assertTrue(hasattr(datatype, "__frozen__"))
        # frozen
        if prefix == "Frozen":
            self.assertIsNot(datatype.__hash__, object.__hash__)
            self.assertTrue(issubclass(datatype, abc.Hashable))
            self.assertFalse(hasattr(datatype, "__mutate__"))
            ancestor = getattr(datahold, name[6:], object)
            self.assertTrue(issubclass(datatype, ancestor))
        # mutable
        if prefix == "Mutable":
            self.assertIn(datatype.__hash__, [None, object.__hash__])
            self.assertTrue(hasattr(datatype, "__mutate__"))
            self.assertTrue(issubclass(datatype, datahold.MutableObject))
            ancestor = getattr(datahold, name[7:], object)
            self.assertTrue(issubclass(datatype, ancestor))
        # no prefix
        if prefix == "":
            self.assertIn(datatype.__hash__, [None, object.__hash__])
            self.assertFalse(hasattr(datatype, "__mutate__"))
        # like
        if suffix == "Like":
            self.assertTrue(hasattr(datatype, "__init__"))
        # slot
        if suffix == "Slot":
            self.assertTrue(hasattr(datatype, "__init__"))
            self.assertTrue(issubclass(datatype, datahold.ObjectSlot))
            ancestor = getattr(datahold, name[:-4] + "Like")
            self.assertTrue(issubclass(datatype, ancestor))
        # no suffix
        if suffix == "":
            self.assertIs(datatype.__init__, object.__init__)

    def test_name(self: Self, /) -> None:
        for name in Lazy.lazy.datatypes.keys():
            with self.subTest(datatype=name):
                self._test_name(name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
