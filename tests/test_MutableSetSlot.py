import unittest
from typing import Any, Self

from datahold import MutableSetSlot


class TestAdd(unittest.TestCase):
    def test_adds_new_element(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        value.add(3)
        self.assertEqual(set(value), {1, 2, 3})

    def test_adding_duplicate_does_not_change_set(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        value.add(2)
        self.assertEqual(set(value), {1, 2})

    def test_adds_hashable_tuple(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot()
        value.add((1, 2))
        self.assertEqual(set(value), {(1, 2)})

    def test_adding_unhashable_element_raises_type_error(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1})
        with self.assertRaises(TypeError):
            value.add([2])
        self.assertEqual(set(value), {1})


class TestClear(unittest.TestCase):
    def test_clears_populated_set(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        value.clear()
        self.assertEqual(set(value), set())

    def test_clearing_empty_set_keeps_it_empty(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot()
        value.clear()
        self.assertEqual(set(value), set())

    def test_clear_returns_none(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        self.assertIsNone(value.clear())  # type: ignore[func-returns-value]

    def test_set_can_be_reused_after_clear(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        value.clear()
        value.add(3)
        self.assertEqual(set(value), {3})


class TestCopy(unittest.TestCase):
    def test_copy_has_same_contents(self: Self) -> None:
        copied: MutableSetSlot[Any]
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        copied = value.copy()
        self.assertEqual(set(copied), {1, 2, 3})

    def test_copy_is_a_different_object(self: Self) -> None:
        copied: MutableSetSlot[Any]
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        copied = value.copy()
        self.assertIsNot(copied, value)

    def test_copy_is_independent_of_original(self: Self) -> None:
        copied: MutableSetSlot[Any]
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        copied = value.copy()
        copied.add(3)
        self.assertEqual(set(value), {1, 2})
        self.assertEqual(set(copied), {1, 2, 3})

    def test_copy_of_empty_set_is_empty(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot()
        copied = value.copy()
        self.assertEqual(set(copied), set())


class TestDifference(unittest.TestCase):
    def test_difference_removes_shared_elements(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        result = value.difference({2, 3, 4})
        self.assertEqual(set(result), {1})

    def test_difference_accepts_multiple_iterables(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3, 4})
        result = value.difference({1}, [2, 5])
        self.assertEqual(set(result), {3, 4})

    def test_difference_with_disjoint_set_is_unchanged(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        result = value.difference({3, 4})
        self.assertEqual(set(result), {1, 2})

    def test_difference_does_not_modify_original(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        value.difference({2})
        self.assertEqual(set(value), {1, 2, 3})


class TestDifferenceUpdate(unittest.TestCase):
    def test_difference_update_removes_shared_elements(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        value.difference_update({2, 4})
        self.assertEqual(set(value), {1, 3})

    def test_difference_update_accepts_multiple_iterables(self: Self) -> None:
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

    def test_difference_update_with_self_empties_set(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        value.difference_update(value)
        self.assertEqual(set(value), set())


class TestDiscard(unittest.TestCase):
    def test_discards_existing_element(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        value.discard(2)
        self.assertEqual(set(value), {1, 3})

    def test_discarding_missing_element_does_not_raise(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        value.discard(3)
        self.assertEqual(set(value), {1, 2})

    def test_discard_returns_none(self: Self) -> None:
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


class TestIntersection(unittest.TestCase):
    def test_intersection_returns_shared_elements(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        result = value.intersection({2, 3, 4})
        self.assertEqual(set(result), {2, 3})

    def test_intersection_accepts_multiple_iterables(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3, 4})
        result = value.intersection({2, 3, 4}, [3, 4, 5])
        self.assertEqual(set(result), {3, 4})

    def test_intersection_with_disjoint_set_is_empty(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        result = value.intersection({3, 4})
        self.assertEqual(set(result), set())

    def test_intersection_does_not_modify_original(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        value.intersection({2})
        self.assertEqual(set(value), {1, 2, 3})


class TestIntersectionUpdate(unittest.TestCase):
    def test_intersection_update_keeps_shared_elements(self: Self) -> None:
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

    def test_intersection_update_with_self_is_unchanged(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        value.intersection_update(value)
        self.assertEqual(set(value), {1, 2, 3})


class TestIsDisjoint(unittest.TestCase):
    def test_disjoint_sets_return_true(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        self.assertTrue(value.isdisjoint({3, 4}))

    def test_overlapping_sets_return_false(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        self.assertFalse(value.isdisjoint({2, 3}))

    def test_empty_set_is_disjoint_from_populated_set(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot()
        self.assertTrue(value.isdisjoint({1, 2}))

    def test_isdisjoint_accepts_generator(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        other = (number for number in (3, 4))
        self.assertTrue(value.isdisjoint(other))


class TestIsSubset(unittest.TestCase):
    def test_proper_subset_returns_true(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        self.assertTrue(value.issubset({1, 2, 3}))

    def test_equal_set_is_subset(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        self.assertTrue(value.issubset({1, 2}))

    def test_non_subset_returns_false(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 4})
        self.assertFalse(value.issubset({1, 2, 3}))

    def test_empty_set_is_subset_of_any_set(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot()
        self.assertTrue(value.issubset({1, 2}))


class TestIsSuperset(unittest.TestCase):
    def test_proper_superset_returns_true(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        self.assertTrue(value.issuperset({1, 2}))

    def test_equal_set_is_superset(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        self.assertTrue(value.issuperset({1, 2}))

    def test_non_superset_returns_false(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        self.assertFalse(value.issuperset({1, 3}))

    def test_every_set_is_superset_of_empty_set(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        self.assertTrue(value.issuperset(set()))


class TestPop(unittest.TestCase):
    def test_pop_returns_and_removes_only_element(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1})
        result = value.pop()
        self.assertEqual(result, 1)
        self.assertEqual(set(value), set())

    def test_pop_from_empty_set_raises_key_error(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot()
        with self.assertRaises(KeyError):
            value.pop()

    def test_pop_removes_one_element_from_populated_set(self: Self) -> None:
        original: set[int]
        result: Any
        value: MutableSetSlot[Any]
        original = {1, 2, 3}
        value = MutableSetSlot(original)
        result = value.pop()
        self.assertIn(result, original)
        self.assertEqual(set(value), original - {result})

    def test_repeated_pop_exhausts_set(self: Self) -> None:
        popped: set[Any]
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        popped = {value.pop(), value.pop(), value.pop()}
        self.assertEqual(popped, {1, 2, 3})
        self.assertEqual(set(value), set())


class TestRemove(unittest.TestCase):
    def test_removes_existing_element(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        value.remove(2)
        self.assertEqual(set(value), {1, 3})

    def test_removing_missing_element_raises_key_error(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        with self.assertRaises(KeyError):
            value.remove(3)
        self.assertEqual(set(value), {1, 2})

    def test_remove_returns_none(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        self.assertIsNone(value.remove(1))  # type: ignore[func-returns-value]

    def test_removing_unhashable_element_raises_type_error(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        with self.assertRaises(Exception):
            # in general you should not rely upon
            # a TypeError or an AttributeError occuring
            value.remove([1])
        self.assertEqual(set(value), {1, 2})


class TestSymmetricDifference(unittest.TestCase):
    def test_symmetric_difference_excludes_shared_elements(self: Self) -> None:
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

    def test_symmetric_difference_of_equal_sets_is_empty(self: Self) -> None:
        result: Any
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        result = value.symmetric_difference({1, 2})
        self.assertEqual(set(result), set())

    def test_symmetric_difference_does_not_modify_original(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2, 3})
        value.symmetric_difference({3, 4})
        self.assertEqual(set(value), {1, 2, 3})


class TestSymmetricDifferenceUpdate(unittest.TestCase):
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

    def test_symmetric_difference_update_returns_none(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        result = value.symmetric_difference_update({2, 3})
        self.assertIsNone(result)
        self.assertEqual(set(value), {1, 3})


class TestUnion(unittest.TestCase):
    def test_union_combines_elements(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        result = value.union({2, 3})
        self.assertEqual(set(result), {1, 2, 3})

    def test_union_accepts_multiple_iterables(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1})
        result = value.union({2}, [3, 4])
        self.assertEqual(set(result), {1, 2, 3, 4})

    def test_union_without_arguments_returns_same_contents(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        result = value.union()
        self.assertEqual(set(result), {1, 2})
        self.assertIsNot(result, value)

    def test_union_does_not_modify_original(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        value.union({3, 4})
        self.assertEqual(set(value), {1, 2})


class TestUpdate(unittest.TestCase):
    def test_update_adds_elements_from_iterable(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        value.update({2, 3, 4})
        self.assertEqual(set(value), {1, 2, 3, 4})

    def test_update_accepts_multiple_iterables(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1})
        value.update({2}, [3, 4])
        self.assertEqual(set(value), {1, 2, 3, 4})

    def test_update_ignores_duplicate_elements(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1, 2})
        value.update([1, 1, 2, 2])
        self.assertEqual(set(value), {1, 2})

    def test_update_returns_none(self: Self) -> None:
        value: MutableSetSlot[Any]
        value = MutableSetSlot({1})
        result = value.update({2, 3})
        self.assertIsNone(result)
        self.assertEqual(set(value), {1, 2, 3})


if __name__ == "__main__":
    unittest.main()
