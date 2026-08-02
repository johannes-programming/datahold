import operator
import unittest
from typing import Any, Self

from Lazy import Lazy


class TestInternalComparsion(unittest.TestCase):
    def _test_typename(self: Self, typename: str, /, **kwargs: Any) -> None:
        for opername, info in kwargs.items():
            oper = getattr(operator, opername)
            with self.subTest(operator=opername):
                self._test_operator(typename, oper, **info)

    def _test_operator(self: Self, *args: Any, **kwargs: Any) -> None:
        for testname, testinfo in kwargs.items():
            with self.subTest(testname=testname):
                self._test_vars(*args, **testinfo)

    def _test_vars(
        self: Self,
        typename: str,
        oper: Any,
        /,
        *,
        a: str,
        b: str,
        valid: bool = True,
    ) -> None:
        example_a = Lazy.get_example(typename, a)
        example_b = Lazy.get_example(typename, b)
        builtin_a = Lazy.get_builtin_example(typename, a)
        builtin_b = Lazy.get_builtin_example(typename, b)
        if valid:
            answer = oper(example_a, example_b)
            solution = oper(builtin_a, builtin_b)
            self.assertEqual(answer, solution)
            return
        with self.assertRaises(Exception):
            answer = oper(example_a, example_b)
        with self.assertRaises(Exception):
            solution = oper(builtin_a, builtin_b)

    def test_internal_comparison(self: Self) -> None:
        for typename, info in Lazy.lazy.datatypes.items():
            with self.subTest(typename=typename):
                self._test_typename(
                    typename,
                    **info.get("TestInternalComparsion", {}),
                )
