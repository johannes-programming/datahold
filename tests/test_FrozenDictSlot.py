import unittest
from collections import abc
from typing import Any, Self

from datahold import FrozenDictSlot


class TestFromKeysMethod(unittest.TestCase):
    def test_fromkeys_uses_none_by_default(self: Self) -> None:
        result: Any = FrozenDictSlot.fromkeys(["a", "b", "c"])

        self.assertEqual(result, {"a": None, "b": None, "c": None})

    def test_fromkeys_uses_provided_value(self: Self) -> None:
        result: Any = FrozenDictSlot.fromkeys(["a", "b"], 10)

        self.assertEqual(result, {"a": 10, "b": 10})

    def test_fromkeys_uses_same_value_object_for_every_key(self: Self) -> None:
        value: Any = []
        result: Any = FrozenDictSlot.fromkeys(["a", "b"], value)

        self.assertIs(result["a"], value)
        self.assertIs(result["b"], value)

    def test_fromkeys_removes_duplicate_keys(self: Self) -> None:
        result: Any = FrozenDictSlot.fromkeys(
            ["a", "b", "a", "c", "b"],
            1,
        )

        self.assertEqual(list(result.keys()), ["a", "b", "c"])
        self.assertEqual(result, {"a": 1, "b": 1, "c": 1})

    def test_fromkeys_accepts_generator(self: Self) -> None:
        keys: Any = (str(number) for number in range(3))
        result: Any = FrozenDictSlot.fromkeys(keys, "value")

        self.assertEqual(
            result,
            {"0": "value", "1": "value", "2": "value"},
        )

    def test_fromkeys_accepts_empty_iterable(self: Self) -> None:
        self.assertEqual(FrozenDictSlot.fromkeys([], 1), {})

    def test_fromkeys_returns_frozen_dict_slot(self: Self) -> None:
        result: Any = FrozenDictSlot.fromkeys(["a"], 1)

        self.assertIsInstance(result, FrozenDictSlot)

    def test_fromkeys_rejects_unhashable_keys(self: Self) -> None:
        with self.assertRaises(TypeError):
            FrozenDictSlot.fromkeys([["unhashable"]], 1)  # type: ignore


class TestGetMethod(unittest.TestCase):
    def test_get_returns_existing_value(self: Self) -> None:
        mapping: Any = FrozenDictSlot({"a": 1, "b": 2})

        self.assertEqual(mapping.get("a"), 1)

    def test_get_returns_none_for_missing_key(self: Self) -> None:
        mapping: Any = FrozenDictSlot({"a": 1})

        self.assertIsNone(mapping.get("missing"))

    def test_get_returns_default_for_missing_key(self: Self) -> None:
        mapping: Any = FrozenDictSlot({"a": 1})

        self.assertEqual(mapping.get("missing", 20), 20)

    def test_get_returns_existing_value_instead_of_default(self: Self) -> None:
        mapping: Any = FrozenDictSlot({"a": 1})

        self.assertEqual(mapping.get("a", 20), 1)

    def test_get_returns_exact_default_object(self: Self) -> None:
        default: Any = []
        mapping: Any = FrozenDictSlot()

        self.assertIs(mapping.get("missing", default), default)

    def test_get_accepts_different_hashable_key_types(self: Self) -> None:
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

    def test_get_rejects_unhashable_key(self: Self) -> None:
        self.assertIsNone(FrozenDictSlot().get([]))

    def test_get_rejects_too_many_arguments(self: Self) -> None:
        with self.assertRaises(TypeError):
            FrozenDictSlot().get("a", 1, 2)  # type: ignore[call-overload]


class TestItemsMethod(unittest.TestCase):
    def test_items_contains_all_key_value_pairs(self: Self) -> None:
        mapping: Any = FrozenDictSlot({"a": 1, "b": 2})

        self.assertEqual(
            set(mapping.items()),
            {("a", 1), ("b", 2)},
        )

    def test_items_of_empty_mapping_is_empty(self: Self) -> None:
        self.assertEqual(list(FrozenDictSlot().items()), [])

    def test_items_preserves_insertion_order(self: Self) -> None:
        mapping: Any = FrozenDictSlot(
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

    def test_items_supports_membership_testing(self: Self) -> None:
        items: Any = FrozenDictSlot({"a": 1, "b": 2}).items()

        self.assertIn(("a", 1), items)
        self.assertNotIn(("a", 2), items)

    def test_items_has_correct_length(self: Self) -> None:
        items: Any = FrozenDictSlot(
            {
                "a": 1,
                "b": 2,
                "c": 3,
            }
        ).items()

        self.assertEqual(len(items), 3)

    def test_items_can_be_iterated_multiple_times(self: Self) -> None:
        items: Any = FrozenDictSlot({"a": 1, "b": 2}).items()

        self.assertEqual(list(items), [("a", 1), ("b", 2)])
        self.assertEqual(list(items), [("a", 1), ("b", 2)])

    def test_items_rejects_arguments(self: Self) -> None:
        with self.assertRaises(TypeError):
            FrozenDictSlot({"a": 1}).items("unexpected")  # type: ignore[call-arg]


class TestKeysMethod(unittest.TestCase):
    def test_keys_contains_all_keys(self: Self) -> None:
        mapping: Any = FrozenDictSlot({"a": 1, "b": 2, "c": 3})

        self.assertEqual(set(mapping.keys()), {"a", "b", "c"})

    def test_keys_of_empty_mapping_is_empty(self: Self) -> None:
        self.assertEqual(list(FrozenDictSlot().keys()), [])

    def test_keys_preserves_insertion_order(self: Self) -> None:
        mapping: Any = FrozenDictSlot(
            [
                ("third", 3),
                ("first", 1),
                ("second", 2),
            ]
        )

        self.assertEqual(
            list(mapping.keys()),
            ["third", "first", "second"],
        )

    def test_keys_supports_membership_testing(self: Self) -> None:
        keys: Any = FrozenDictSlot({"a": 1, "b": 2}).keys()

        self.assertIn("a", keys)
        self.assertNotIn("missing", keys)

    def test_keys_has_correct_length(self: Self) -> None:
        keys: Any = FrozenDictSlot(
            {
                "a": 1,
                "b": 2,
                "c": 3,
            }
        ).keys()

        self.assertEqual(len(keys), 3)

    def test_keys_supports_set_operations(self: Self) -> None:
        keys: Any = FrozenDictSlot({"a": 1, "b": 2}).keys()

        self.assertEqual(keys & {"b", "c"}, {"b"})
        self.assertEqual(keys | {"c"}, {"a", "b", "c"})

    def test_keys_rejects_arguments(self: Self) -> None:
        with self.assertRaises(TypeError):
            FrozenDictSlot({"a": 1}).keys("unexpected")  # type: ignore[call-arg]


class TestValuesMethod(unittest.TestCase):
    def test_values_contains_all_values(self: Self) -> None:
        mapping: Any = FrozenDictSlot({"a": 1, "b": 2, "c": 3})

        self.assertEqual(list(mapping.values()), [1, 2, 3])

    def test_values_of_empty_mapping_is_empty(self: Self) -> None:
        self.assertEqual(list(FrozenDictSlot().values()), [])

    def test_values_preserves_insertion_order(self: Self) -> None:
        mapping: Any = FrozenDictSlot(
            [
                ("third", 3),
                ("first", 1),
                ("second", 2),
            ]
        )

        self.assertEqual(list(mapping.values()), [3, 1, 2])

    def test_values_preserves_duplicates(self: Self) -> None:
        mapping: Any = FrozenDictSlot(
            {
                "a": 1,
                "b": 1,
                "c": 2,
            }
        )

        self.assertEqual(list(mapping.values()), [1, 1, 2])

    def test_values_supports_membership_testing(self: Self) -> None:
        values: Any = FrozenDictSlot({"a": 1, "b": 2}).values()

        self.assertIn(1, values)
        self.assertNotIn(3, values)

    def test_values_has_correct_length(self: Self) -> None:
        values: Any = FrozenDictSlot(
            {
                "a": 1,
                "b": 2,
                "c": 3,
            }
        ).values()

        self.assertEqual(len(values), 3)

    def test_values_can_be_iterated_multiple_times(self: Self) -> None:
        values: Any = FrozenDictSlot({"a": 1, "b": 2}).values()

        self.assertEqual(list(values), [1, 2])
        self.assertEqual(list(values), [1, 2])

    def test_values_rejects_arguments(self: Self) -> None:
        with self.assertRaises(TypeError):
            FrozenDictSlot({"a": 1}).values("unexpected")  # type: ignore[call-arg]


if __name__ == "__main__":
    unittest.main()
