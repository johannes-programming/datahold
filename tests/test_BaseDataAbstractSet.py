from __future__ import annotations

"""Comprehensive unit tests for BaseDataAbstractSet.

Tests all methods directly, magic methods via built-ins and operators,
and verifies signatures of all methods one by one against expected values.
"""

import inspect
import unittest
from collections.abc import Container, Set
from typing import Optional, Self, cast

import setdoc

from datahold.base.BaseDataAbstractSet import BaseDataAbstractSet


class TestBaseDataAbstractSet(unittest.TestCase):
    """Test case for BaseDataAbstractSet abstract base class."""

    def setUp(self) -> None:
        """Create a concrete subclass and instance for testing."""

        class ConcreteSet(BaseDataAbstractSet[int]):
            """Concrete set backed by frozenset data for hashability."""

            @setdoc.basic
            def __fget__(self: Self) -> BaseDataAbstractSet.Data[int]:
                return self._data

            @setdoc.basic
            def __init__(self: Self, items: list[int]) -> None:
                self._data: frozenset[int] = frozenset(items)

        self.ConcreteSet = ConcreteSet
        self.instance: ConcreteSet = ConcreteSet([10, 20, 30])

    def test_inheritance(self) -> None:
        """Verify inheritance from Set and Container."""
        self.assertTrue(issubclass(BaseDataAbstractSet, Set))
        self.assertTrue(issubclass(BaseDataAbstractSet, Container))
        self.assertIsInstance(self.instance, Set)
        self.assertIsInstance(self.instance, Container)

    def test_cannot_instantiate_directly(self) -> None:
        """Direct instantiation of abstract class must raise TypeError."""
        x: Optional[BaseDataAbstractSet[bytes]]
        x = None
        with self.assertRaises(TypeError) as context:
            x = BaseDataAbstractSet()  # type: ignore[abstract]
        self.assertIs(x, None)
        self.assertIn("abstract", str(context.exception).lower())

    def test_len_method(self) -> None:
        """Test __len__ directly and via built-in len()."""
        self.assertEqual(self.instance.__len__(), 3)
        self.assertEqual(len(self.instance), 3)

    def test_iter_method(self) -> None:
        """Test __iter__ directly and via iter() and set() conversion."""
        self.assertEqual(set(self.instance.__iter__()), {10, 20, 30})
        self.assertEqual(set(iter(self.instance)), {10, 20, 30})

    def test_contains_method(self) -> None:
        """Test __contains__ directly and via 'in' operator for any object type."""
        self.assertTrue(self.instance.__contains__(10))
        self.assertTrue(20 in self.instance)
        self.assertFalse(99 in self.instance)
        self.assertFalse("string" in self.instance)  # any object

    def test_data_property(self) -> None:
        """Test the abstract data property getter and its protocol compliance."""
        data = self.instance.data
        self.assertIsInstance(data, frozenset)
        self.assertEqual(len(data), 3)
        # Data must be hashable as per protocol
        self.assertIsInstance(hash(data), int)

    def test_signature_of_len(self) -> None:
        """Check signature of __len__ matches expected."""
        sig: inspect.Signature = inspect.signature(BaseDataAbstractSet.__len__)
        params = list(sig.parameters.values())
        self.assertEqual(len(params), 1)
        self.assertEqual(params[0].name, "self")
        self.assertIn(sig.return_annotation, (int, "int"))

    def test_signature_of_iter(self) -> None:
        """Check signature of __iter__ matches expected."""
        sig = inspect.signature(BaseDataAbstractSet.__iter__)
        params = list(sig.parameters.values())
        self.assertEqual(len(params), 1)
        self.assertEqual(params[0].name, "self")
        self.assertTrue("Iterator" in str(sig.return_annotation))

    def test_signature_of_contains(self) -> None:
        """Check signature of __contains__ matches expected (self, other: object) -> bool."""
        sig = inspect.signature(BaseDataAbstractSet.__contains__)
        params = list(sig.parameters.values())
        self.assertEqual(len(params), 2)
        self.assertEqual(params[0].name, "self")
        self.assertEqual(params[1].name, "other")
        self.assertIn(
            params[1].kind,
            (
                inspect.Parameter.POSITIONAL_ONLY,
                inspect.Parameter.POSITIONAL_OR_KEYWORD,
            ),
        )
        self.assertIn(
            sig.return_annotation, ("bool", bool, inspect.Signature.empty)
        )

    def test_signature_of_data_property(self) -> None:
        """Check signature of the data property getter."""
        fget = cast(property, BaseDataAbstractSet.data).fget
        sig = inspect.signature(fget)  # type: ignore[arg-type]
        params = list(sig.parameters.values())
        self.assertEqual(len(params), 1)
        self.assertEqual(params[0].name, "self")
        self.assertTrue("Data" in str(sig.return_annotation))

    def test_concrete_subclass_is_fully_functional(self) -> None:
        """A subclass overriding only data must be fully working Set."""
        s = self.ConcreteSet([42])
        self.assertEqual(len(s), 1)
        self.assertIn(42, s)
        self.assertEqual(set(s), {42})

    def test_empty_set(self) -> None:
        """Test behavior with empty data."""
        empty = self.ConcreteSet([])
        self.assertEqual(len(empty), 0)
        self.assertFalse(1 in empty)
        self.assertEqual(set(empty), set())


if __name__ == "__main__":
    unittest.main(verbosity=2)
