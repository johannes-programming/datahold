import unittest
from typing import Any, Self

from datahold import HoldSet


class TestHoldSet(unittest.TestCase):

    def setUp(self: Self) -> None:
        self.obj: Any = HoldSet({1, 2, 3})
        self.same: Any = HoldSet({1, 2, 3})
        self.other: Any = HoldSet({3, 4, 5})

    # __init__
    def test_init(self: Self) -> None:
        obj: Any = HoldSet([1, 2, 3])
        self.assertEqual(obj.__fget__(), frozenset({1, 2, 3}))

    # data property
    def test_data(self: Self) -> None:
        self.assertIsInstance(self.obj.__fget__(), frozenset)
        self.assertEqual(self.obj.__fget__(), frozenset({1, 2, 3}))

    # __contains__
    def test_contains(self: Self) -> None:
        self.assertIn(1, self.obj)
        self.assertNotIn(999, self.obj)

    # __iter__
    def test_iter(self: Self) -> None:
        self.assertEqual(set(iter(self.obj)), {1, 2, 3})

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
        self.assertTrue(HoldSet({1, 2}) < HoldSet({1, 2, 3}))

    # __le__
    def test_le(self: Self) -> None:
        self.assertTrue(HoldSet({1, 2}) <= HoldSet({1, 2, 3}))
        self.assertTrue(HoldSet({1, 2}) <= HoldSet({1, 2}))

    # __gt__
    def test_gt(self: Self) -> None:
        self.assertTrue(HoldSet({1, 2, 3}) > HoldSet({1, 2}))

    # __ge__
    def test_ge(self: Self) -> None:
        self.assertTrue(HoldSet({1, 2, 3}) >= HoldSet({1, 2}))
        self.assertTrue(HoldSet({1, 2}) >= HoldSet({1, 2}))

    # __or__
    def test_or(self: Self) -> None:
        result: Any = HoldSet({1, 2}) | HoldSet({2, 3})

        self.assertIsInstance(result, HoldSet)
        self.assertEqual(
            result,
            HoldSet({1, 2, 3}),
        )

    # __and__
    def test_and(self: Self) -> None:
        result: Any = HoldSet({1, 2, 3}) & HoldSet({2, 3, 4})

        self.assertEqual(
            result,
            HoldSet({2, 3}),
        )

    # __sub__
    def test_sub(self: Self) -> None:
        result: Any = HoldSet({1, 2, 3}) - HoldSet({2})

        self.assertEqual(
            result,
            HoldSet({1, 3}),
        )

    # __xor__
    def test_xor(self: Self) -> None:
        result: Any = HoldSet({1, 2, 3}) ^ HoldSet({3, 4})

        self.assertEqual(
            result,
            HoldSet({1, 2, 4}),
        )

    # __repr__
    def test_repr(self: Self) -> None:
        self.assertEqual(
            repr(HoldSet({1, 2, 3})),
            "HoldSet({1, 2, 3})",
        )

    # add
    def test_add(self: Self) -> None:
        self.obj.add(4)

        self.assertEqual(
            self.obj,
            HoldSet({1, 2, 3, 4}),
        )

    # remove
    def test_remove(self: Self) -> None:
        self.obj.remove(2)

        self.assertEqual(
            self.obj,
            HoldSet({1, 3}),
        )

    # discard
    def test_discard(self: Self) -> None:
        self.obj.discard(2)
        self.obj.discard(999)

        self.assertEqual(
            self.obj,
            HoldSet({1, 3}),
        )

    # pop
    def test_pop(self: Self) -> None:
        value: Any = self.obj.pop()

        self.assertNotIn(value, self.obj)
        self.assertEqual(len(self.obj), 2)

    # clear
    def test_clear(self: Self) -> None:
        self.obj.clear()

        self.assertEqual(len(self.obj), 0)

    # update
    def test_update(self: Self) -> None:
        self.obj.update({4, 5})

        self.assertEqual(
            self.obj,
            HoldSet({1, 2, 3, 4, 5}),
        )

    # union
    def test_union(self: Self) -> None:
        result: Any = self.obj.union({4, 5})

        self.assertIsInstance(result, HoldSet)
        self.assertEqual(
            result,
            HoldSet({1, 2, 3, 4, 5}),
        )

    # intersection
    def test_intersection(self: Self) -> None:
        result: Any = self.obj.intersection({2, 3, 4})

        self.assertEqual(
            result,
            HoldSet({2, 3}),
        )

    # difference
    def test_difference(self: Self) -> None:
        result: Any = self.obj.difference({2})

        self.assertEqual(
            result,
            HoldSet({1, 3}),
        )

    # symmetric_difference
    def test_symmetric_difference(self: Self) -> None:
        result: Any = self.obj.symmetric_difference({3, 4})

        self.assertEqual(
            result,
            HoldSet({1, 2, 4}),
        )

    # issubset
    def test_issubset(self: Self) -> None:
        self.assertTrue(HoldSet({1, 2}).issubset(HoldSet({1, 2, 3})))

    # issuperset
    def test_issuperset(self: Self) -> None:
        self.assertTrue(HoldSet({1, 2, 3}).issuperset(HoldSet({1, 2})))

    # isdisjoint
    def test_isdisjoint(self: Self) -> None:
        self.assertTrue(HoldSet({1, 2}).isdisjoint(HoldSet({3, 4})))

        self.assertFalse(HoldSet({1, 2}).isdisjoint(HoldSet({2, 3})))

    # copy
    def test_copy(self: Self) -> None:
        result: Any = self.obj.copy()

        self.assertIsInstance(result, HoldSet)
        self.assertEqual(result, self.obj)
        self.assertIsNot(result, self.obj)

    # reverse operators
    def test_reverse_operators(self: Self) -> None:
        self.assertEqual(
            {1, 2} | HoldSet({2, 3}),
            HoldSet({1, 2, 3}),
        )

        self.assertEqual(
            {1, 2} & HoldSet({2, 3}),
            HoldSet({2}),
        )

        self.assertEqual(
            {1, 2} - HoldSet({2}),
            HoldSet({1}),
        )

        self.assertEqual(
            {1, 2} ^ HoldSet({2, 3}),
            HoldSet({1, 3}),
        )


if __name__ == "__main__":
    unittest.main()
