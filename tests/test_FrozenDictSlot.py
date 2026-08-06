__all__: list[str] = [
    "TestMethodFromKeys",
    "TestMethodGet",
    "TestMethodItems",
    "TestMethodKeys",
    "TestMethodValues",
    "TestOperatorAssignment",
    "TestOperatorContains",
    "TestOperatorDeletion",
    "TestOperatorEquality",
    "TestOperatorInequality",
    "TestOperatorIteration",
    "TestOperatorLength",
    "TestOperatorMappingUnpack",
    "TestOperatorNotContains",
    "TestOperatorReflectedUnion",
    "TestOperatorReversed",
    "TestOperatorSubscription",
    "TestOperatorTruth",
]
import unittest
from collections import abc
from typing import Any, Self

from datahold import FrozenDictSlot


class TestMethodFromKeys(unittest.TestCase):
    def test_fromkeys_uses_none_by_default(self: Self, /) -> None:
        result: Any
        result = FrozenDictSlot.fromkeys(["a", "b", "c"])
        self.assertEqual(result, {"a": None, "b": None, "c": None})

    def test_fromkeys_uses_provided_value(self: Self, /) -> None:
        result: Any
        result = FrozenDictSlot.fromkeys(["a", "b"], 10)
        self.assertEqual(result, {"a": 10, "b": 10})

    def test_fromkeys_uses_same_value_object_for_every_key(
        self: Self, /
    ) -> None:
        result: Any
        value: Any
        value = []
        result = FrozenDictSlot.fromkeys(["a", "b"], value)
        self.assertIs(result["a"], value)
        self.assertIs(result["b"], value)

    def test_fromkeys_removes_duplicate_keys(self: Self, /) -> None:
        result: FrozenDictSlot[Any, Any]
        result = FrozenDictSlot.fromkeys(
            ["a", "b", "a", "c", "b"],
            1,
        )
        self.assertEqual(list(result.keys()), ["a", "b", "c"])
        self.assertEqual(result, {"a": 1, "b": 1, "c": 1})

    def test_fromkeys_accepts_generator(self: Self, /) -> None:
        keys: Any
        result: Any
        keys = (str(number) for number in range(3))
        result = FrozenDictSlot.fromkeys(keys, "value")
        self.assertEqual(
            result,
            {"0": "value", "1": "value", "2": "value"},
        )

    def test_fromkeys_accepts_empty_iterable(self: Self, /) -> None:
        self.assertEqual(FrozenDictSlot.fromkeys([], 1), {})

    def test_fromkeys_returns_frozen_dict_slot(self: Self, /) -> None:
        result: Any
        result = FrozenDictSlot.fromkeys(["a"], 1)
        self.assertIsInstance(result, FrozenDictSlot)

    def test_fromkeys_rejects_unhashable_keys(self: Self, /) -> None:
        with self.assertRaises(TypeError):
            FrozenDictSlot.fromkeys([["unhashable"]], 1)  # type: ignore


class TestMethodGet(unittest.TestCase):
    def test_get_returns_existing_value(self: Self, /) -> None:
        mapping: Any
        mapping = FrozenDictSlot({"a": 1, "b": 2})
        self.assertEqual(mapping.get("a"), 1)

    def test_get_returns_none_for_missing_key(self: Self, /) -> None:
        mapping: Any
        mapping = FrozenDictSlot({"a": 1})
        self.assertIsNone(mapping.get("missing"))

    def test_get_returns_default_for_missing_key(self: Self, /) -> None:
        mapping: Any
        mapping = FrozenDictSlot({"a": 1})
        self.assertEqual(mapping.get("missing", 20), 20)

    def test_get_returns_existing_value_instead_of_default(
        self: Self, /
    ) -> None:
        mapping: Any
        mapping = FrozenDictSlot({"a": 1})
        self.assertEqual(mapping.get("a", 20), 1)

    def test_get_returns_exact_default_object(self: Self, /) -> None:
        default: Any
        mapping: Any
        default = []
        mapping = FrozenDictSlot()
        self.assertIs(mapping.get("missing", default), default)

    def test_get_accepts_different_hashable_key_types(self: Self, /) -> None:
        mapping: FrozenDictSlot[abc.Hashable, str]
        mapping = FrozenDictSlot(
            {  # type: ignore
                1: "integer",
                (2, 3): "tuple",
                None: "none",
            }
        )

        self.assertEqual(mapping.get(1), "integer")
        self.assertEqual(mapping.get((2, 3)), "tuple")
        self.assertEqual(mapping.get(None), "none")

    def test_get_rejects_unhashable_key(self: Self, /) -> None:
        self.assertIsNone(FrozenDictSlot().get([]))

    def test_get_rejects_too_many_arguments(self: Self, /) -> None:
        with self.assertRaises(TypeError):
            FrozenDictSlot().get("a", 1, 2)  # type: ignore[call-overload]


class TestMethodItems(unittest.TestCase):
    def test_items_contains_all_key_value_pairs(self: Self, /) -> None:
        mapping: FrozenDictSlot[str, int]
        mapping = FrozenDictSlot({"a": 1, "b": 2})
        self.assertEqual(
            set(mapping.items()),
            {("a", 1), ("b", 2)},
        )

    def test_items_of_empty_mapping_is_empty(self: Self, /) -> None:
        self.assertEqual(list(FrozenDictSlot().items()), [])

    def test_items_preserves_insertion_order(self: Self, /) -> None:
        mapping: FrozenDictSlot[str, int]
        mapping = FrozenDictSlot(
            [
                ("third", 3),
                ("first", 1),
                ("second", 2),
            ]
        )
        self.assertEqual(
            list(mapping.items()),
            [("third", 3), ("first", 1), ("second", 2)],
        )

    def test_items_supports_membership_testing(self: Self, /) -> None:
        data: FrozenDictSlot[str, int]
        items: Any
        data = FrozenDictSlot({"a": 1, "b": 2})
        items = data.items()
        self.assertIn(("a", 1), items)
        self.assertNotIn(("a", 2), items)

    def test_items_has_correct_length(self: Self, /) -> None:
        data: FrozenDictSlot[str, int]
        items: Any
        data = FrozenDictSlot(
            {
                "a": 1,
                "b": 2,
                "c": 3,
            }
        )
        items = data.items()
        self.assertEqual(len(items), 3)

    def test_items_can_be_iterated_multiple_times(self: Self, /) -> None:
        data: FrozenDictSlot[str, int]
        items: Any
        data = FrozenDictSlot({"a": 1, "b": 2})
        items = data.items()
        self.assertEqual(list(items), [("a", 1), ("b", 2)])
        self.assertEqual(list(items), [("a", 1), ("b", 2)])

    def test_items_rejects_arguments(self: Self, /) -> None:
        with self.assertRaises(TypeError):
            FrozenDictSlot({"a": 1}).items("unexpected")  # type: ignore[arg-type, call-arg]


class TestMethodKeys(unittest.TestCase):
    def test_keys_contains_all_keys(self: Self, /) -> None:
        mapping: Any = FrozenDictSlot({"a": 1, "b": 2, "c": 3})

        self.assertEqual(set(mapping.keys()), {"a", "b", "c"})

    def test_keys_of_empty_mapping_is_empty(self: Self, /) -> None:
        self.assertEqual(list(FrozenDictSlot().keys()), [])

    def test_keys_preserves_insertion_order(self: Self, /) -> None:
        mapping: FrozenDictSlot[str, int]
        other: list[tuple[Any, Any]]
        other = [
            ("third", 3),
            ("first", 1),
            ("second", 2),
        ]
        mapping = FrozenDictSlot(other)
        self.assertEqual(
            list(mapping.keys()),
            ["third", "first", "second"],
        )

    def test_keys_supports_membership_testing(self: Self, /) -> None:
        data: FrozenDictSlot[str, int]
        keys: Any
        data = FrozenDictSlot({"a": 1, "b": 2})
        keys = data.keys()
        self.assertIn("a", keys)
        self.assertNotIn("missing", keys)

    def test_keys_has_correct_length(self: Self, /) -> None:
        data: FrozenDictSlot[str, int]
        keys: Any
        other: dict[str, int]
        other = {
            "a": 1,
            "b": 2,
            "c": 3,
        }
        data = FrozenDictSlot(other)
        keys = data.keys()
        self.assertEqual(len(keys), 3)

    def test_keys_supports_set_operations(self: Self, /) -> None:
        data: FrozenDictSlot[str, int]
        keys: Any
        data = FrozenDictSlot({"a": 1, "b": 2})
        keys = data.keys()
        self.assertEqual(keys & {"b", "c"}, {"b"})
        self.assertEqual(keys | {"c"}, {"a", "b", "c"})

    def test_keys_rejects_arguments(self: Self, /) -> None:
        with self.assertRaises(TypeError):
            FrozenDictSlot({"a": 1}).keys("unexpected")  # type: ignore[arg-type, call-arg]


class TestMethodValues(unittest.TestCase):
    def test_values_contains_all_values(self: Self, /) -> None:
        mapping: FrozenDictSlot[str, int]
        mapping = FrozenDictSlot({"a": 1, "b": 2, "c": 3})
        self.assertEqual(list(mapping.values()), [1, 2, 3])

    def test_values_of_empty_mapping_is_empty(self: Self, /) -> None:
        self.assertEqual(list(FrozenDictSlot().values()), [])

    def test_values_preserves_insertion_order(self: Self, /) -> None:
        mapping: FrozenDictSlot[str, int]
        other: list[tuple[str, int]]
        other = [
            ("third", 3),
            ("first", 1),
            ("second", 2),
        ]
        mapping = FrozenDictSlot(other)
        self.assertEqual(list(mapping.values()), [3, 1, 2])

    def test_values_preserves_duplicates(self: Self, /) -> None:
        mapping: Any
        other: dict[str, int]
        other = {
            "a": 1,
            "b": 1,
            "c": 2,
        }
        mapping = FrozenDictSlot(other)
        self.assertEqual(list(mapping.values()), [1, 1, 2])

    def test_values_supports_membership_testing(self: Self, /) -> None:
        values: Any
        values = FrozenDictSlot[str, int]({"a": 1, "b": 2}).values()
        self.assertIn(1, values)
        self.assertNotIn(3, values)

    def test_values_has_correct_length(self: Self, /) -> None:
        other: Any
        values: Any
        other = {
            "a": 1,
            "b": 2,
            "c": 3,
        }
        values = FrozenDictSlot(other).values()
        self.assertEqual(len(values), 3)

    def test_values_can_be_iterated_multiple_times(self: Self, /) -> None:
        values: Any
        values = FrozenDictSlot[str, int]({"a": 1, "b": 2}).values()
        self.assertEqual(list(values), [1, 2])
        self.assertEqual(list(values), [1, 2])

    def test_values_rejects_arguments(self: Self, /) -> None:
        with self.assertRaises(TypeError):
            FrozenDictSlot({"a": 1}).values("unexpected")  # type: ignore[arg-type, call-arg]


class TestOperatorSubscription(unittest.TestCase):
    def test_string_key(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({"name": "Ada"})
        self.assertEqual(value["name"], "Ada")

    def test_integer_key(self: Self, /) -> None:
        value: FrozenDictSlot[int, str]
        value = FrozenDictSlot({10: "ten"})
        self.assertEqual(value[10], "ten")

    def test_tuple_key(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({(1, 2): "point"})
        self.assertEqual(value[(1, 2)], "point")

    def test_missing_key(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({"a": 1})
        with self.assertRaises(KeyError):
            value["missing"]


class TestOperatorContains(unittest.TestCase):
    def test_present_key(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({"a": 1})
        self.assertTrue("a" in value)

    def test_absent_key(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({"a": 1})
        self.assertFalse("b" in value)

    def test_values_are_not_searched(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({"a": "value"})
        self.assertFalse("value" in value)

    def test_empty_mapping(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({})
        self.assertFalse("a" in value)


class TestOperatorNotContains(unittest.TestCase):
    def test_absent_key(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({"a": 1})
        self.assertTrue("b" not in value)

    def test_present_key(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({"a": 1})
        self.assertFalse("a" not in value)

    def test_value_is_not_a_key(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({"a": 1})
        self.assertTrue(1 not in value)

    def test_empty_mapping(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({})
        self.assertTrue("a" not in value)


class TestOperatorEquality(unittest.TestCase):
    def test_equal_instances(self: Self, /) -> None:
        left: FrozenDictSlot[Any, Any]
        right: FrozenDictSlot[Any, Any]
        left = FrozenDictSlot({"a": 1, "b": 2})
        right = FrozenDictSlot({"a": 1, "b": 2})
        self.assertTrue(left == right)

    def test_order_does_not_affect_equality(self: Self, /) -> None:
        left: FrozenDictSlot[Any, Any]
        right: FrozenDictSlot[Any, Any]
        left = FrozenDictSlot({"a": 1, "b": 2})
        right = FrozenDictSlot({"b": 2, "a": 1})
        self.assertTrue(left == right)

    def test_equal_plain_dictionary(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({"a": 1})
        self.assertTrue(value == {"a": 1})

    def test_different_value_is_not_equal(self: Self, /) -> None:
        left: FrozenDictSlot[Any, Any]
        right: FrozenDictSlot[Any, Any]
        left = FrozenDictSlot({"a": 1})
        right = FrozenDictSlot({"a": 2})
        self.assertFalse(left == right)


class TestOperatorInequality(unittest.TestCase):
    def test_different_values(self: Self, /) -> None:
        left: FrozenDictSlot[Any, Any]
        right: FrozenDictSlot[Any, Any]
        left = FrozenDictSlot({"a": 1})
        right = FrozenDictSlot({"a": 2})
        self.assertTrue(left != right)

    def test_different_keys(self: Self, /) -> None:
        left: FrozenDictSlot[Any, Any]
        right: FrozenDictSlot[Any, Any]
        left = FrozenDictSlot({"a": 1})
        right = FrozenDictSlot({"b": 1})
        self.assertTrue(left != right)

    def test_different_lengths(self: Self, /) -> None:
        left: FrozenDictSlot[Any, Any]
        right: FrozenDictSlot[Any, Any]
        left = FrozenDictSlot({"a": 1})
        right = FrozenDictSlot({"a": 1, "b": 2})
        self.assertTrue(left != right)

    def test_equal_plain_dictionary(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({"a": 1})
        self.assertFalse(value != {"a": 1})


class TestOperatorLength(unittest.TestCase):
    def test_empty_mapping(self: Self, /) -> None:
        self.assertEqual(len(FrozenDictSlot({})), 0)

    def test_one_item(self: Self, /) -> None:
        self.assertEqual(len(FrozenDictSlot[str, int]({"a": 1})), 1)

    def test_multiple_items(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({"a": 1, "b": 2, "c": 3, "d": 4})
        self.assertEqual(len(value), 4)

    def test_nested_mapping_counts_as_one_value(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({"nested": {"a": 1, "b": 2}})
        self.assertEqual(len(value), 1)


class TestOperatorTruth(unittest.TestCase):
    def test_empty_mapping_is_false(self: Self, /) -> None:
        self.assertFalse(bool(FrozenDictSlot({})))

    def test_mapping_with_zero_value_is_true(self: Self, /) -> None:
        self.assertTrue(bool(FrozenDictSlot[str, int]({"a": 0})))

    def test_mapping_with_none_value_is_true(self: Self, /) -> None:
        self.assertTrue(bool(FrozenDictSlot[str, None]({"a": None})))

    def test_mapping_with_multiple_items_is_true(self: Self, /) -> None:
        self.assertTrue(bool(FrozenDictSlot[str, int]({"a": 1, "b": 2})))


class TestOperatorIteration(unittest.TestCase):
    def test_iterates_over_keys(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({"a": 1, "b": 2})
        self.assertEqual(list(iter(value)), ["a", "b"])

    def test_empty_iteration(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({})
        self.assertEqual(list(iter(value)), [])

    def test_preserves_insertion_order(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({"third": 3, "first": 1, "second": 2})
        self.assertEqual(list(iter(value)), ["third", "first", "second"])

    def test_supports_non_string_keys(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({1: "one", (2, 3): "tuple"})
        self.assertEqual(list(iter(value)), [1, (2, 3)])


class TestOperatorReversed(unittest.TestCase):
    def test_reverses_key_order(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({"a": 1, "b": 2, "c": 3})
        self.assertEqual(list(reversed(value)), ["c", "b", "a"])

    def test_empty_mapping(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({})
        self.assertEqual(list(reversed(value)), [])

    def test_single_item(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({"a": 1})
        self.assertEqual(list(reversed(value)), ["a"])

    def test_supports_non_string_keys(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({1: "one", (2, 3): "tuple"})
        self.assertEqual(list(reversed(value)), [(2, 3), 1])


class TestOperatorMappingUnpack(unittest.TestCase):
    def test_unpack_empty_mapping(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({})
        self.assertEqual({**value}, {})

    def test_unpack_items(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({"a": 1, "b": 2})
        self.assertEqual({**value}, {"a": 1, "b": 2})

    def test_later_value_overrides_frozen_value(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({"a": 1})
        self.assertEqual({**value, "a": 2}, {"a": 2})

    def test_frozen_value_overrides_earlier_value(self: Self, /) -> None:
        value: FrozenDictSlot[Any, Any]
        value = FrozenDictSlot({"a": 2})
        self.assertEqual({"a": 1, **value}, {"a": 2})


class TestOperatorAssignment(unittest.TestCase):
    def test_cannot_replace_existing_string_key(self: Self, /) -> None:
        value: FrozenDictSlot[str, int]
        value = FrozenDictSlot({"a": 1})
        with self.assertRaises(TypeError):
            value["a"] = 2  # type: ignore[index]

    def test_cannot_add_new_string_key(self: Self, /) -> None:
        value: FrozenDictSlot[str, int]
        value = FrozenDictSlot({"a": 1})
        with self.assertRaises(TypeError):
            value["b"] = 2  # type: ignore[index]

    def test_cannot_replace_integer_key(self: Self, /) -> None:
        value: FrozenDictSlot[int, str]
        value = FrozenDictSlot({1: "one"})
        with self.assertRaises(TypeError):
            value[1] = "changed"  # type: ignore[index]

    def test_failed_assignment_leaves_mapping_unchanged(self: Self, /) -> None:
        value: FrozenDictSlot[str, int]
        value = FrozenDictSlot({"a": 1})
        with self.assertRaises(TypeError):
            value["a"] = 99  # type: ignore[index]
        self.assertEqual(value, {"a": 1})


class TestOperatorDeletion(unittest.TestCase):
    def test_cannot_delete_existing_string_key(self: Self, /) -> None:
        value: FrozenDictSlot[str, int]
        value = FrozenDictSlot({"a": 1})
        with self.assertRaises(TypeError):
            del value["a"]  # type: ignore[attr-defined]

    def test_cannot_delete_missing_string_key(self: Self, /) -> None:
        value: FrozenDictSlot[str, int]
        value = FrozenDictSlot({"a": 1})
        with self.assertRaises(TypeError):
            del value["missing"]  # type: ignore[attr-defined]

    def test_cannot_delete_integer_key(self: Self, /) -> None:
        value: FrozenDictSlot[int, str]
        value = FrozenDictSlot({1: "one"})
        with self.assertRaises(TypeError):
            del value[1]  # type: ignore[attr-defined]

    def test_failed_deletion_leaves_mapping_unchanged(self: Self, /) -> None:
        value: FrozenDictSlot[str, int]
        value = FrozenDictSlot({"a": 1, "b": 2})
        with self.assertRaises(TypeError):
            del value["a"]  # type: ignore[attr-defined]
        self.assertEqual(value, {"a": 1, "b": 2})


if __name__ == "__main__":
    unittest.main()
