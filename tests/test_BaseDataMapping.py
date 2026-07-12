#!/usr/bin/env python3
"""Comprehensive unit tests for BaseDataMapping.

Tests all methods directly, magic methods via built-ins and operators,
and verifies signatures of all methods one by one against expected values.
"""

from __future__ import annotations

import inspect
import unittest
from collections.abc import Container, Mapping
from typing import Optional, Self, cast

from datahold.base.BaseDataMapping import BaseDataMapping


class TestBaseDataMapping(unittest.TestCase):
    """Test case for BaseDataMapping abstract base class."""

    def setUp(self) -> None:
        """Create a concrete subclass and instance for testing."""

        class HashableDict(dict):  # type: ignore[type-arg]
            """A dict subclass made hashable for Data protocol compliance."""

            def __hash__(self: Self) -> int:  # type: ignore[override]
                return hash(frozenset(self.items()))

        class ConcreteMapping(BaseDataMapping[str, int]):
            """Concrete mapping backed by HashableDict data for hashability."""

            def __init__(self, items: dict[str, int] | None = None) -> None:
                if items is None:
                    items = {}
                self._data: HashableDict = HashableDict(items)

            @property
            def data(self) -> BaseDataMapping.Data[str, int]:
                return self._data

        self.ConcreteMapping = ConcreteMapping
        self.instance: ConcreteMapping = ConcreteMapping(
            {"a": 10, "b": 20, "c": 30}
        )

    def test_inheritance(self) -> None:
        """Verify inheritance from Mapping and Container."""
        self.assertTrue(issubclass(BaseDataMapping, Mapping))
        self.assertTrue(issubclass(BaseDataMapping, Container))
        self.assertIsInstance(self.instance, Mapping)
        self.assertIsInstance(self.instance, Container)

    def test_cannot_instantiate_directly(self) -> None:
        """Direct instantiation of abstract class must raise TypeError."""
        x: Optional[BaseDataMapping[str, int]]
        x = None
        with self.assertRaises(TypeError) as context:
            x = BaseDataMapping()  # type: ignore[abstract]
        self.assertIs(x, None)
        self.assertIn("abstract", str(context.exception).lower())

    def test_len_method(self) -> None:
        """Test __len__ directly and via built-in len()."""
        self.assertEqual(self.instance.__len__(), 3)
        self.assertEqual(len(self.instance), 3)

    def test_getitem_method(self) -> None:
        """Test __getitem__ directly and via indexing operator."""
        self.assertEqual(self.instance.__getitem__("a"), 10)
        self.assertEqual(self.instance["b"], 20)
        with self.assertRaises(KeyError):
            _ = self.instance["missing"]

    def test_iter_method(self) -> None:
        """Test __iter__ directly and via iter() and dict() conversion."""
        self.assertEqual(set(self.instance.__iter__()), {"a", "b", "c"})
        self.assertEqual(set(iter(self.instance)), {"a", "b", "c"})
        self.assertEqual(dict(self.instance), {"a": 10, "b": 20, "c": 30})

    def test_contains_method(self) -> None:
        """Test __contains__ directly and via 'in' operator for any object type."""
        self.assertTrue("b" in self.instance)
        self.assertFalse("missing" in self.instance)
        self.assertFalse(99 in self.instance)  # type: ignore

    def test_data_property(self) -> None:
        """Test the abstract data property getter and its protocol compliance."""
        data = self.instance.data
        self.assertIsInstance(data, dict)
        self.assertEqual(data["a"], 10)
        self.assertEqual(len(data), 3)
        # Data must be hashable as per protocol
        self.assertIsInstance(hash(data), int)

    def test_signature_of_len(self) -> None:
        """Check signature of __len__ matches expected."""
        sig: inspect.Signature = inspect.signature(BaseDataMapping.__len__)
        params = list(sig.parameters.values())
        self.assertEqual(len(params), 1)
        self.assertEqual(params[0].name, "self")
        self.assertIn(sig.return_annotation, (int, "int"))

    def test_signature_of_getitem(self) -> None:
        """Check signature of __getitem__ matches expected."""
        sig = inspect.signature(BaseDataMapping.__getitem__)
        params = list(sig.parameters.values())
        self.assertEqual(len(params), 2)
        self.assertEqual(params[0].name, "self")
        self.assertEqual(params[1].name, "key")
        self.assertIn(
            sig.return_annotation,
            (
                int,
                "Value",
                inspect.Signature.empty,
            ),
        )

    def test_signature_of_iter(self) -> None:
        """Check signature of __iter__ matches expected."""
        sig = inspect.signature(BaseDataMapping.__iter__)
        params = list(sig.parameters.values())
        self.assertEqual(len(params), 1)
        self.assertEqual(params[0].name, "self")
        self.assertTrue(
            "Iterator" in str(sig.return_annotation)
            or "Iterable" in str(sig.return_annotation)
        )

    def test_signature_of_contains(self) -> None:
        """Check signature of __contains__ matches expected (self, key: Hashable) -> bool."""
        sig = inspect.signature(BaseDataMapping.__contains__)  # type: ignore
        params = list(sig.parameters.values())
        self.assertEqual(len(params), 2)
        self.assertEqual(params[0].name, "self")
        self.assertEqual(params[1].name, "key")
        self.assertIn(
            params[1].kind,
            (
                inspect.Parameter.POSITIONAL_ONLY,
                inspect.Parameter.POSITIONAL_OR_KEYWORD,
            ),
        )
        self.assertIn(
            sig.return_annotation, (bool, "bool", inspect.Signature.empty)
        )

    def test_signature_of_data_property(self) -> None:
        """Check signature of the data property getter."""
        fget = cast(property, BaseDataMapping.data).fget
        sig = inspect.signature(fget)  # type: ignore[arg-type]
        params = list(sig.parameters.values())
        self.assertEqual(len(params), 1)
        self.assertEqual(params[0].name, "self")
        self.assertTrue("Data" in str(sig.return_annotation))

    def test_concrete_subclass_is_fully_functional(self) -> None:
        """A subclass overriding only data must be fully working Mapping."""
        m = self.ConcreteMapping({"x": 99})
        self.assertEqual(len(m), 1)
        self.assertEqual(m["x"], 99)
        self.assertIn("x", m)
        self.assertEqual(dict(m), {"x": 99})

    def test_empty_mapping(self) -> None:
        """Test behavior with empty data."""
        empty = self.ConcreteMapping({})
        self.assertEqual(len(empty), 0)
        self.assertFalse("a" in empty)
        with self.assertRaises(KeyError):
            _ = empty["a"]
        self.assertEqual(dict(empty), {})


if __name__ == "__main__":
    unittest.main(verbosity=2)
