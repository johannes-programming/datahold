__all__: list[str] = [
    "TestCopy",
    "TestDataAttribute",
    "TestFrozenHoldLists",
    "TestFrozenMutability",
]
import unittest
from typing import Any, Self

from datahold import BaseHoldObject, FrozenDataList


class FrozenHoldList[Item](
    BaseHoldObject[FrozenDataList.Data[Item]],
    FrozenDataList[Item],
):
    """Provide usable frozen list-like with slots."""

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
        cls, args = (FrozenHoldList, ([1, 2],))
        # They must not *define* copy themselves
        self.assertNotIn("copy", cls.__dict__)
        # Optional: if they *do* expose copy on the instance, it should not
        # create a mutable variant; you can drop this if you prefer.
        obj = cls(*args)
        if hasattr(obj, "copy"):
            copy_obj = obj.copy()
            self.assertIsInstance(copy_obj, cls)


class TestDataAttribute(unittest.TestCase):
    def test_list_data_is_tuple(self: Self) -> None:
        f: FrozenHoldList[Any]
        f = FrozenHoldList([1, 2, 3])
        self.assertIsInstance(f.__fget__(), list)


class TestFrozenHoldList(unittest.TestCase):

    def setUp(self: Self) -> None:
        self.obj = FrozenHoldList([1, 2, 3])
        self.same = FrozenHoldList([1, 2, 3])
        self.other = FrozenHoldList([1, 2, 4])

    # __init__
    def test_init(self: Self) -> None:
        obj: FrozenHoldList[int]
        obj = FrozenHoldList([42])
        self.assertEqual(obj.__fget__(), [42])

    # data property
    def test_data(self: Self) -> None:
        self.assertIsInstance(self.obj.__fget__(), list)
        self.assertEqual(self.obj.__fget__(), [1, 2, 3])

    # __contains__
    def test_contains(self: Self) -> None:
        self.assertIn(2, self.obj)
        self.assertNotIn(99, self.obj)

    # __getitem__
    def test_getitem(self: Self) -> None:
        self.assertEqual(self.obj[0], 1)
        self.assertEqual(self.obj[-1], 3)

    def test_getitem_slice(self: Self) -> None:
        result: Any
        result = self.obj[1:]
        self.assertEqual(result, FrozenHoldList([2, 3]))
        self.assertEqual(list(result), [2, 3])

    # __iter__
    def test_iter(self: Self) -> None:
        self.assertEqual(list(iter(self.obj)), [1, 2, 3])

    # __len__
    def test_len(self: Self) -> None:
        self.assertEqual(len(self.obj), 3)

    # __eq__
    def test_eq(self: Self) -> None:
        self.assertEqual(self.obj, self.same)
        self.assertFalse(self.obj == self.other)

    # __ne__
    def test_ne(self: Self) -> None:
        self.assertNotEqual(self.obj, self.other)
        self.assertFalse(self.obj != self.same)

    # __lt__
    def test_lt(self: Self) -> None:
        expected: bool
        expected = self.obj.__fget__() < self.other.__fget__()
        self.assertEqual(self.obj < self.other, expected)

    # __le__
    def test_le(self: Self) -> None:
        expected: bool
        expected = self.obj.__fget__() <= self.same.__fget__()
        self.assertEqual(self.obj <= self.same, expected)

    # __gt__
    def test_gt(self: Self) -> None:
        expected: bool
        expected = self.other.__fget__() > self.obj.__fget__()
        self.assertEqual(self.other > self.obj, expected)

    # __ge__
    def test_ge(self: Self) -> None:
        expected: bool
        expected = self.obj.__fget__() >= self.same.__fget__()
        self.assertEqual(self.obj >= self.same, expected)

    # __hash__
    def test_hash(self: Self) -> None:
        self.assertEqual(hash(self.obj), hash(tuple(self.obj.__fget__())))
        self.assertEqual(hash(self.obj), hash(self.same))

    # __add__
    def test_add(self: Self) -> None:
        result: Any
        result = self.obj + FrozenHoldList([4, 5])
        self.assertIsInstance(result, FrozenHoldList)
        self.assertEqual(
            result,
            FrozenHoldList([1, 2, 3, 4, 5]),
        )

    # __mul__
    def test_mul(self: Self) -> None:
        result: Any
        result = self.obj * 2
        self.assertIsInstance(result, FrozenHoldList)
        self.assertEqual(
            result,
            FrozenHoldList([1, 2, 3, 1, 2, 3]),
        )

    # __rmul__
    def test_rmul(self: Self) -> None:
        result: Any
        result = 2 * self.obj
        self.assertIsInstance(result, FrozenHoldList)
        self.assertEqual(
            result,
            FrozenHoldList([1, 2, 3, 1, 2, 3]),
        )

    # __reversed__
    def test_reversed(self: Self) -> None:
        self.assertEqual(
            list(reversed(self.obj)),
            [3, 2, 1],
        )

    # __repr__
    def test_repr(self: Self) -> None:
        self.assertEqual(
            repr(self.obj),
            "FrozenHoldList([1, 2, 3])",
        )

    # count
    def test_count(self: Self) -> None:
        obj: FrozenHoldList[int]
        obj = FrozenHoldList([1, 2, 1, 3, 1])
        self.assertEqual(obj.count(1), 3)
        self.assertEqual(obj.count(99), 0)

    # index
    def test_index(self: Self) -> None:
        self.assertEqual(self.obj.index(2), 1)
        with self.assertRaises(ValueError):
            self.obj.index(99)


class TestFrozenMutability(unittest.TestCase):
    def test_frozen_list_cannot_mutate(self: Self) -> None:
        f: Any
        f = FrozenHoldList([1, 2, 3])
        with self.assertRaises((TypeError, AttributeError)):
            f.append(4)
        with self.assertRaises((TypeError, AttributeError)):
            f.pop()


if __name__ == "__main__":
    unittest.main()
