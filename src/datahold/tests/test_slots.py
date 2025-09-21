import unittest
from typing import *

from datahold.core import *


class TestGo(unittest.TestCase):
    def test_go(self: Self) -> None:
        types:list[type] = [
            HoldABC,
            HoldDict,
            HoldList,
            HoldSet,
            OkayABC,
            OkayDict,
            OkayList,
            OkaySet,
        ]
        t:type
        for t in types:
            with self.subTest(cls=t.__name__):
                self.go_ann(t)
                self.go_slot(t)

    def go_ann(self:Self, cls:type) -> None:
        self.assertEqual(list(cls.__annotations__.keys()), ["data"])

    def go_slot(self:Self, cls:type) -> None:
        obj:Any
        try:
            obj = cls()
        except Exception:
            return
        with self.assertRaises(AttributeError):
            obj.foo = 42


if __name__ == "__main__":
    unittest.main()
