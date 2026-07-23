__all__: list[str] = ["TestFrozenHoldDict"]

import unittest
from typing import Any, Self

from frozendict import frozendict

from datahold import FrozenHoldDict


class TestFrozenHoldDict(unittest.TestCase):

    def setUp(self: Self) -> None:
        self.obj: Any = FrozenHoldDict({"a": 1, "b": 2})
        self.same: Any = FrozenHoldDict({"a": 1, "b": 2})
        self.other: Any = FrozenHoldDict({"a": 1, "b": 3})

    # __init__
    def test_init(self: Self) -> None:
        obj: Any
        obj = FrozenHoldDict({"x": 42})
        self.assertEqual(obj.__fget__(), frozendict({"x": 42}))

    # data property
    def test_data(self: Self) -> None:
        self.assertIsInstance(self.obj.__fget__(), frozendict)
        self.assertEqual(self.obj.__fget__(), frozendict({"a": 1, "b": 2}))

    # __contains__
    def test_contains(self: Self) -> None:
        self.assertIn("a", self.obj)
        self.assertNotIn("c", self.obj)

    # __getitem__
    def test_getitem(self: Self) -> None:
        self.assertEqual(self.obj["a"], 1)

    # __iter__
    def test_iter(self: Self) -> None:
        self.assertEqual(list(iter(self.obj)), ["a", "b"])

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

    # __hash__
    def test_hash(self: Self) -> None:
        self.assertEqual(hash(self.obj), hash(self.obj.__fget__()))
        self.assertEqual(hash(self.obj), hash(self.same))

    # __or__
    def test_or(self: Self) -> None:
        left: Any
        result: Any
        right: Any
        left = FrozenHoldDict({"a": 1})
        right = FrozenHoldDict({"b": 2})

        result = left | right

        self.assertIsInstance(result, FrozenHoldDict)
        self.assertEqual(
            result,
            FrozenHoldDict({"a": 1, "b": 2}),
        )

    # __repr__
    def test_repr(self: Self) -> None:
        self.assertEqual(
            repr(self.obj),
            "FrozenHoldDict({'a': 1, 'b': 2})",
        )

    # fromkeys
    def test_fromkeys(self: Self) -> None:
        result: Any
        result = FrozenHoldDict.fromkeys(
            ["x", "y"],
            123,
        )

        self.assertIsInstance(result, FrozenHoldDict)
        self.assertEqual(
            result,
            FrozenHoldDict({"x": 123, "y": 123}),
        )

    # get
    def test_get(self: Self) -> None:
        self.assertEqual(self.obj.get("a"), 1)
        self.assertIsNone(self.obj.get("missing"))
        self.assertEqual(self.obj.get("a", 999), 1)
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


if __name__ == "__main__":
    unittest.main()
