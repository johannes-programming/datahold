__all__: list[str] = [
    "TestCopy",
    "TestDataAttribute",
    "TestFrozenHoldDict",
    "TestFrozenMutability",
]

import unittest
from collections import abc
from typing import Any, Self

from frozendict import frozendict

from datahold import BaseHoldObject, FrozenDataDict


class FrozenHoldDict[Key: abc.Hashable, Value](
    BaseHoldObject[FrozenDataDict.Data[Key, Value]],
    FrozenDataDict[Key, Value],
):
    """Provide usable frozen dict-like with slots."""

    __slots__ = ()


class TestCopy(unittest.TestCase):

    def test_frozen_have_no_copy_2(self: Self) -> None:
        """
        Frozen classes should not define their own copy method.
        (If a parent class or wrapped object exposes one, we ignore that.)
        """
        args: Any
        cls: Any
        copy_obj: Any
        obj: Any
        cls, args = (FrozenHoldDict, ({"a": 1},))
        # They must not *define* copy themselves
        self.assertNotIn("copy", cls.__dict__)
        # Optional: if they *do* expose copy on the instance, it should not
        # create a mutable variant; you can drop this if you prefer.
        obj = cls(*args)
        if hasattr(obj, "copy"):
            copy_obj = obj.copy()
            self.assertIsInstance(copy_obj, cls)


class TestDataAttribute(unittest.TestCase):
    def test_dict_data_is_immutable_mapping(self: Self) -> None:
        f: FrozenHoldDict[Any, Any]
        f = FrozenHoldDict({"a": 1})
        self.assertIsInstance(f.__fget__(), dict)


class TestFrozenHoldDict(unittest.TestCase):

    def setUp(self: Self) -> None:
        self.obj: Any = FrozenHoldDict({"a": 1, "b": 2})
        self.same: Any = FrozenHoldDict({"a": 1, "b": 2})
        self.other: Any = FrozenHoldDict({"a": 1, "b": 3})

    # __init__
    def test_init(self: Self) -> None:
        obj: Any
        obj = FrozenHoldDict({"x": 42})
        self.assertEqual(obj.__fget__(), dict({"x": 42}))

    # data property
    def test_data(self: Self) -> None:
        self.assertIsInstance(self.obj.__fget__(), dict)
        self.assertEqual(self.obj.__fget__(), dict({"a": 1, "b": 2}))

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
        self.assertEqual(hash(self.obj), hash(frozendict(self.obj.__fget__())))
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


class TestFrozenMutability(unittest.TestCase):
    def test_frozen_dict_cannot_mutate(self: Self) -> None:
        f: Any
        f = FrozenHoldDict({"a": 1})
        with self.assertRaises((TypeError, AttributeError)):
            f["b"] = 2
        with self.assertRaises((TypeError, AttributeError)):
            f.pop("a", None)


if __name__ == "__main__":
    unittest.main()
