import unittest
from typing import *

from datahold import core
from datahold.core import *


class TestData(unittest.TestCase):
    def test_constructor_abc(self: Self) -> None:
        with self.assertRaises(Exception):
            core.DataDict.DataDict()
        with self.assertRaises(Exception):
            core.DataList.DataList()
        with self.assertRaises(Exception):
            core.DataSet.DataSet()

    def test_constructor_core(self: Self) -> None:
        core.HoldDict.HoldDict()
        core.HoldList.HoldList()
        core.HoldSet.HoldSet()

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
            if attrname == "__subclasshook__":
                continue
            doc = getattr(member, "__doc__", None)
            error = "%r inside %r has no docstring" % (attrname, name)
            self.assertNotEqual(doc, None, error)
        try:
            obj = cls()
        except TypeError:
            return
        with self.assertRaises(AttributeError):
            obj.foo = 42


if __name__ == "__main__":
    unittest.main()
