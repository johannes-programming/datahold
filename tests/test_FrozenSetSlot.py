import unittest
from typing import Self

from datahold import FrozenSetSlot


class TestUnionOperator(unittest.TestCase):
    def test_union_with_overlap(self: Self) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2, 3}) | FrozenSetSlot({3, 4}),
            frozenset({1, 2, 3, 4}),
        )

    def test_union_with_disjoint_sets(self: Self) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2}) | FrozenSetSlot({3, 4}),
            frozenset({1, 2, 3, 4}),
        )

    def test_union_with_empty_set(self: Self) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2}) | FrozenSetSlot(),
            frozenset({1, 2}),
        )

    def test_union_with_builtin_frozenset(self: Self) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2}) | frozenset({2, 3}),
            frozenset({1, 2, 3}),
        )


class TestIntersectionOperator(unittest.TestCase):
    def test_intersection_with_overlap(self: Self) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2, 3}) & FrozenSetSlot({2, 3, 4}),
            frozenset({2, 3}),
        )

    def test_intersection_with_disjoint_sets(self: Self) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2}) & FrozenSetSlot({3, 4}),
            frozenset(),
        )

    def test_intersection_with_empty_set(self: Self) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2}) & FrozenSetSlot(),
            frozenset(),
        )

    def test_intersection_with_builtin_set(self: Self) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2, 3}) & {2, 3, 4},
            frozenset({2, 3}),
        )


class TestDifferenceOperator(unittest.TestCase):
    def test_difference_with_overlap(self: Self) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2, 3}) - FrozenSetSlot({2, 3, 4}),
            frozenset({1}),
        )

    def test_difference_with_disjoint_sets(self: Self) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2}) - FrozenSetSlot({3, 4}),
            frozenset({1, 2}),
        )

    def test_difference_with_identical_sets(self: Self) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2}) - FrozenSetSlot({1, 2}),
            frozenset(),
        )

    def test_difference_with_empty_set(self: Self) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2}) - FrozenSetSlot(),
            frozenset({1, 2}),
        )


class TestSymmetricDifferenceOperator(unittest.TestCase):
    def test_symmetric_difference_with_overlap(self: Self) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2, 3}) ^ FrozenSetSlot({3, 4}),
            frozenset({1, 2, 4}),
        )

    def test_symmetric_difference_with_disjoint_sets(self: Self) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2}) ^ FrozenSetSlot({3, 4}),
            frozenset({1, 2, 3, 4}),
        )

    def test_symmetric_difference_with_identical_sets(self: Self) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2}) ^ FrozenSetSlot({1, 2}),
            frozenset(),
        )

    def test_symmetric_difference_with_empty_set(self: Self) -> None:
        self.assertEqual(
            FrozenSetSlot({1, 2}) ^ FrozenSetSlot(),
            frozenset({1, 2}),
        )


class TestSubsetOperator(unittest.TestCase):
    def test_equal_sets_are_subsets(self: Self) -> None:
        self.assertTrue(FrozenSetSlot({1, 2}) <= FrozenSetSlot({1, 2}))

    def test_proper_subset_is_subset(self: Self) -> None:
        self.assertTrue(FrozenSetSlot({1, 2}) <= FrozenSetSlot({1, 2, 3}))

    def test_larger_set_is_not_subset(self: Self) -> None:
        self.assertFalse(FrozenSetSlot({1, 2, 3}) <= FrozenSetSlot({1, 2}))

    def test_empty_set_is_subset(self: Self) -> None:
        self.assertTrue(FrozenSetSlot() <= FrozenSetSlot({1}))


class TestProperSubsetOperator(unittest.TestCase):
    def test_proper_subset(self: Self) -> None:
        self.assertTrue(FrozenSetSlot({1, 2}) < FrozenSetSlot({1, 2, 3}))

    def test_equal_sets_are_not_proper_subsets(self: Self) -> None:
        self.assertFalse(FrozenSetSlot({1, 2}) < FrozenSetSlot({1, 2}))

    def test_larger_set_is_not_proper_subset(self: Self) -> None:
        self.assertFalse(FrozenSetSlot({1, 2, 3}) < FrozenSetSlot({1, 2}))

    def test_empty_set_is_proper_subset_of_nonempty_set(self: Self) -> None:
        self.assertTrue(FrozenSetSlot() < FrozenSetSlot({1}))


class TestSupersetOperator(unittest.TestCase):
    def test_equal_sets_are_supersets(self: Self) -> None:
        self.assertTrue(FrozenSetSlot({1, 2}) >= FrozenSetSlot({1, 2}))

    def test_larger_set_is_superset(self: Self) -> None:
        self.assertTrue(FrozenSetSlot({1, 2, 3}) >= FrozenSetSlot({1, 2}))

    def test_smaller_set_is_not_superset(self: Self) -> None:
        self.assertFalse(FrozenSetSlot({1, 2}) >= FrozenSetSlot({1, 2, 3}))

    def test_every_set_is_superset_of_empty_set(self: Self) -> None:
        self.assertTrue(FrozenSetSlot({1}) >= FrozenSetSlot())


class TestProperSupersetOperator(unittest.TestCase):
    def test_proper_superset(self: Self) -> None:
        self.assertTrue(FrozenSetSlot({1, 2, 3}) > FrozenSetSlot({1, 2}))

    def test_equal_sets_are_not_proper_supersets(self: Self) -> None:
        self.assertFalse(FrozenSetSlot({1, 2}) > FrozenSetSlot({1, 2}))

    def test_smaller_set_is_not_proper_superset(self: Self) -> None:
        self.assertFalse(FrozenSetSlot({1, 2}) > FrozenSetSlot({1, 2, 3}))

    def test_nonempty_set_is_proper_superset_of_empty_set(self: Self) -> None:
        self.assertTrue(FrozenSetSlot({1}) > FrozenSetSlot())


class TestEqualityOperator(unittest.TestCase):
    def test_equal_instances(self: Self) -> None:
        self.assertTrue(FrozenSetSlot({1, 2, 3}) == FrozenSetSlot({3, 2, 1}))

    def test_equal_to_builtin_frozenset(self: Self) -> None:
        self.assertTrue(FrozenSetSlot({1, 2}) == frozenset({1, 2}))  # type: ignore[comparison-overlap]

    def test_equal_to_builtin_set(self: Self) -> None:
        self.assertTrue(FrozenSetSlot({1, 2}) == {1, 2})  # type: ignore[comparison-overlap]

    def test_unequal_values(self: Self) -> None:
        self.assertFalse(FrozenSetSlot({1, 2}) == FrozenSetSlot({1, 3}))

    def test_not_equal_to_non_set_object(self: Self) -> None:
        self.assertFalse(FrozenSetSlot({1, 2}) == [1, 2])  # type: ignore[comparison-overlap]


class TestInequalityOperator(unittest.TestCase):
    def test_different_instances_are_unequal(self: Self) -> None:
        self.assertTrue(FrozenSetSlot({1, 2}) != FrozenSetSlot({1, 3}))

    def test_equal_instances_are_not_unequal(self: Self) -> None:
        self.assertFalse(FrozenSetSlot({1, 2}) != FrozenSetSlot({2, 1}))

    def test_equal_builtin_frozenset_is_not_unequal(self: Self) -> None:
        self.assertFalse(FrozenSetSlot({1, 2}) != frozenset({1, 2}))  # type: ignore[comparison-overlap]

    def test_different_builtin_set_is_unequal(self: Self) -> None:
        self.assertTrue(FrozenSetSlot({1, 2}) != {1, 2, 3})  # type: ignore[comparison-overlap]

    def test_non_set_object_is_unequal(self: Self) -> None:
        self.assertTrue(FrozenSetSlot({1, 2}) != [1, 2])  # type: ignore[comparison-overlap]


class TestMembershipOperator(unittest.TestCase):
    def test_existing_element_is_member(self: Self) -> None:
        self.assertTrue(2 in FrozenSetSlot({1, 2, 3}))

    def test_missing_element_is_not_member(self: Self) -> None:
        self.assertFalse(4 in FrozenSetSlot({1, 2, 3}))

    def test_nested_frozenset_is_member(self: Self) -> None:
        nested = frozenset({1, 2})
        self.assertTrue(nested in FrozenSetSlot({nested, frozenset({3})}))

    def test_equivalent_set_matches_nested_frozenset(self: Self) -> None:
        self.assertTrue({1, 2} in FrozenSetSlot({frozenset({1, 2})}))


class TestNonMembershipOperator(unittest.TestCase):
    def test_missing_element_is_not_member(self: Self) -> None:
        self.assertTrue(4 not in FrozenSetSlot({1, 2, 3}))

    def test_existing_element_is_member(self: Self) -> None:
        self.assertFalse(2 not in FrozenSetSlot({1, 2, 3}))

    def test_missing_nested_frozenset_is_not_member(self: Self) -> None:
        self.assertTrue(
            frozenset({3, 4}) not in FrozenSetSlot({frozenset({1, 2})})
        )

    def test_equivalent_set_is_considered_a_member(self: Self) -> None:
        self.assertFalse({1, 2} not in FrozenSetSlot({frozenset({1, 2})}))


if __name__ == "__main__":
    unittest.main()
