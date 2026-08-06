__all__: list[str] = [
    "TestMethodDifference",
    "TestMethodIntersection",
    "TestMethodIsDisjoint",
    "TestMethodIsSubset",
    "TestMethodIsSuperset",
    "TestMethodSymmetricDifference",
    "TestMethodUnion",
    "TestOperatorDifference",
    "TestOperatorEquality",
    "TestOperatorInequality",
    "TestOperatorIntersection",
    "TestOperatorMembership",
    "TestOperatorNonMembership",
    "TestOperatorProperSubset",
    "TestOperatorProperSuperset",
    "TestOperatorSubset",
    "TestOperatorSuperset",
    "TestOperatorSymmetricDifference",
    "TestOperatorUnion",
]

import unittest
from typing import Self

from datahold import FrozenSetSlot


class TestOperatorUnion(unittest.TestCase):
    def test_union_with_overlap(self: Self, /) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2, 3}) | FrozenSetSlot({3, 4}),
            frozenset({1, 2, 3, 4}),
        )

    def test_union_with_disjoint_sets(self: Self, /) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2}) | FrozenSetSlot({3, 4}),
            frozenset({1, 2, 3, 4}),
        )

    def test_union_with_empty_set(self: Self, /) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2}) | FrozenSetSlot(),
            frozenset({1, 2}),
        )

    def test_union_with_builtin_frozenset(self: Self, /) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2}) | frozenset({2, 3}),
            frozenset({1, 2, 3}),
        )


class TestOperatorIntersection(unittest.TestCase):
    def test_intersection_with_overlap(self: Self, /) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2, 3}) & FrozenSetSlot({2, 3, 4}),
            frozenset({2, 3}),
        )

    def test_intersection_with_disjoint_sets(self: Self, /) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2}) & FrozenSetSlot({3, 4}),
            frozenset(),
        )

    def test_intersection_with_empty_set(self: Self, /) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2}) & FrozenSetSlot(),
            frozenset(),
        )

    def test_intersection_with_builtin_set(self: Self, /) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2, 3}) & {2, 3, 4},
            frozenset({2, 3}),
        )


class TestOperatorDifference(unittest.TestCase):
    def test_difference_with_overlap(self: Self, /) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2, 3}) - FrozenSetSlot({2, 3, 4}),
            frozenset({1}),
        )

    def test_difference_with_disjoint_sets(self: Self, /) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2}) - FrozenSetSlot({3, 4}),
            frozenset({1, 2}),
        )

    def test_difference_with_identical_sets(self: Self, /) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2}) - FrozenSetSlot({1, 2}),
            frozenset(),
        )

    def test_difference_with_empty_set(self: Self, /) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2}) - FrozenSetSlot(),
            frozenset({1, 2}),
        )


class TestOperatorSymmetricDifference(unittest.TestCase):
    def test_symmetric_difference_with_overlap(self: Self, /) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2, 3}) ^ FrozenSetSlot({3, 4}),
            frozenset({1, 2, 4}),
        )

    def test_symmetric_difference_with_disjoint_sets(self: Self, /) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2}) ^ FrozenSetSlot({3, 4}),
            frozenset({1, 2, 3, 4}),
        )

    def test_symmetric_difference_with_identical_sets(self: Self, /) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2}) ^ FrozenSetSlot({1, 2}),
            frozenset(),
        )

    def test_symmetric_difference_with_empty_set(self: Self, /) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2}) ^ FrozenSetSlot(),
            frozenset({1, 2}),
        )


class TestOperatorSubset(unittest.TestCase):
    def test_equal_sets_are_subsets(self: Self, /) -> None:
        self.assertTrue(FrozenSetSlot({1, 2}) <= FrozenSetSlot({1, 2}))

    def test_proper_subset_is_subset(self: Self, /) -> None:
        self.assertTrue(FrozenSetSlot({1, 2}) <= FrozenSetSlot({1, 2, 3}))

    def test_larger_set_is_not_subset(self: Self, /) -> None:
        self.assertFalse(FrozenSetSlot({1, 2, 3}) <= FrozenSetSlot({1, 2}))

    def test_empty_set_is_subset(self: Self, /) -> None:
        self.assertTrue(FrozenSetSlot() <= FrozenSetSlot({1}))


class TestOperatorProperSubset(unittest.TestCase):
    def test_proper_subset(self: Self, /) -> None:
        self.assertTrue(FrozenSetSlot({1, 2}) < FrozenSetSlot({1, 2, 3}))

    def test_equal_sets_are_not_proper_subsets(self: Self, /) -> None:
        self.assertFalse(FrozenSetSlot({1, 2}) < FrozenSetSlot({1, 2}))

    def test_larger_set_is_not_proper_subset(self: Self, /) -> None:
        self.assertFalse(FrozenSetSlot({1, 2, 3}) < FrozenSetSlot({1, 2}))

    def test_empty_set_is_proper_subset_of_nonempty_set(self: Self, /) -> None:
        self.assertTrue(FrozenSetSlot() < FrozenSetSlot({1}))


class TestOperatorSuperset(unittest.TestCase):
    def test_equal_sets_are_supersets(self: Self, /) -> None:
        self.assertTrue(FrozenSetSlot({1, 2}) >= FrozenSetSlot({1, 2}))

    def test_larger_set_is_superset(self: Self, /) -> None:
        self.assertTrue(FrozenSetSlot({1, 2, 3}) >= FrozenSetSlot({1, 2}))

    def test_smaller_set_is_not_superset(self: Self, /) -> None:
        self.assertFalse(FrozenSetSlot({1, 2}) >= FrozenSetSlot({1, 2, 3}))

    def test_every_set_is_superset_of_empty_set(self: Self, /) -> None:
        self.assertTrue(FrozenSetSlot({1}) >= FrozenSetSlot())


class TestOperatorProperSuperset(unittest.TestCase):
    def test_proper_superset(self: Self, /) -> None:
        self.assertTrue(FrozenSetSlot({1, 2, 3}) > FrozenSetSlot({1, 2}))

    def test_equal_sets_are_not_proper_supersets(self: Self, /) -> None:
        self.assertFalse(FrozenSetSlot({1, 2}) > FrozenSetSlot({1, 2}))

    def test_smaller_set_is_not_proper_superset(self: Self, /) -> None:
        self.assertFalse(FrozenSetSlot({1, 2}) > FrozenSetSlot({1, 2, 3}))

    def test_nonempty_set_is_proper_superset_of_empty_set(
        self: Self, /
    ) -> None:
        self.assertTrue(FrozenSetSlot({1}) > FrozenSetSlot())


class TestOperatorEquality(unittest.TestCase):
    def test_equal_instances(self: Self, /) -> None:
        self.assertTrue(FrozenSetSlot({1, 2, 3}) == FrozenSetSlot({3, 2, 1}))

    def test_equal_to_builtin_frozenset(self: Self, /) -> None:
        self.assertTrue(FrozenSetSlot({1, 2}) == frozenset({1, 2}))  # type: ignore[comparison-overlap]

    def test_equal_to_builtin_set(self: Self, /) -> None:
        self.assertTrue(FrozenSetSlot({1, 2}) == {1, 2})  # type: ignore[comparison-overlap]

    def test_unequal_values(self: Self, /) -> None:
        self.assertFalse(FrozenSetSlot({1, 2}) == FrozenSetSlot({1, 3}))

    def test_not_equal_to_non_set_object(self: Self, /) -> None:
        self.assertFalse(FrozenSetSlot({1, 2}) == [1, 2])  # type: ignore[comparison-overlap]


class TestOperatorInequality(unittest.TestCase):
    def test_different_instances_are_unequal(self: Self, /) -> None:
        self.assertTrue(FrozenSetSlot({1, 2}) != FrozenSetSlot({1, 3}))

    def test_equal_instances_are_not_unequal(self: Self, /) -> None:
        self.assertFalse(FrozenSetSlot({1, 2}) != FrozenSetSlot({2, 1}))

    def test_equal_builtin_frozenset_is_not_unequal(self: Self, /) -> None:
        self.assertFalse(FrozenSetSlot({1, 2}) != frozenset({1, 2}))  # type: ignore[comparison-overlap]

    def test_different_builtin_set_is_unequal(self: Self, /) -> None:
        self.assertTrue(FrozenSetSlot({1, 2}) != {1, 2, 3})  # type: ignore[comparison-overlap]

    def test_non_set_object_is_unequal(self: Self, /) -> None:
        self.assertTrue(FrozenSetSlot({1, 2}) != [1, 2])  # type: ignore[comparison-overlap]


class TestOperatorMembership(unittest.TestCase):
    def test_existing_element_is_member(self: Self, /) -> None:
        self.assertTrue(2 in FrozenSetSlot({1, 2, 3}))

    def test_missing_element_is_not_member(self: Self, /) -> None:
        self.assertFalse(4 in FrozenSetSlot({1, 2, 3}))

    def test_nested_frozenset_is_member(self: Self, /) -> None:
        nested = frozenset({1, 2})
        self.assertTrue(nested in FrozenSetSlot({nested, frozenset({3})}))

    def test_equivalent_set_matches_nested_frozenset(self: Self, /) -> None:
        self.assertTrue({1, 2} in FrozenSetSlot({frozenset({1, 2})}))


class TestOperatorNonMembership(unittest.TestCase):
    def test_missing_element_is_not_member(self: Self, /) -> None:
        self.assertTrue(4 not in FrozenSetSlot({1, 2, 3}))

    def test_existing_element_is_member(self: Self, /) -> None:
        self.assertFalse(2 not in FrozenSetSlot({1, 2, 3}))

    def test_missing_nested_frozenset_is_not_member(self: Self, /) -> None:
        self.assertTrue(
            frozenset({3, 4}) not in FrozenSetSlot({frozenset({1, 2})})
        )

    def test_equivalent_set_is_considered_a_member(self: Self, /) -> None:
        self.assertFalse({1, 2} not in FrozenSetSlot({frozenset({1, 2})}))


class TestMethodDifference(unittest.TestCase):
    def test_difference_with_overlapping_values(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2, 3}).difference({2, 3, 4})

        self.assertEqual(result, frozenset({1}))

    def test_difference_with_disjoint_values(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2}).difference({3, 4})

        self.assertEqual(result, frozenset({1, 2}))

    def test_difference_with_multiple_iterables(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2, 3, 4, 5}).difference(
            {2, 3},
            [4],
            (5, 6),
        )

        self.assertEqual(result, frozenset({1}))

    def test_difference_without_arguments(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2}).difference()

        self.assertEqual(result, frozenset({1, 2}))

    def test_difference_returns_frozen_set_slot(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2, 3}).difference({3})

        self.assertIsInstance(result, FrozenSetSlot)

    def test_difference_rejects_non_iterable(self: Self, /) -> None:
        with self.assertRaises(TypeError):
            FrozenSetSlot({1, 2}).difference(3)  # type: ignore[arg-type]


class TestMethodIntersection(unittest.TestCase):
    def test_intersection_with_overlapping_values(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2, 3}).intersection({2, 3, 4})

        self.assertEqual(result, frozenset({2, 3}))

    def test_intersection_with_disjoint_values(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2}).intersection({3, 4})

        self.assertEqual(result, frozenset())

    def test_intersection_with_multiple_iterables(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2, 3, 4}).intersection(
            [2, 3, 4, 5],
            (3, 4, 6),
        )

        self.assertEqual(result, frozenset({3, 4}))

    def test_intersection_without_arguments(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2}).intersection()

        self.assertEqual(result, frozenset({1, 2}))

    def test_intersection_returns_frozen_set_slot(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2, 3}).intersection({2, 3})

        self.assertIsInstance(result, FrozenSetSlot)

    def test_intersection_accepts_generator(self: Self, /) -> None:
        values = (value for value in range(2, 5))
        result = FrozenSetSlot({1, 2, 3}).intersection(values)

        self.assertEqual(result, frozenset({2, 3}))


class TestMethodIsDisjoint(unittest.TestCase):
    def test_disjoint_iterables(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2}).isdisjoint({3, 4})

        self.assertTrue(result)

    def test_overlapping_iterables(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2, 3}).isdisjoint({3, 4})

        self.assertFalse(result)

    def test_empty_instance_is_disjoint(self: Self, /) -> None:
        result = FrozenSetSlot().isdisjoint({1, 2})

        self.assertTrue(result)

    def test_is_disjoint_with_empty_iterable(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2}).isdisjoint([])

        self.assertTrue(result)

    def test_is_disjoint_accepts_generator(self: Self, /) -> None:
        values = (value for value in range(3, 6))
        result = FrozenSetSlot({1, 2, 3}).isdisjoint(values)

        self.assertFalse(result)

    def test_is_disjoint_rejects_non_iterable(self: Self, /) -> None:
        with self.assertRaises(TypeError):
            FrozenSetSlot({1, 2}).isdisjoint(3)  # type: ignore[arg-type]


class TestMethodIsSubset(unittest.TestCase):
    def test_proper_subset(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2}).issubset({1, 2, 3})

        self.assertTrue(result)

    def test_equal_set_is_subset(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2}).issubset([2, 1])

        self.assertTrue(result)

    def test_non_subset(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2, 4}).issubset({1, 2, 3})

        self.assertFalse(result)

    def test_empty_instance_is_subset(self: Self, /) -> None:
        result = FrozenSetSlot().issubset({1, 2})

        self.assertTrue(result)

    def test_nonempty_instance_is_not_subset_of_empty_iterable(
        self: Self,
    ) -> None:
        result = FrozenSetSlot({1}).issubset([])

        self.assertFalse(result)

    def test_is_subset_accepts_generator(self: Self, /) -> None:
        values = (value for value in range(1, 4))
        result = FrozenSetSlot({1, 2}).issubset(values)

        self.assertTrue(result)


class TestMethodIsSuperset(unittest.TestCase):
    def test_proper_superset(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2, 3}).issuperset({1, 2})

        self.assertTrue(result)

    def test_equal_set_is_superset(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2}).issuperset([2, 1])

        self.assertTrue(result)

    def test_non_superset(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2}).issuperset({1, 2, 3})

        self.assertFalse(result)

    def test_every_instance_is_superset_of_empty_iterable(
        self: Self, /
    ) -> None:
        result = FrozenSetSlot({1, 2}).issuperset([])

        self.assertTrue(result)

    def test_empty_instance_is_not_superset_of_nonempty_iterable(
        self: Self,
    ) -> None:
        result = FrozenSetSlot().issuperset({1})

        self.assertFalse(result)

    def test_is_superset_accepts_generator(self: Self, /) -> None:
        values = (value for value in range(1, 3))
        result = FrozenSetSlot({1, 2, 3}).issuperset(values)

        self.assertTrue(result)


class TestMethodSymmetricDifference(unittest.TestCase):
    def test_symmetric_difference_with_overlap(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2, 3}).symmetric_difference({3, 4})

        self.assertEqual(result, frozenset({1, 2, 4}))

    def test_symmetric_difference_with_disjoint_values(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2}).symmetric_difference([3, 4])

        self.assertEqual(result, frozenset({1, 2, 3, 4}))

    def test_symmetric_difference_with_equal_values(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2}).symmetric_difference((2, 1))

        self.assertEqual(result, frozenset())

    def test_symmetric_difference_with_empty_iterable(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2}).symmetric_difference([])

        self.assertEqual(result, frozenset({1, 2}))

    def test_symmetric_difference_returns_frozen_set_slot(
        self: Self, /
    ) -> None:
        result = FrozenSetSlot({1, 2}).symmetric_difference({2, 3})

        self.assertIsInstance(result, FrozenSetSlot)

    def test_symmetric_difference_rejects_multiple_arguments(
        self: Self,
    ) -> None:
        with self.assertRaises(TypeError):
            FrozenSetSlot({1, 2}).symmetric_difference({2}, {3})  # type: ignore[call-arg]


class TestMethodUnion(unittest.TestCase):
    def test_union_with_overlapping_values(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2, 3}).union({3, 4})

        self.assertEqual(result, frozenset({1, 2, 3, 4}))

    def test_union_with_disjoint_values(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2}).union([3, 4])

        self.assertEqual(result, frozenset({1, 2, 3, 4}))

    def test_union_with_multiple_iterables(self: Self, /) -> None:
        result = FrozenSetSlot({1}).union(
            [2, 3],
            (3, 4),
            frozenset({5}),
        )

        self.assertEqual(result, frozenset({1, 2, 3, 4, 5}))

    def test_union_without_arguments(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2}).union()

        self.assertEqual(result, frozenset({1, 2}))

    def test_union_returns_frozen_set_slot(self: Self, /) -> None:
        result = FrozenSetSlot({1, 2}).union({3})

        self.assertIsInstance(result, FrozenSetSlot)

    def test_union_accepts_generator(self: Self, /) -> None:
        values = (value for value in range(2, 5))
        result = FrozenSetSlot({1, 2}).union(values)

        self.assertEqual(result, frozenset({1, 2, 3, 4}))


if __name__ == "__main__":
    unittest.main()
