__all__: list[str] = ["TestFrozenHoldSet"]
import unittest
from typing import Self

from datahold.frozen.FrozenHoldSet import FrozenHoldSet


class TestFrozenHoldSet(unittest.TestCase):

    def setUp(self: Self) -> None:
        self.obj = FrozenHoldSet({1, 2, 3})
        self.same = FrozenHoldSet({1, 2, 3})
        self.other = FrozenHoldSet({3, 4, 5})

    # __init__
    def test_init(self: Self) -> None:
        obj = FrozenHoldSet([1, 2, 3])
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
        self.assertTrue(FrozenHoldSet({1, 2}) < FrozenHoldSet({1, 2, 3}))

    # __le__
    def test_le(self: Self) -> None:
        self.assertTrue(FrozenHoldSet({1, 2}) <= FrozenHoldSet({1, 2, 3}))
        self.assertTrue(FrozenHoldSet({1, 2}) <= FrozenHoldSet({1, 2}))

    # __gt__
    def test_gt(self: Self) -> None:
        self.assertTrue(FrozenHoldSet({1, 2, 3}) > FrozenHoldSet({1, 2}))

    # __ge__
    def test_ge(self: Self) -> None:
        self.assertTrue(FrozenHoldSet({1, 2, 3}) >= FrozenHoldSet({1, 2}))
        self.assertTrue(FrozenHoldSet({1, 2}) >= FrozenHoldSet({1, 2}))

    # __hash__
    def test_hash(self: Self) -> None:
        self.assertEqual(hash(self.obj), hash(self.same))
        self.assertEqual(hash(self.obj), hash(self.obj.__fget__()))

    # __or__
    def test_or(self: Self) -> None:
        result = FrozenHoldSet({1, 2}) | FrozenHoldSet({2, 3})

        self.assertIsInstance(result, FrozenHoldSet)
        self.assertEqual(
            result,
            FrozenHoldSet({1, 2, 3}),
        )

    # __repr__
    def test_repr(self: Self) -> None:
        self.assertEqual(
            repr(FrozenHoldSet({1, 2, 3})),
            "FrozenHoldSet({1, 2, 3})",
        )

    # union
    def test_union(self: Self) -> None:
        result = self.obj.union({4, 5})

        self.assertIsInstance(result, FrozenHoldSet)
        self.assertEqual(
            result,
            FrozenHoldSet({1, 2, 3, 4, 5}),
        )

    # intersection
    def test_intersection(self: Self) -> None:
        result = self.obj.intersection({2, 3, 4})

        self.assertEqual(
            result,
            FrozenHoldSet({2, 3}),
        )

    # difference
    def test_difference(self: Self) -> None:
        result = self.obj.difference({2})

        self.assertEqual(
            result,
            FrozenHoldSet({1, 3}),
        )

    # symmetric_difference
    def test_symmetric_difference(self: Self) -> None:
        result = self.obj.symmetric_difference({3, 4})

        self.assertEqual(
            result,
            FrozenHoldSet({1, 2, 4}),
        )

    # issubset
    def test_issubset(self: Self) -> None:
        self.assertTrue(
            FrozenHoldSet({1, 2}).issubset(FrozenHoldSet({1, 2, 3}))
        )

    # issuperset
    def test_issuperset(self: Self) -> None:
        self.assertTrue(
            FrozenHoldSet({1, 2, 3}).issuperset(FrozenHoldSet({1, 2}))
        )

    # isdisjoint
    def test_isdisjoint(self: Self) -> None:
        self.assertTrue(
            FrozenHoldSet({1, 2}).isdisjoint(FrozenHoldSet({3, 4}))
        )
        self.assertFalse(
            FrozenHoldSet({1, 2}).isdisjoint(FrozenHoldSet({2, 3}))
        )

    # __and__
    def test_and(self: Self) -> None:
        result = FrozenHoldSet({1, 2, 3}) & FrozenHoldSet({2, 3, 4})

        self.assertEqual(
            result,
            FrozenHoldSet({2, 3}),
        )

    # __sub__
    def test_sub(self: Self) -> None:
        result = FrozenHoldSet({1, 2, 3}) - FrozenHoldSet({2})

        self.assertEqual(
            result,
            FrozenHoldSet({1, 3}),
        )

    # __xor__
    def test_xor(self: Self) -> None:
        result = FrozenHoldSet({1, 2, 3}) ^ FrozenHoldSet({3, 4})

        self.assertEqual(
            result,
            FrozenHoldSet({1, 2, 4}),
        )

    # reverse operators
    def test_reverse_operators(self: Self) -> None:
        self.assertEqual(
            {1, 2} | FrozenHoldSet({2, 3}),
            FrozenHoldSet({1, 2, 3}),
        )

        self.assertEqual(
            {1, 2} & FrozenHoldSet({2, 3}),
            FrozenHoldSet({2}),
        )

        self.assertEqual(
            {1, 2} - FrozenHoldSet({2}),
            FrozenHoldSet({1}),
        )

        self.assertEqual(
            {1, 2} ^ FrozenHoldSet({2, 3}),
            FrozenHoldSet({1, 3}),
        )


if __name__ == "__main__":
    unittest.main()
