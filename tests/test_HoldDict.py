__all__: list[str] = [
    "TestDataAttribute",
    "TestHoldDict",
    "TestMutableBehavior",
    "TestCopy",
]
import unittest
from collections import abc
from typing import Any, Self, cast

from datahold import BaseHoldObject, DataDict


class HoldDict[Key: abc.Hashable, Value](
    BaseHoldObject[DataDict.Data[Key, Value]],
    DataDict[Key, Value],
):
    """Provide usable mutable dict-like with slots."""

    __slots__ = ()


class TestCopy(unittest.TestCase):
    def test_mutable_copy_returns_same_type_and_is_shallow(self: Self) -> None:
        d: HoldDict[str, dict[str, int]]
        d_copy: HoldDict[str, dict[str, int]]
        d = HoldDict({"a": {"x": 1}})
        d_copy = d.copy()
        self.assertIsInstance(d_copy, type(d))
        self.assertIsNot(d_copy, d)
        self.assertEqual(dict(d_copy), dict(d))

        # shallow: inner object is shared
        cast(dict[str, int], d["a"])["x"] = 2
        self.assertEqual(cast(dict[str, int], d_copy["a"])["x"], 2)


class TestDataAttribute(unittest.TestCase):
    def test_dict_data_is_immutable_mapping(self: Self) -> None:
        m: HoldDict[Any, Any]
        m = HoldDict({"a": 1})
        self.assertIsInstance(m.__fget__(), dict)


class TestHoldDict(unittest.TestCase):

    def setUp(self: Self) -> None:
        self.obj: Any
        self.other: Any
        self.same: Any
        self.obj = HoldDict({"a": 1, "b": 2})
        self.same = HoldDict({"a": 1, "b": 2})
        self.other = HoldDict({"a": 1, "b": 3})

    # __init__
    def test_init(self: Self) -> None:
        obj: Any
        obj = HoldDict({"x": 42})
        self.assertEqual(obj.__fget__(), {"x": 42})

    # data property
    def test_data(self: Self) -> None:
        self.assertIsInstance(self.obj.__fget__(), dict)
        self.assertEqual(self.obj.__fget__(), {"a": 1, "b": 2})

    # __contains__
    def test_contains(self: Self) -> None:
        self.assertIn("a", self.obj)
        self.assertNotIn("c", self.obj)

    # __getitem__
    def test_getitem(self: Self) -> None:
        self.assertEqual(self.obj["a"], 1)

    # __setitem__
    def test_setitem(self: Self) -> None:
        self.obj["c"] = 3
        self.assertEqual(self.obj["c"], 3)

    # __delitem__
    def test_delitem(self: Self) -> None:
        del self.obj["a"]
        self.assertNotIn("a", self.obj)

    # __iter__
    def test_iter(self: Self) -> None:
        self.assertEqual(set(iter(self.obj)), {"a", "b"})

    # __len__
    def test_len(self: Self) -> None:
        self.assertEqual(len(self.obj), 2)

    # __eq__
    def test_eq(self: Self) -> None:
        self.assertEqual(self.obj, self.same)
        self.assertFalse(self.obj == self.other)

    # __ne__
    def test_ne(self: Self) -> None:
        self.assertNotEqual(self.obj, self.other)
        self.assertFalse(self.obj != self.same)

    # __or__
    def test_or(self: Self) -> None:
        result: Any
        result = HoldDict({"a": 1}) | HoldDict({"b": 2})
        self.assertIsInstance(result, HoldDict)
        self.assertEqual(
            result,
            HoldDict({"a": 1, "b": 2}),
        )

    # __repr__
    def test_repr(self: Self) -> None:
        self.assertEqual(
            repr(self.obj),
            "HoldDict({'a': 1, 'b': 2})",
        )

    # fromkeys
    def test_fromkeys(self: Self) -> None:
        result: Any
        result = HoldDict.fromkeys(["x", "y"], 123)
        self.assertIsInstance(result, HoldDict)
        self.assertEqual(
            result,
            HoldDict({"x": 123, "y": 123}),
        )

    # get
    def test_get(self: Self) -> None:
        self.assertEqual(self.obj.get("a"), 1)
        self.assertIsNone(self.obj.get("missing"))
        self.assertEqual(
            self.obj.get("missing", 999),
            999,
        )

    # items
    def test_items(self: Self) -> None:
        self.assertEqual(
            set(self.obj.items()),
            {("a", 1), ("b", 2)},
        )

    # keys
    def test_keys(self: Self) -> None:
        self.assertEqual(
            set(self.obj.keys()),
            {"a", "b"},
        )

    # values
    def test_values(self: Self) -> None:
        self.assertEqual(
            set(self.obj.values()),
            {1, 2},
        )

    # update
    def test_update(self: Self) -> None:
        self.obj.update({"c": 3})
        self.assertEqual(
            self.obj,
            HoldDict({"a": 1, "b": 2, "c": 3}),
        )

    # setdefault
    def test_setdefault(self: Self) -> None:
        value: Any
        value = self.obj.setdefault("c", 3)
        self.assertEqual(value, 3)
        self.assertEqual(self.obj["c"], 3)

    # pop
    def test_pop(self: Self) -> None:
        value: Any
        value = self.obj.pop("a")
        self.assertEqual(value, 1)
        self.assertNotIn("a", self.obj)

    # popitem
    def test_popitem(self: Self) -> None:
        key: Any
        value: Any
        key, value = self.obj.popitem()
        self.assertNotIn(key, self.obj)
        self.assertIn(value, {1, 2})

    # clear
    def test_clear(self: Self) -> None:
        self.obj.clear()
        self.assertEqual(len(self.obj), 0)

    # copy
    def test_copy(self: Self) -> None:
        result: Any
        result = self.obj.copy()
        self.assertIsInstance(result, HoldDict)
        self.assertEqual(result, self.obj)
        self.assertIsNot(result, self.obj)


class TestMutableBehavior(unittest.TestCase):
    def test_hold_dict_mutates_and_syncs_data(self: Self) -> None:
        x: HoldDict[Any, Any]
        x = HoldDict({"a": 1})
        x["b"] = 2
        self.assertEqual(x["b"], 2)
        self.assertEqual(x.__fget__()["b"], 2)


if __name__ == "__main__":
    unittest.main()
