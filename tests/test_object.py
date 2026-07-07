__all__: list[str] = ["TestObject"]
import unittest
from importlib import import_module
from typing import Any, Self

from iterprod import iterprod

METHODS: tuple[str, ...]
MUTES: tuple[str, ...]
ROOTS: tuple[str, ...]
SLOTS: tuple[str, ...]
METHODS = ("__format__", "__str__")
MUTES = ("", "Base", "Frozen")
ROOTS = ("Object", "Dict", "List", "Set")
SLOTS = ("Data", "Hold")


class TestObject(unittest.TestCase):
    def _test_cls(self: Self, cls: type) -> None:
        method: Any
        for method in METHODS:
            with self.subTest(cls=cls):
                self.assertIs(getattr(cls, method), getattr(object, method))

    def test_object(self: Self) -> None:
        cls: type
        clsname: str
        importname: str
        mute: str
        root: str
        slot: str
        for mute, slot, root in iterprod(MUTES, SLOTS, ROOTS):
            clsname = mute + slot + root
            importname = "datahold."
            if mute:
                importname += mute.lower()
            else:
                importname += "core"
            importname += "." + clsname
            cls = getattr(import_module(name=importname), clsname)
            self._test_cls(cls)


if __name__ == "__main__":
    unittest.main()
