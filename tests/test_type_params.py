from __future__ import annotations

__all__: list[str] = ["TestTypeParams"]

import unittest
from typing import Any, Optional, Self

from Lazy import Lazy

import datahold


class TestTypeParams(unittest.TestCase):
    def _test_type_param(
        self: Self,
        param: Any,
        /,
        covariant: Optional[bool] = None,
        contravariant: Optional[bool] = None,
        **kwargs: Any,
    ) -> None:
        if covariant is not None:
            self.assertEqual(param.__covariant__, covariant)
        if contravariant is not None:
            self.assertEqual(param.__contravariant__, contravariant)

    def _test_type_params(
        self: Self, name: str, type_params: list[Any], /
    ) -> None:
        datatype: Any
        index: int
        datatype = getattr(datahold, name)
        index = 0
        for param, info in zip(
            datatype.__type_params__,
            type_params,
            strict=True,
        ):
            with self.subTest(index=index):
                self._test_type_param(param, **info)
            index += 1

    def test_type_params(self: Self, /) -> None:
        for name, data in Lazy.lazy.datatypes.items():
            if "type_params" not in data:
                continue
            with self.subTest(datatype=name):
                self._test_type_params(name, data["type_params"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
