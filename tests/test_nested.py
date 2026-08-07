__all__: list[str] = ["TestNested"]

import unittest
from typing import Any, Self, TypeAliasType, get_origin

from Lazy import Lazy

import datahold


class TestNested(unittest.TestCase):

    def _test(
        self: Self, datatype: Any, nestedname: str, solutionname: str
    ) -> None:
        nested = getattr(datatype, nestedname, None)
        if isinstance(nested, TypeAliasType):
            answer = get_origin(nested.__value__)
        else:
            answer = nested
        solution = Lazy.get_import(solutionname)
        self.assertIs(answer, solution)

    def _test_datatype(self: Self, datatype: Any, /, **kwargs: Any) -> None:
        for x, y in kwargs.items():
            with self.subTest(nested=x, solution=y):
                self._test(datatype, nestedname=x, solutionname=y)

    def test_nested(self: Self, /) -> None:
        datatype: Any
        for typename, info in Lazy.lazy.datatypes.items():
            with self.subTest(typename=typename):
                datatype = getattr(datahold, typename)
                self._test_datatype(datatype, **info.get("nested", {}))
