__all__: list[str] = ["TestFrozenHoldLists"]
import unittest
from typing import Self

from datahold.frozen.FrozenHoldList import FrozenHoldList


class TestFrozenHoldList(unittest.TestCase):

    def setUp(self: Self) -> None:
        self.obj = FrozenHoldList([1, 2, 3])
        self.same = FrozenHoldList([1, 2, 3])
        self.other = FrozenHoldList([1, 2, 4])

    # __init__
    def test_init(self: Self) -> None:
        obj = FrozenHoldList([42])
        self.assertEqual(obj.data, (42,))

    # data property
    def test_data(self: Self) -> None:
        self.assertIsInstance(self.obj.data, tuple)
        self.assertEqual(self.obj.data, (1, 2, 3))

    # __contains__
    def test_contains(self: Self) -> None:
        self.assertIn(2, self.obj)
        self.assertNotIn(99, self.obj)

    # __getitem__
    def test_getitem(self: Self) -> None:
        self.assertEqual(self.obj[0], 1)
        self.assertEqual(self.obj[-1], 3)

    def test_getitem_slice(self: Self) -> None:
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
        expected = self.obj.data < self.other.data
        self.assertEqual(self.obj < self.other, expected)

    # __le__
    def test_le(self: Self) -> None:
        expected = self.obj.data <= self.same.data
        self.assertEqual(self.obj <= self.same, expected)

    # __gt__
    def test_gt(self: Self) -> None:
        expected = self.other.data > self.obj.data
        self.assertEqual(self.other > self.obj, expected)

    # __ge__
    def test_ge(self: Self) -> None:
        expected = self.obj.data >= self.same.data
        self.assertEqual(self.obj >= self.same, expected)

    # __hash__
    def test_hash(self: Self) -> None:
        self.assertEqual(hash(self.obj), hash(self.obj.data))
        self.assertEqual(hash(self.obj), hash(self.same))

    # __add__
    def test_add(self: Self) -> None:
        result = self.obj + FrozenHoldList([4, 5])

        self.assertIsInstance(result, FrozenHoldList)
        self.assertEqual(
            result,
            FrozenHoldList([1, 2, 3, 4, 5]),
        )

    # __mul__
    def test_mul(self: Self) -> None:
        result = self.obj * 2

        self.assertIsInstance(result, FrozenHoldList)
        self.assertEqual(
            result,
            FrozenHoldList([1, 2, 3, 1, 2, 3]),
        )

    # __rmul__
    def test_rmul(self: Self) -> None:
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
        obj = FrozenHoldList([1, 2, 1, 3, 1])

        self.assertEqual(obj.count(1), 3)
        self.assertEqual(obj.count(99), 0)

    # index
    def test_index(self: Self) -> None:
        self.assertEqual(self.obj.index(2), 1)

        with self.assertRaises(ValueError):
            self.obj.index(99)


if __name__ == "__main__":
    unittest.main()
