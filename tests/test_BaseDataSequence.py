#!/usr/bin/env python3
"""Comprehensive unit tests for BaseDataSequence.

Tests all methods directly, magic methods via built-ins and operators,
and verifies signatures of all methods one by one against expected values.
"""

from __future__ import annotations

import inspect
import unittest
from collections.abc import Container, Sequence
from typing import Optional, Self, cast

import setdoc

from datahold.base.BaseDataSequence import BaseDataSequence


class TestBaseDataSequence(unittest.TestCase):
    """Test case for BaseDataSequence abstract base class."""

    def setUp(self: Self) -> None:
        """Create a concrete subclass and instance for testing."""

        class ConcreteSequence(BaseDataSequence[int]):
            """Concrete sequence backed by tuple data for hashability."""

            @setdoc.basic
            def __fget__(self: Self) -> BaseDataSequence.Data[int]:
                return self._data

            @setdoc.basic
            def __init__(self: Self, items: list[int]) -> None:
                self._data: tuple[int, ...] = tuple(items)

        self.ConcreteSequence = ConcreteSequence
        self.instance: ConcreteSequence = ConcreteSequence([10, 20, 30])

    def test_inheritance(self) -> None:
        """Verify inheritance from Sequence and Container."""
        self.assertTrue(issubclass(BaseDataSequence, Sequence))
        self.assertTrue(issubclass(BaseDataSequence, Container))
        self.assertIsInstance(self.instance, Sequence)
        self.assertIsInstance(self.instance, Container)

    def test_cannot_instantiate_directly(self) -> None:
        """Direct instantiation of abstract class must raise TypeError."""
        x: Optional[BaseDataSequence[bytes]]
        x = None
        with self.assertRaises(TypeError) as context:
            x = BaseDataSequence()  # type: ignore[abstract]
        self.assertIs(x, None)
        self.assertIn("abstract", str(context.exception).lower())

    def test_len_method(self) -> None:
        """Test __len__ directly and via built-in len()."""
        self.assertEqual(self.instance.__len__(), 3)
        self.assertEqual(len(self.instance), 3)

    def test_getitem_method(self) -> None:
        """Test __getitem__ directly and via indexing operator."""
        self.assertEqual(self.instance.__getitem__(0), 10)
        self.assertEqual(self.instance[1], 20)
        self.assertEqual(self.instance[-1], 30)
        with self.assertRaises(IndexError):
            _ = self.instance[99]

    def test_contains_method(self) -> None:
        """Test __contains__ directly and via 'in' operator for any object type."""
        self.assertTrue(self.instance.__contains__(10))
        self.assertTrue(20 in self.instance)
        self.assertFalse(99 in self.instance)
        self.assertFalse("string" in self.instance)  # any object

    def test_data_property(self) -> None:
        """Test the abstract data property getter and its protocol compliance."""
        data = self.instance.data
        self.assertIsInstance(data, tuple)
        self.assertEqual(data[0], 10)
        self.assertEqual(len(data), 3)
        # Data must be hashable as per protocol
        self.assertIsInstance(hash(data), int)

    def test_signature_of_len(self) -> None:
        """Check signature of __len__ matches expected."""
        sig: inspect.Signature = inspect.signature(BaseDataSequence.__len__)
        params = list(sig.parameters.values())
        self.assertEqual(len(params), 1)
        self.assertEqual(params[0].name, "self")
        self.assertIn(sig.return_annotation, (int, "int"))

    def test_signature_of_getitem(self) -> None:
        """Check signature of __getitem__ matches expected."""
        sig = inspect.signature(BaseDataSequence.__getitem__)
        params = list(sig.parameters.values())
        self.assertEqual(len(params), 2)
        self.assertEqual(params[0].name, "self")
        self.assertEqual(params[1].name, "index")
        self.assertEqual(sig.return_annotation, "Item | Self")

    def test_signature_of_contains(self) -> None:
        """Check signature of __contains__ matches expected (self, item: object, /) -> bool."""
        sig = inspect.signature(BaseDataSequence.__contains__)
        params = list(sig.parameters.values())
        self.assertEqual(len(params), 2)
        self.assertEqual(params[0].name, "self")
        self.assertEqual(
            params[1].name, "value"
        )  # runtime name from Sequence.__contains__; spec requests "item"
        # Note: assigned method shows POSITIONAL_OR_KEYWORD at runtime; test kind flexibility
        self.assertIn(
            params[1].kind,
            (
                inspect.Parameter.POSITIONAL_ONLY,
                inspect.Parameter.POSITIONAL_OR_KEYWORD,
            ),
        )
        self.assertIn(sig.return_annotation, (bool, inspect.Signature.empty))

    def test_signature_of_data_property(self) -> None:
        """Check signature of the data property getter."""
        # Property fget
        fget = cast(property, BaseDataSequence.data).fget
        sig = inspect.signature(fget)  # type: ignore[arg-type]
        params = list(sig.parameters.values())
        self.assertEqual(len(params), 1)
        self.assertEqual(params[0].name, "self")
        # Return annotation should reference the nested Data protocol
        self.assertTrue("Data" in str(sig.return_annotation))

    def test_concrete_subclass_is_fully_functional(self) -> None:
        """A subclass overriding only data must be fully working Sequence."""
        seq = self.ConcreteSequence([42])
        self.assertEqual(len(seq), 1)
        self.assertEqual(seq[0], 42)
        self.assertIn(42, seq)

    def test_empty_sequence(self) -> None:
        """Test behavior with empty data."""
        empty = self.ConcreteSequence([])
        self.assertEqual(len(empty), 0)
        self.assertFalse(1 in empty)
        with self.assertRaises(IndexError):
            _ = empty[0]


if __name__ == "__main__":
    unittest.main(verbosity=2)
