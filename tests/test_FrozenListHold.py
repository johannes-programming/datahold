import operator
import unittest
from typing import Any, Self

from Lazy import Lazy

import datahold


class TestCountMethod(unittest.TestCase):
    def test_count_repeated_value(self: Self) -> None:
        self.assertEqual(datahold.FrozenListSlot((1, 2, 2, 3)).count(2), 2)

    def test_count_missing_value(self: Self) -> None:
        self.assertEqual(datahold.FrozenListSlot((1, 2, 3)).count(4), 0)

    def test_count_empty_collection(self: Self) -> None:
        self.assertEqual(datahold.FrozenListSlot(()).count(1), 0)

    def test_count_uses_equality(self: Self) -> None:
        self.assertEqual(datahold.FrozenListSlot((1, True, 2)).count(1), 2)


class TestIndexMethod(unittest.TestCase):
    def test_index_first_occurrence(self: Self) -> None:
        self.assertEqual(
            datahold.FrozenListSlot(("a", "b", "a")).index("a"), 0
        )

    def test_index_with_start(self: Self) -> None:
        self.assertEqual(
            datahold.FrozenListSlot(("a", "b", "a")).index("a", 1), 2
        )

    def test_index_with_start_and_stop(self: Self) -> None:
        self.assertEqual(
            datahold.FrozenListSlot(("a", "b", "a", "b")).index("b", 2, 4),
            3,
        )

    def test_index_missing_value(self: Self) -> None:
        with self.assertRaises(ValueError):
            datahold.FrozenListSlot((1, 2, 3)).index(4)


class TestAdditionOperator(unittest.TestCase):
    def test_add_two_nonempty_values(self: Self) -> None:
        x: datahold.FrozenListSlot[int]
        y: datahold.FrozenListSlot[int]
        x = datahold.FrozenListSlot((1, 2))
        y = datahold.FrozenListSlot((3, 4))
        self.assertEqual(tuple(x + y), (1, 2, 3, 4))

    def test_add_empty_right_operand(self: Self) -> None:
        x: datahold.FrozenListSlot[int]
        y: datahold.FrozenListSlot[int]
        x = datahold.FrozenListSlot((1, 2))
        y = datahold.FrozenListSlot(())
        self.assertEqual(tuple(x + y), (1, 2))

    def test_add_empty_left_operand(self: Self) -> None:
        x: datahold.FrozenListSlot[int]
        y: datahold.FrozenListSlot[int]
        x = datahold.FrozenListSlot(())
        y = datahold.FrozenListSlot((1, 2))
        self.assertEqual(tuple(x + y), (1, 2))

    def test_add_invalid_operand(self: Self) -> None:
        with self.assertRaises(TypeError):
            datahold.FrozenListSlot((1, 2)) + [3, 4]  # type: ignore[operator]


class TestMultiplicationOperator(unittest.TestCase):
    def test_multiply_by_positive_integer(self: Self) -> None:
        x: datahold.FrozenListSlot[int]
        x = datahold.FrozenListSlot((1, 2))
        self.assertEqual(tuple(x * 3), (1, 2, 1, 2, 1, 2))

    def test_multiply_by_zero(self: Self) -> None:
        x: datahold.FrozenListSlot[int]
        x = datahold.FrozenListSlot((1, 2))
        self.assertEqual(tuple(x * 0), ())

    def test_multiply_by_negative_integer(self: Self) -> None:
        x: datahold.FrozenListSlot[int]
        x = datahold.FrozenListSlot((1, 2))
        self.assertEqual(tuple(x * -2), ())

    def test_reflected_multiplication(self: Self) -> None:
        x: datahold.FrozenListSlot[int]
        x = datahold.FrozenListSlot((1, 2))
        self.assertEqual(tuple(2 * x), (1, 2, 1, 2))


class TestMembershipOperator(unittest.TestCase):
    def test_contains_present_value(self: Self) -> None:
        self.assertTrue(2 in datahold.FrozenListSlot((1, 2, 3)))

    def test_contains_missing_value(self: Self) -> None:
        self.assertFalse(4 in datahold.FrozenListSlot((1, 2, 3)))

    def test_contains_nested_value(self: Self) -> None:
        self.assertTrue((1, 2) in datahold.FrozenListSlot(((1, 2), (3, 4))))

    def test_contains_uses_equality(self: Self) -> None:
        self.assertTrue(True in datahold.FrozenListSlot((1, 2, 3)))


class TestNonMembershipOperator(unittest.TestCase):
    def test_not_contains_missing_value(self: Self) -> None:
        self.assertTrue(4 not in datahold.FrozenListSlot((1, 2, 3)))

    def test_not_contains_present_value(self: Self) -> None:
        self.assertFalse(2 not in datahold.FrozenListSlot((1, 2, 3)))

    def test_not_contains_empty_collection(self: Self) -> None:
        self.assertTrue(1 not in datahold.FrozenListSlot(()))

    def test_not_contains_nested_value(self: Self) -> None:
        self.assertTrue(
            (5, 6) not in datahold.FrozenListSlot(((1, 2), (3, 4)))
        )


class TestSubscriptionOperator(unittest.TestCase):
    def test_positive_index(self: Self) -> None:
        self.assertEqual(datahold.FrozenListSlot(("a", "b", "c"))[1], "b")

    def test_negative_index(self: Self) -> None:
        self.assertEqual(datahold.FrozenListSlot(("a", "b", "c"))[-1], "c")

    def test_basic_slice(self: Self) -> None:
        result: datahold.FrozenListSlot[int]
        result = datahold.FrozenListSlot((0, 1, 2, 3, 4))[1:4]
        self.assertEqual(tuple(result), (1, 2, 3))

    def test_extended_slice(self: Self) -> None:
        result: datahold.FrozenListSlot[int]
        result = datahold.FrozenListSlot((0, 1, 2, 3, 4, 5))[::2]
        self.assertEqual(tuple(result), (0, 2, 4))


class TestEqualityOperator(unittest.TestCase):
    def test_equal_values(self: Self) -> None:
        x: datahold.FrozenListSlot[int]
        y: datahold.FrozenListSlot[int]
        x = datahold.FrozenListSlot((1, 2))
        y = datahold.FrozenListSlot((1, 2))
        self.assertTrue(x == y)

    def test_different_values(self: Self) -> None:
        self.assertFalse(
            datahold.FrozenListSlot((1, 2)) == datahold.FrozenListSlot((1, 3))
        )

    def test_different_lengths(self: Self) -> None:
        self.assertFalse(
            datahold.FrozenListSlot((1, 2))
            == datahold.FrozenListSlot((1, 2, 3))
        )

    def test_tuple_comparison(self: Self) -> None:
        self.assertTrue(list(datahold.FrozenListSlot((1, 2))) == [1, 2])


class TestInequalityOperator(unittest.TestCase):
    def test_different_values(self: Self) -> None:
        self.assertTrue(
            datahold.FrozenListSlot((1, 2)) != datahold.FrozenListSlot((1, 3))
        )

    def test_equal_values(self: Self) -> None:
        self.assertFalse(
            datahold.FrozenListSlot((1, 2)) != datahold.FrozenListSlot((1, 2))
        )

    def test_different_lengths(self: Self) -> None:
        self.assertTrue(
            datahold.FrozenListSlot((1, 2))
            != datahold.FrozenListSlot((1, 2, 3))
        )

    def test_list_comparison(self: Self) -> None:
        self.assertTrue(datahold.FrozenListSlot((1, 2)) != [1, 2])


class TestLessThanOperator(unittest.TestCase):
    def test_less_at_first_item(self: Self) -> None:
        self.assertTrue(
            datahold.FrozenListSlot((1, 9)) < datahold.FrozenListSlot((2, 0))
        )

    def test_less_at_later_item(self: Self) -> None:
        self.assertTrue(
            datahold.FrozenListSlot((1, 2)) < datahold.FrozenListSlot((1, 3))
        )

    def test_shorter_prefix_is_less(self: Self) -> None:
        self.assertTrue(
            datahold.FrozenListSlot((1, 2))
            < datahold.FrozenListSlot((1, 2, 0))
        )

    def test_equal_value_is_not_less(self: Self) -> None:
        self.assertFalse(
            datahold.FrozenListSlot((1, 2)) < datahold.FrozenListSlot((1, 2))
        )


class TestLessThanOrEqualOperator(unittest.TestCase):
    def test_less_value(self: Self) -> None:
        x: datahold.FrozenListSlot[int]
        y: datahold.FrozenListSlot[int]
        x = datahold.FrozenListSlot((1, 2))
        y = datahold.FrozenListSlot((1, 3))
        self.assertTrue(x <= y)

    def test_equal_value(self: Self) -> None:
        x: datahold.FrozenListSlot[int]
        y: datahold.FrozenListSlot[int]
        x = datahold.FrozenListSlot((1, 2))
        y = datahold.FrozenListSlot((1, 2))
        self.assertTrue(x <= y)

    def test_greater_value(self: Self) -> None:
        x: datahold.FrozenListSlot[int]
        y: datahold.FrozenListSlot[int]
        x = datahold.FrozenListSlot((2, 0))
        y = datahold.FrozenListSlot((1, 9))
        self.assertFalse(x <= y)

    def test_shorter_prefix(self: Self) -> None:
        x: datahold.FrozenListSlot[int]
        y: datahold.FrozenListSlot[int]
        x = datahold.FrozenListSlot((1,))
        y = datahold.FrozenListSlot((1, 0))
        self.assertTrue(x <= y)


class TestAugmentedAdditionOperator(unittest.TestCase):
    def test_augmented_add_nonempty_values(self: Self) -> None:
        value: datahold.ListLike[int]
        value = datahold.FrozenListSlot((1, 2))
        value += datahold.FrozenListSlot((3, 4))
        self.assertEqual(tuple(value), (1, 2, 3, 4))

    def test_augmented_add_empty_right_operand(self: Self) -> None:
        value: datahold.ListLike[int]
        value = datahold.FrozenListSlot((1, 2))
        value += datahold.FrozenListSlot(())
        self.assertEqual(tuple(value), (1, 2))

    def test_augmented_add_to_empty_value(self: Self) -> None:
        value: datahold.ListLike[int]
        value = datahold.FrozenListSlot(())
        value += datahold.FrozenListSlot((1, 2))
        self.assertEqual(tuple(value), (1, 2))

    def test_augmented_add_invalid_operand(self: Self) -> None:
        value: Any
        value = datahold.FrozenListSlot((1, 2))
        with self.assertRaises(TypeError):
            value += [3, 4]


class TestAugmentedMultiplicationOperator(unittest.TestCase):
    def test_augmented_multiply_positive_integer(self: Self) -> None:
        value: datahold.FrozenListSlot[int]
        value = datahold.FrozenListSlot((1, 2))
        value *= 2
        self.assertEqual(tuple(value), (1, 2, 1, 2))

    def test_augmented_multiply_by_zero(self: Self) -> None:
        value: datahold.FrozenListSlot[int]
        value = datahold.FrozenListSlot((1, 2))
        value *= 0
        self.assertEqual(tuple(value), ())

    def test_augmented_multiply_by_negative_integer(self: Self) -> None:
        value: datahold.FrozenListSlot[int]
        value = datahold.FrozenListSlot((1, 2))
        value *= -1
        self.assertEqual(tuple(value), ())

    def test_augmented_multiply_invalid_operand(self: Self) -> None:
        value: datahold.FrozenListSlot[int]
        value = datahold.FrozenListSlot((1, 2))
        with self.assertRaises(TypeError):
            value *= 1.5  # type: ignore[operator]


class TestAllBuiltin(unittest.TestCase):
    def test_all_truthy_elements(self: Self) -> None:
        self.assertEqual(
            all(datahold.FrozenListSlot((1, "x", True))), all((1, "x", True))
        )

    def test_all_with_falsy_element(self: Self) -> None:
        self.assertEqual(
            all(datahold.FrozenListSlot((1, 0, 3))), all((1, 0, 3))
        )

    def test_all_empty(self: Self) -> None:
        self.assertEqual(all(datahold.FrozenListSlot(())), all(()))

    def test_all_falsy_elements(self: Self) -> None:
        self.assertEqual(
            all(datahold.FrozenListSlot((False, None, ""))),
            all((False, None, "")),
        )


class TestAnyBuiltin(unittest.TestCase):
    def test_any_truthy_element(self: Self) -> None:
        self.assertEqual(
            any(datahold.FrozenListSlot((0, "", 3))), any((0, "", 3))
        )

    def test_any_without_truthy_element(self: Self) -> None:
        self.assertEqual(
            any(datahold.FrozenListSlot((0, "", None))), any((0, "", None))
        )

    def test_any_empty(self: Self) -> None:
        self.assertEqual(any(datahold.FrozenListSlot(())), any(()))

    def test_any_all_truthy(self: Self) -> None:
        self.assertEqual(
            any(datahold.FrozenListSlot((1, 2, 3))), any((1, 2, 3))
        )


class TestBoolBuiltin(unittest.TestCase):
    def test_bool_nonempty(self: Self) -> None:
        self.assertEqual(bool(datahold.FrozenListSlot((1,))), bool((1,)))

    def test_bool_empty(self: Self) -> None:
        self.assertEqual(bool(datahold.FrozenListSlot(())), bool(()))

    def test_bool_nonempty_with_false_element(self: Self) -> None:
        self.assertEqual(
            bool(datahold.FrozenListSlot((False,))), bool((False,))
        )

    def test_bool_nonempty_with_none_element(self: Self) -> None:
        self.assertEqual(bool(datahold.FrozenListSlot((None,))), bool((None,)))


class TestEnumerateBuiltin(unittest.TestCase):
    def test_enumerate_default_start(self: Self) -> None:
        self.assertEqual(
            list(enumerate(datahold.FrozenListSlot(("a", "b")))),
            list(enumerate(("a", "b"))),
        )

    def test_enumerate_positive_start(self: Self) -> None:
        self.assertEqual(
            list(enumerate(datahold.FrozenListSlot(("a", "b")), 5)),
            list(enumerate(("a", "b"), 5)),
        )

    def test_enumerate_negative_start(self: Self) -> None:
        self.assertEqual(
            list(enumerate(datahold.FrozenListSlot(("a", "b")), -2)),
            list(enumerate(("a", "b"), -2)),
        )

    def test_enumerate_empty(self: Self) -> None:
        self.assertEqual(
            list(enumerate(datahold.FrozenListSlot(()))),
            list(enumerate(())),
        )


class TestHashBuiltin(unittest.TestCase):
    def test_hash_integer_elements(self: Self) -> None:
        self.assertEqual(
            hash(datahold.FrozenListSlot((1, 2, 3))), hash((1, 2, 3))
        )

    def test_hash_empty(self: Self) -> None:
        self.assertEqual(hash(datahold.FrozenListSlot(())), hash(()))

    def test_hash_nested_hashable_elements(self: Self) -> None:
        self.assertEqual(
            hash(datahold.FrozenListSlot(((1, 2), (3, 4)))),
            hash(((1, 2), (3, 4))),
        )

    def test_hash_rejects_unhashable_element(self: Self) -> None:
        with self.assertRaises(TypeError):
            hash(datahold.FrozenListSlot(([1, 2],)))


class TestIterBuiltin(unittest.TestCase):
    def test_iter_preserves_order(self: Self) -> None:
        self.assertEqual(
            list(iter(datahold.FrozenListSlot((1, 2, 3)))),
            list(iter((1, 2, 3))),
        )

    def test_iter_empty(self: Self) -> None:
        self.assertEqual(
            list(iter(datahold.FrozenListSlot(()))),
            list(iter(())),
        )

    def test_iter_nested_elements(self: Self) -> None:
        self.assertEqual(
            list(iter(datahold.FrozenListSlot(((1, 2), (3, 4))))),
            list(iter(((1, 2), (3, 4)))),
        )

    def test_iterators_are_independent(self: Self) -> None:
        value = datahold.FrozenListSlot((1, 2, 3))
        first = iter(value)
        second = iter(value)
        self.assertEqual((next(first), next(first), next(second)), (1, 2, 1))


class TestLenBuiltin(unittest.TestCase):
    def test_len_multiple_elements(self: Self) -> None:
        self.assertEqual(
            len(datahold.FrozenListSlot((1, 2, 3))), len((1, 2, 3))
        )

    def test_len_single_element(self: Self) -> None:
        self.assertEqual(len(datahold.FrozenListSlot((1,))), len((1,)))

    def test_len_empty(self: Self) -> None:
        self.assertEqual(len(datahold.FrozenListSlot(())), len(()))

    def test_len_nested_elements(self: Self) -> None:
        self.assertEqual(
            len(datahold.FrozenListSlot(((1, 2), (3, 4)))),
            len(((1, 2), (3, 4))),
        )


class TestListBuiltin(unittest.TestCase):
    def test_list_integer_elements(self: Self) -> None:
        self.assertEqual(
            list(datahold.FrozenListSlot((1, 2, 3))), list((1, 2, 3))
        )

    def test_list_empty(self: Self) -> None:
        self.assertEqual(list(datahold.FrozenListSlot(())), list(()))

    def test_list_nested_elements(self: Self) -> None:
        self.assertEqual(
            list(datahold.FrozenListSlot(((1, 2), (3, 4)))),
            list(((1, 2), (3, 4))),
        )

    def test_list_preserves_duplicate_elements(self: Self) -> None:
        self.assertEqual(
            list(datahold.FrozenListSlot(("a", "a", "b"))),
            list(("a", "a", "b")),
        )


class TestMaxBuiltin(unittest.TestCase):
    def test_max_integer_elements(self: Self) -> None:
        self.assertEqual(
            max(datahold.FrozenListSlot((3, 1, 4, 2))), max((3, 1, 4, 2))
        )

    def test_max_string_elements(self: Self) -> None:
        self.assertEqual(
            max(datahold.FrozenListSlot(("beta", "alpha", "gamma"))),
            max(("beta", "alpha", "gamma")),
        )

    def test_max_with_key(self: Self) -> None:
        self.assertEqual(
            max(datahold.FrozenListSlot(("a", "abcd", "xy")), key=len),
            max(("a", "abcd", "xy"), key=len),
        )

    def test_max_empty_raises_value_error(self: Self) -> None:
        with self.assertRaises(ValueError):
            max(datahold.FrozenListSlot(()))


class TestMinBuiltin(unittest.TestCase):
    def test_min_integer_elements(self: Self) -> None:
        self.assertEqual(
            min(datahold.FrozenListSlot((3, 1, 4, 2))), min((3, 1, 4, 2))
        )

    def test_min_string_elements(self: Self) -> None:
        self.assertEqual(
            min(datahold.FrozenListSlot(("beta", "alpha", "gamma"))),
            min(("beta", "alpha", "gamma")),
        )

    def test_min_with_key(self: Self) -> None:
        self.assertEqual(
            min(datahold.FrozenListSlot(("abcd", "a", "xy")), key=len),
            min(("abcd", "a", "xy"), key=len),
        )

    def test_min_empty_raises_value_error(self: Self) -> None:
        with self.assertRaises(ValueError):
            min(datahold.FrozenListSlot(()))


class TestReversedBuiltin(unittest.TestCase):
    def test_reversed_multiple_elements(self: Self) -> None:
        self.assertEqual(
            list(reversed(datahold.FrozenListSlot((1, 2, 3)))),
            list(reversed((1, 2, 3))),
        )

    def test_reversed_single_element(self: Self) -> None:
        self.assertEqual(
            list(reversed(datahold.FrozenListSlot(("x",)))),
            list(reversed(("x",))),
        )

    def test_reversed_empty(self: Self) -> None:
        self.assertEqual(
            list(reversed(datahold.FrozenListSlot(()))),
            list(reversed(())),
        )

    def test_reversed_nested_elements(self: Self) -> None:
        self.assertEqual(
            list(reversed(datahold.FrozenListSlot(((1, 2), (3, 4))))),
            list(reversed(((1, 2), (3, 4)))),
        )


class TestSortedBuiltin(unittest.TestCase):
    def test_sorted_integer_elements(self: Self) -> None:
        self.assertEqual(
            sorted(datahold.FrozenListSlot((3, 1, 2))),
            sorted((3, 1, 2)),
        )

    def test_sorted_string_elements(self: Self) -> None:
        self.assertEqual(
            sorted(datahold.FrozenListSlot(("beta", "alpha", "gamma"))),
            sorted(("beta", "alpha", "gamma")),
        )

    def test_sorted_reverse(self: Self) -> None:
        self.assertEqual(
            sorted(datahold.FrozenListSlot((3, 1, 2)), reverse=True),
            sorted((3, 1, 2), reverse=True),
        )

    def test_sorted_with_key(self: Self) -> None:
        self.assertEqual(
            sorted(datahold.FrozenListSlot(("aaaa", "b", "cc")), key=len),
            sorted(("aaaa", "b", "cc"), key=len),
        )


class TestSumBuiltin(unittest.TestCase):
    def test_sum_integer_elements(self: Self) -> None:
        self.assertEqual(
            sum(datahold.FrozenListSlot((1, 2, 3))), sum((1, 2, 3))
        )

    def test_sum_with_start(self: Self) -> None:
        self.assertEqual(
            sum(datahold.FrozenListSlot((1, 2, 3)), 10),
            sum((1, 2, 3), 10),
        )

    def test_sum_empty(self: Self) -> None:
        self.assertEqual(sum(datahold.FrozenListSlot(())), sum(()))

    def test_sum_float_elements(self: Self) -> None:
        self.assertEqual(
            sum(datahold.FrozenListSlot((1.5, 2.5, 3.0))),
            sum((1.5, 2.5, 3.0)),
        )


class TestTupleBuiltin(unittest.TestCase):
    def test_tuple_integer_elements(self: Self) -> None:
        self.assertEqual(
            tuple(datahold.FrozenListSlot((1, 2, 3))), tuple((1, 2, 3))
        )

    def test_tuple_empty(self: Self) -> None:
        self.assertEqual(tuple(datahold.FrozenListSlot(())), tuple(()))

    def test_tuple_nested_elements(self: Self) -> None:
        self.assertEqual(
            tuple(datahold.FrozenListSlot(((1, 2), (3, 4)))),
            tuple(((1, 2), (3, 4))),
        )

    def test_tuple_preserves_duplicate_elements(self: Self) -> None:
        self.assertEqual(
            tuple(datahold.FrozenListSlot(("a", "a", "b"))),
            tuple(("a", "a", "b")),
        )


if __name__ == "__main__":
    unittest.main()
