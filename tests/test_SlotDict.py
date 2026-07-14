__all__: list[str] = ["Test_SlotDict"]
import unittest
from typing import Any, Optional, Self

from frozendict import frozendict

from datahold.core.SlotDict import SlotDict


class Test_SlotDict(unittest.TestCase):
    def setUp(self: Self) -> None:
        self.payload: dict[str, Optional[int]]
        self.payload = {"a": 1, "b": 2, "c": None}
        self.slotdict = SlotDict(self.payload)
        self.dict_ = dict(self.payload)

    # ------------------------------------------------------------------
    # Directly test explicit methods
    # ------------------------------------------------------------------

    def test_init(self: Self) -> None:
        sd: SlotDict[Any, Any]
        self.assertEqual(dict(self.slotdict), self.dict_)
        sd = SlotDict([("x", 1), ("y", 2)])
        self.assertEqual(dict(sd), {"x": 1, "y": 2})
        sd = SlotDict(x=1, y=2)
        self.assertEqual(dict(sd), {"x": 1, "y": 2})

    def test_fget(self: Self) -> None:
        data: frozendict[Any, Any]
        data = self.slotdict.__fget__()
        self.assertIsInstance(data, frozendict)
        self.assertEqual(data, frozendict(self.payload))

    def test_fset(self: Self) -> None:
        new_data: frozendict[str, int]
        new_data = frozendict({"x": 10, "y": 20})
        self.slotdict.__fset__(new_data)
        self.assertEqual(dict(self.slotdict), {"x": 10, "y": 20})
        self.assertEqual(self.slotdict.__fget__(), new_data)

    def test_fromkeys(self: Self) -> None:
        result: SlotDict[Any, Any]
        result = SlotDict.fromkeys(("a", "b", "c"), 123)
        self.assertIsInstance(result, SlotDict)
        self.assertEqual(dict(result), dict.fromkeys(("a", "b", "c"), 123))

    # ------------------------------------------------------------------
    # Test magic methods only through builtins/operators
    # ------------------------------------------------------------------

    def test_len(self: Self) -> None:
        self.assertEqual(len(self.slotdict), len(self.dict_))

    def test_iter(self: Self) -> None:
        self.assertEqual(list(iter(self.slotdict)), list(iter(self.dict_)))

    def test_contains_operator(self: Self) -> None:
        key: Any
        for key in self.dict_:
            self.assertEqual(key in self.slotdict, key in self.dict_)
        self.assertEqual("missing" in self.slotdict, "missing" in self.dict_)

    def test_subscription_operator(self: Self) -> None:
        key: Any
        for key in self.dict_:
            self.assertEqual(self.slotdict[key], self.dict_[key])
        with self.assertRaises(KeyError):
            _ = self.slotdict["missing"]

    def test_equality_operator(self: Self) -> None:
        self.assertTrue(self.slotdict == SlotDict(self.payload))
        self.assertFalse(self.slotdict == SlotDict({"a": 1}))
        self.assertEqual(self.slotdict == SlotDict(self.payload), True)

    def test_union_operator(self: Self) -> None:
        other: dict[str, int]
        other = {"d": 4, "a": 99}
        result = self.slotdict | SlotDict(other)
        expected = self.dict_ | other
        self.assertIsInstance(result, SlotDict)
        self.assertEqual(dict(result), expected)

    def test_dict_constructor(self: Self) -> None:
        self.assertEqual(dict(self.slotdict), self.dict_)

    def test_list_constructor(self: Self) -> None:
        self.assertEqual(list(self.slotdict), list(self.dict_))

    def test_tuple_constructor(self: Self) -> None:
        self.assertEqual(tuple(self.slotdict), tuple(self.dict_))


if __name__ == "__main__":
    unittest.main()
