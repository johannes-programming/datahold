__all__: list[str] = ["TestData"]

import unittest
from typing import Any, Self

from datahold import core


class TestData(unittest.TestCase):

    def test_doc(self: Self) -> None:
        name: str
        s: str
        t: str
        for s in ("Data", "Hold"):
            for t in ("Object", "Dict", "List", "Set"):
                name = s + t
                with self.subTest(name=name):
                    self.go(name=name)

    def go(self: Self, name: str) -> None:
        attrname: Any
        cls: Any
        doc: Any
        error: Any
        member: Any
        module: Any
        obj: Any
        module = getattr(core, name)
        cls = getattr(module, name)
        for attrname in dir(cls):
            member = getattr(cls, attrname)
            if not callable(member) and not isinstance(member, property):
                continue
            if getattr(member, "__isabstractmethod__", False):
                continue
            if attrname in ("__init_subclass__", "__subclasshook__"):
                continue
            if getattr(member, "__module__", None) == "collections.abc":
                continue
            doc = getattr(member, "__doc__", None)
            error = "%r inside %r has no docstring" % (attrname, name)
            self.assertIsNotNone(doc, error)
        try:
            obj = cls()
        except TypeError:
            return
        with self.assertRaises(AttributeError):
            obj.foo = 42


if __name__ == "__main__":
    unittest.main()
