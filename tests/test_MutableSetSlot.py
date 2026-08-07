__all__: list[str] = [
    "TestMethodAdd",
    "TestMethodClear",
    "TestMethodCopy",
    "TestMethodDifference",
    "TestMethodDifferenceUpdate",
    "TestMethodDiscard",
    "TestMethodIntersection",
    "TestMethodIntersectionUpdate",
    "TestMethodIsDisjoint",
    "TestMethodIsSubset",
    "TestMethodIsSuperset",
    "TestMethodPop",
    "TestMethodRemove",
    "TestMethodSymmetricDifference",
    "TestMethodSymmetricDifferenceUpdate",
    "TestMethodUnion",
    "TestMethodUpdate",
    "TestOperatorAnd",
    "TestOperatorContains",
    "TestOperatorEquality",
    "TestOperatorGreaterThan",
    "TestOperatorGreaterThanOrEqual",
    "TestOperatorInPlaceAnd",
    "TestOperatorInPlaceOr",
    "TestOperatorInPlaceSubtract",
    "TestOperatorInPlaceXor",
    "TestOperatorLessThan",
    "TestOperatorLessThanOrEqual",
    "TestOperatorNotContains",
    "TestOperatorNotEqual",
    "TestOperatorOr",
    "TestOperatorSubtract",
    "TestOperatorXor",
]


import unittest
from typing import Any, Never, Self

from datahold import MutableSetSlot


class TestMethodAdd(unittest.TestCase):
    def test_adds_new_element(self: Self, /) -> None:
        value: MutableSetSlot[int]
        value = MutableSetSlot({1, 2})
        value.add(3)
        self.assertEqual(set(value), {1, 2, 3})

    def test_adding_duplicate_does_not_change_set(self: Self, /) -> None:
        value: MutableSetSlot[int]
        value = MutableSetSlot({1, 2})
        value.add(2)
        self.assertEqual(set(value), {1, 2})

    def test_adds_hashable_tuple(self: Self, /) -> None:
        value: MutableSetSlot[tuple[int, int]]
        value = MutableSetSlot()
        value.add((1, 2))
        self.assertEqual(set(value), {(1, 2)})

    def test_adding_unhashable_element_raises_type_error(
        self: Self, /
    ) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1})
        with self.assertRaises(TypeError):
            value.add([2])
        self.assertEqual(set(value), {1})


class TestMethodClear(unittest.TestCase):
    def test_clears_populated_set(self: Self, /) -> None:
        value: MutableSetSlot[int]
        value = MutableSetSlot({1, 2, 3})
        value.clear()
        self.assertEqual(set(value), set())

    def test_clearing_empty_set_keeps_it_empty(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot()
        value.clear()
        self.assertEqual(set(value), set())

    def test_clear_returns_none(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        self.assertIsNone(value.clear())  # type: ignore[func-returns-value]

    def test_set_can_be_reused_after_clear(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        value.clear()
        value.add(3)
        self.assertEqual(set(value), {3})


class TestMethodCopy(unittest.TestCase):
    def test_copy_has_same_contents(self: Self, /) -> None:
        copied: MutableSetSlot[Any]
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        copied = value.copy()
        self.assertEqual(set(copied), {1, 2, 3})

    def test_copy_is_a_different_object(self: Self, /) -> None:
        copied: MutableSetSlot[Any]
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        copied = value.copy()
        self.assertIsNot(copied, value)

    def test_copy_is_independent_of_original(self: Self, /) -> None:
        copied: MutableSetSlot[Any]
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        copied = value.copy()
        copied.add(3)
        self.assertEqual(set(value), {1, 2})
        self.assertEqual(set(copied), {1, 2, 3})

    def test_copy_of_empty_set_is_empty(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot()
        copied = value.copy()
        self.assertEqual(set(copied), set())


class TestMethodDifference(unittest.TestCase):
    def test_difference_removes_shared_elements(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        result = value.difference({2, 3, 4})
        self.assertEqual(set(result), {1})

    def test_difference_accepts_multiple_iterables(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3, 4})
        result = value.difference({1}, [2, 5])
        self.assertEqual(set(result), {3, 4})

    def test_difference_with_disjoint_set_is_unchanged(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        result = value.difference({3, 4})
        self.assertEqual(set(result), {1, 2})

    def test_difference_does_not_modify_original(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        value.difference({2})
        self.assertEqual(set(value), {1, 2, 3})


class TestMethodDifferenceUpdate(unittest.TestCase):
    def test_difference_update_removes_shared_elements(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        value.difference_update({2, 4})
        self.assertEqual(set(value), {1, 3})

    def test_difference_update_accepts_multiple_iterables(
        self: Self, /
    ) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3, 4})
        value.difference_update({1}, [2, 5])
        self.assertEqual(set(value), {3, 4})

    def test_difference_update_with_disjoint_set_is_unchanged(
        self: Self,
    ) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        value.difference_update({3, 4})
        self.assertEqual(set(value), {1, 2})

    def test_difference_update_with_self_empties_set(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        value.difference_update(value)
        self.assertEqual(set(value), set())


class TestMethodDiscard(unittest.TestCase):
    def test_discards_existing_element(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        value.discard(2)
        self.assertEqual(set(value), {1, 3})

    def test_discarding_missing_element_does_not_raise(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        value.discard(3)
        self.assertEqual(set(value), {1, 2})

    def test_discard_returns_none(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        self.assertIsNone(value.discard(1))

    def test_discarding_unhashable_element_raises_type_error(
        self: Self,
    ) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        with self.assertRaises(TypeError):
            value.discard([1])  # type: ignore
        self.assertEqual(set(value), {1, 2})


class TestMethodIntersection(unittest.TestCase):
    def test_intersection_returns_shared_elements(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        result = value.intersection({2, 3, 4})
        self.assertEqual(set(result), {2, 3})

    def test_intersection_accepts_multiple_iterables(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3, 4})
        result = value.intersection({2, 3, 4}, [3, 4, 5])
        self.assertEqual(set(result), {3, 4})

    def test_intersection_with_disjoint_set_is_empty(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        result = value.intersection({3, 4})
        self.assertEqual(set(result), set())

    def test_intersection_does_not_modify_original(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        value.intersection({2})
        self.assertEqual(set(value), {1, 2, 3})


class TestMethodIntersectionUpdate(unittest.TestCase):
    def test_intersection_update_keeps_shared_elements(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        value.intersection_update({2, 3, 4})
        self.assertEqual(set(value), {2, 3})

    def test_intersection_update_accepts_multiple_iterables(
        self: Self,
    ) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3, 4})
        value.intersection_update({2, 3, 4}, [3, 4, 5])
        self.assertEqual(set(value), {3, 4})

    def test_intersection_update_with_disjoint_set_empties_set(
        self: Self,
    ) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        value.intersection_update({3, 4})
        self.assertEqual(set(value), set())

    def test_intersection_update_with_self_is_unchanged(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        value.intersection_update(value)
        self.assertEqual(set(value), {1, 2, 3})


class TestMethodIsDisjoint(unittest.TestCase):
    def test_disjoint_sets_return_true(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        self.assertTrue(value.isdisjoint({3, 4}))

    def test_overlapping_sets_return_false(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        self.assertFalse(value.isdisjoint({2, 3}))

    def test_empty_set_is_disjoint_from_populated_set(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot()
        self.assertTrue(value.isdisjoint({1, 2}))

    def test_isdisjoint_accepts_generator(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        other = (number for number in (3, 4))
        self.assertTrue(value.isdisjoint(other))


class TestMethodIsSubset(unittest.TestCase):
    def test_proper_subset_returns_true(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        self.assertTrue(value.issubset({1, 2, 3}))

    def test_equal_set_is_subset(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        self.assertTrue(value.issubset({1, 2}))

    def test_non_subset_returns_false(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 4})
        self.assertFalse(value.issubset({1, 2, 3}))

    def test_empty_set_is_subset_of_any_set(self: Self, /) -> None:
        value: MutableSetSlot[Never]
        value = MutableSetSlot()
        self.assertTrue(value.issubset({1, 2}))


class TestMethodIsSuperset(unittest.TestCase):
    def test_proper_superset_returns_true(self: Self, /) -> None:
        value: MutableSetSlot[int]
        value = MutableSetSlot({1, 2, 3})
        self.assertTrue(value.issuperset({1, 2}))

    def test_equal_set_is_superset(self: Self, /) -> None:
        value: MutableSetSlot[int]
        value = MutableSetSlot({1, 2})
        self.assertTrue(value.issuperset({1, 2}))

    def test_non_superset_returns_false(self: Self, /) -> None:
        value: MutableSetSlot[int]
        value = MutableSetSlot({1, 2})
        self.assertFalse(value.issuperset({1, 3}))

    def test_every_set_is_superset_of_empty_set(self: Self, /) -> None:
        value: MutableSetSlot[int]
        value = MutableSetSlot({1, 2})
        self.assertTrue(value.issuperset(set()))


class TestMethodPop(unittest.TestCase):
    def test_pop_returns_and_removes_only_element(self: Self, /) -> None:
        result: int
        value: MutableSetSlot[int]
        value = MutableSetSlot({1})
        result = value.pop()
        self.assertEqual(result, 1)
        self.assertEqual(set(value), set())

    def test_pop_from_empty_set_raises_key_error(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot()
        with self.assertRaises(KeyError):
            value.pop()

    def test_pop_removes_one_element_from_populated_set(self: Self, /) -> None:
        original: set[int]
        result: int
        value: MutableSetSlot[int]
        original = {1, 2, 3}
        value = MutableSetSlot(original)
        result = value.pop()
        self.assertIn(result, original)
        self.assertEqual(set(value), original - {result})

    def test_repeated_pop_exhausts_set(self: Self, /) -> None:
        popped: set[int]
        value: MutableSetSlot[int]
        value = MutableSetSlot({1, 2, 3})
        popped = {value.pop(), value.pop(), value.pop()}
        self.assertEqual(popped, {1, 2, 3})
        self.assertEqual(set(value), set())


class TestMethodRemove(unittest.TestCase):
    def test_removes_existing_element(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        value.remove(2)
        self.assertEqual(set(value), {1, 3})

    def test_removing_missing_element_raises_key_error(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        with self.assertRaises(KeyError):
            value.remove(3)
        self.assertEqual(set(value), {1, 2})

    def test_remove_returns_none(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        self.assertIsNone(value.remove(1))  # type: ignore[func-returns-value]

    def test_removing_unhashable_element_raises_type_error(
        self: Self, /
    ) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        with self.assertRaises(Exception):
            # in general you should not rely upon
            # a TypeError or an AttributeError occuring
            value.remove([1])
        self.assertEqual(set(value), {1, 2})


class TestMethodSymmetricDifference(unittest.TestCase):
    def test_symmetric_difference_excludes_shared_elements(
        self: Self, /
    ) -> None:
        result: Any
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        result = value.symmetric_difference({3, 4, 5})
        self.assertEqual(set(result), {1, 2, 4, 5})

    def test_symmetric_difference_of_disjoint_sets_is_union(
        self: Self,
    ) -> None:
        result: Any
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        result = value.symmetric_difference({3, 4})
        self.assertEqual(set(result), {1, 2, 3, 4})

    def test_symmetric_difference_of_equal_sets_is_empty(
        self: Self, /
    ) -> None:
        result: Any
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        result = value.symmetric_difference({1, 2})
        self.assertEqual(set(result), set())

    def test_symmetric_difference_does_not_modify_original(
        self: Self, /
    ) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        value.symmetric_difference({3, 4})
        self.assertEqual(set(value), {1, 2, 3})


class TestMethodSymmetricDifferenceUpdate(unittest.TestCase):
    def test_symmetric_difference_update_excludes_shared_elements(
        self: Self,
    ) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        value.symmetric_difference_update({3, 4, 5})
        self.assertEqual(set(value), {1, 2, 4, 5})

    def test_symmetric_difference_update_of_disjoint_sets_is_union(
        self: Self,
    ) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        value.symmetric_difference_update({3, 4})
        self.assertEqual(set(value), {1, 2, 3, 4})

    def test_symmetric_difference_update_with_equal_set_empties_set(
        self: Self,
    ) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        value.symmetric_difference_update({1, 2})
        self.assertEqual(set(value), set())

    def test_symmetric_difference_update_returns_none(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        result = value.symmetric_difference_update({2, 3})
        self.assertIsNone(result)
        self.assertEqual(set(value), {1, 3})


class TestMethodUnion(unittest.TestCase):
    def test_union_combines_elements(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        result = value.union({2, 3})
        self.assertEqual(set(result), {1, 2, 3})

    def test_union_accepts_multiple_iterables(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1})
        result = value.union({2}, [3, 4])
        self.assertEqual(set(result), {1, 2, 3, 4})

    def test_union_without_arguments_returns_same_contents(
        self: Self, /
    ) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        result = value.union()
        self.assertEqual(set(result), {1, 2})
        self.assertIsNot(result, value)

    def test_union_does_not_modify_original(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        value.union({3, 4})
        self.assertEqual(set(value), {1, 2})


class TestMethodUpdate(unittest.TestCase):
    def test_update_adds_elements_from_iterable(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        value.update({2, 3, 4})
        self.assertEqual(set(value), {1, 2, 3, 4})

    def test_update_accepts_multiple_iterables(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1})
        value.update({2}, [3, 4])
        self.assertEqual(set(value), {1, 2, 3, 4})

    def test_update_ignores_duplicate_elements(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        value.update([1, 1, 2, 2])
        self.assertEqual(set(value), {1, 2})

    def test_update_returns_none(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1})
        result = value.update({2, 3})
        self.assertIsNone(result)
        self.assertEqual(set(value), {1, 2, 3})


class TestOperatorEquality(unittest.TestCase):

    # this TestCase really demonstrates how bugging mypy is
    # in regards to the equality and inequality operator:
    # every single test requires an ignore-comment...

    def test_equal_same_elements(self: Self, /) -> None:
        self.assertTrue(
            MutableSetSlot({1, 2, 3}) == {1, 2, 3}  # type: ignore[comparison-overlap]
        )

    def test_equal_different_order(self: Self, /) -> None:
        self.assertTrue(
            MutableSetSlot({1, 2, 3}) == {3, 2, 1}  # type: ignore[comparison-overlap]
        )

    def test_equal_empty(self: Self, /) -> None:
        self.assertTrue(
            MutableSetSlot() == set()  # type: ignore[comparison-overlap]
        )

    def test_equal_different_elements(self: Self, /) -> None:
        self.assertFalse(
            MutableSetSlot({1, 2}) == {1, 3}  # type: ignore[comparison-overlap]
        )

    def test_not_equal_different_elements(self: Self, /) -> None:
        self.assertTrue(
            MutableSetSlot({1, 2}) != {1, 3}  # type: ignore[comparison-overlap]
        )

    def test_not_equal_different_size(self: Self, /) -> None:
        self.assertTrue(
            MutableSetSlot({1, 2}) != {1, 2, 3}  # type: ignore[comparison-overlap]
        )

    def test_not_equal_empty_and_nonempty(self: Self, /) -> None:
        self.assertTrue(
            MutableSetSlot() != {1}  # type: ignore[comparison-overlap]
        )

    def test_not_equal_same_elements(self: Self, /) -> None:
        self.assertFalse(
            MutableSetSlot({1, 2, 3}) != {1, 2, 3}  # type: ignore[comparison-overlap]
        )


class TestOperatorLessThan(unittest.TestCase):
    def test_proper_subset(self: Self, /) -> None:
        self.assertTrue(MutableSetSlot({1, 2}) < {1, 2, 3})

    def test_equal_sets_are_not_less(self: Self, /) -> None:
        self.assertFalse(MutableSetSlot({1, 2}) < {1, 2})

    def test_non_subset_is_not_less(self: Self, /) -> None:
        self.assertFalse(MutableSetSlot({1, 4}) < {1, 2, 3})

    def test_empty_is_less_than_nonempty(self: Self, /) -> None:
        self.assertTrue(MutableSetSlot() < {1})


class TestOperatorLessThanOrEqual(unittest.TestCase):
    def test_proper_subset(self: Self, /) -> None:
        self.assertTrue(MutableSetSlot({1, 2}) <= {1, 2, 3})

    def test_equal_sets(self: Self, /) -> None:
        self.assertTrue(MutableSetSlot({1, 2}) <= {1, 2})

    def test_non_subset(self: Self, /) -> None:
        self.assertFalse(MutableSetSlot({1, 4}) <= {1, 2, 3})

    def test_empty_subset(self: Self, /) -> None:
        self.assertTrue(MutableSetSlot() <= {1, 2})


class TestOperatorGreaterThan(unittest.TestCase):
    def test_proper_superset(self: Self, /) -> None:
        self.assertTrue(MutableSetSlot({1, 2, 3}) > {1, 2})

    def test_equal_sets_are_not_greater(self: Self, /) -> None:
        self.assertFalse(MutableSetSlot({1, 2}) > {1, 2})

    def test_non_superset_is_not_greater(self: Self, /) -> None:
        self.assertFalse(MutableSetSlot({1, 4}) > {1, 2})

    def test_nonempty_greater_than_empty(self: Self, /) -> None:
        self.assertTrue(MutableSetSlot({1}) > set())


class TestOperatorGreaterThanOrEqual(unittest.TestCase):
    def test_proper_superset(self: Self, /) -> None:
        self.assertTrue(MutableSetSlot({1, 2, 3}) >= {1, 2})

    def test_equal_sets(self: Self, /) -> None:
        self.assertTrue(MutableSetSlot({1, 2}) >= {1, 2})

    def test_non_superset(self: Self, /) -> None:
        self.assertFalse(MutableSetSlot({1, 4}) >= {1, 2})

    def test_nonempty_superset_of_empty(self: Self, /) -> None:
        self.assertTrue(MutableSetSlot({1}) >= set())


class TestOperatorOr(unittest.TestCase):
    def test_disjoint_union(self: Self, /) -> None:
        self.assertEqual(MutableSetSlot({1, 2}) | {3, 4}, {1, 2, 3, 4})

    def test_overlapping_union(self: Self, /) -> None:
        self.assertEqual(MutableSetSlot({1, 2}) | {2, 3}, {1, 2, 3})

    def test_union_with_empty(self: Self, /) -> None:
        self.assertEqual(MutableSetSlot({1, 2}) | set(), {1, 2})

    def test_empty_union(self: Self, /) -> None:
        self.assertEqual(MutableSetSlot() | {1, 2}, {1, 2})


class TestOperatorAnd(unittest.TestCase):
    def test_overlapping_intersection(self: Self, /) -> None:
        self.assertEqual(MutableSetSlot({1, 2, 3}) & {2, 3, 4}, {2, 3})

    def test_disjoint_intersection(self: Self, /) -> None:
        self.assertEqual(MutableSetSlot({1, 2}) & {3, 4}, set())

    def test_intersection_with_empty(self: Self, /) -> None:
        self.assertEqual(MutableSetSlot({1, 2}) & set(), set())

    def test_intersection_with_self_elements(self: Self, /) -> None:
        self.assertEqual(MutableSetSlot({1, 2}) & {1, 2}, {1, 2})


class TestOperatorSubtract(unittest.TestCase):
    def test_remove_present_elements(self: Self, /) -> None:
        self.assertEqual(MutableSetSlot({1, 2, 3}) - {2}, {1, 3})

    def test_remove_multiple_elements(self: Self, /) -> None:
        self.assertEqual(MutableSetSlot({1, 2, 3, 4}) - {2, 4}, {1, 3})

    def test_subtract_disjoint_set(self: Self, /) -> None:
        self.assertEqual(MutableSetSlot({1, 2}) - {3, 4}, {1, 2})

    def test_subtract_all_elements(self: Self, /) -> None:
        self.assertEqual(MutableSetSlot({1, 2}) - {1, 2}, set())


class TestOperatorXor(unittest.TestCase):
    def test_partially_overlapping_sets(self: Self, /) -> None:
        self.assertEqual(MutableSetSlot({1, 2, 3}) ^ {3, 4}, {1, 2, 4})

    def test_disjoint_sets(self: Self, /) -> None:
        self.assertEqual(MutableSetSlot({1, 2}) ^ {3, 4}, {1, 2, 3, 4})

    def test_identical_sets(self: Self, /) -> None:
        self.assertEqual(MutableSetSlot({1, 2}) ^ {1, 2}, set())

    def test_xor_with_empty(self: Self, /) -> None:
        self.assertEqual(MutableSetSlot({1, 2}) ^ set(), {1, 2})


class TestOperatorInPlaceOr(unittest.TestCase):
    def test_adds_new_elements(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        value |= {3, 4}
        self.assertEqual(value, {1, 2, 3, 4})

    def test_ignores_existing_elements(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        value |= {2, 3}
        self.assertEqual(value, {1, 2, 3})

    def test_empty_operand(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        value |= set()
        self.assertEqual(value, {1, 2})

    def test_mutates_same_object(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1})
        original_id = id(value)
        value |= {2}
        self.assertEqual(id(value), original_id)


class TestOperatorInPlaceAnd(unittest.TestCase):
    def test_keeps_common_elements(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        value &= {2, 3, 4}
        self.assertEqual(value, {2, 3})

    def test_disjoint_sets_become_empty(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        value &= {3, 4}
        self.assertEqual(value, set())

    def test_identical_sets_unchanged(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        value &= {1, 2}
        self.assertEqual(value, {1, 2})

    def test_mutates_same_object(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        original_id = id(value)
        value &= {2}
        self.assertEqual(id(value), original_id)


class TestOperatorInPlaceSubtract(unittest.TestCase):
    def test_removes_elements(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        value -= {2}
        self.assertEqual(value, {1, 3})

    def test_disjoint_operand_changes_nothing(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        value -= {3, 4}
        self.assertEqual(value, {1, 2})

    def test_removing_everything(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        value -= {1, 2}
        self.assertEqual(value, set())

    def test_mutates_same_object(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        original_id = id(value)
        value -= {2}
        self.assertEqual(id(value), original_id)


class TestOperatorInPlaceXor(unittest.TestCase):
    def test_partial_overlap(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        value ^= {3, 4}
        self.assertEqual(value, {1, 2, 4})

    def test_disjoint_sets(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        value ^= {3, 4}
        self.assertEqual(value, {1, 2, 3, 4})

    def test_identical_sets_become_empty(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        value ^= {1, 2}
        self.assertEqual(value, set())

    def test_mutates_same_object(self: Self, /) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        original_id = id(value)
        value ^= {2, 3}
        self.assertEqual(id(value), original_id)


class TestOperatorContains(unittest.TestCase):
    def test_contains_existing_integer(self: Self, /) -> None:
        self.assertTrue(1 in MutableSetSlot({1, 2, 3}))

    def test_does_not_contain_missing_integer(self: Self, /) -> None:
        self.assertFalse(4 in MutableSetSlot({1, 2, 3}))

    def test_contains_existing_string(self: Self, /) -> None:
        self.assertTrue("a" in MutableSetSlot({"a", "b"}))

    def test_empty_contains_nothing(self: Self, /) -> None:
        self.assertFalse(1 in MutableSetSlot())


class TestOperatorNotContains(unittest.TestCase):
    def test_missing_integer(self: Self, /) -> None:
        self.assertTrue(4 not in MutableSetSlot({1, 2, 3}))

    def test_existing_integer(self: Self, /) -> None:
        self.assertFalse(1 not in MutableSetSlot({1, 2, 3}))

    def test_missing_string(self: Self, /) -> None:
        self.assertTrue("c" not in MutableSetSlot({"a", "b"}))

    def test_everything_not_in_empty(self: Self, /) -> None:
        self.assertTrue(1 not in MutableSetSlot())


if __name__ == "__main__":
    unittest.main()
