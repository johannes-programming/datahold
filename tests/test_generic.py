from __future__ import annotations

__all__: list[str] = ["TestGeneric"]

import unittest
from typing import Any, Optional, Self

from Lazy import Lazy

import datahold


class TestGeneric(unittest.TestCase):
    def _test(self: Self, name: str, generic: Optional[int], /) -> None:
        datatype: type[Any]
        if generic is None:
            return
        datatype = getattr(datahold, name)
        if generic == 1:
            datatype[Any]
        elif generic:
            datatype[(Any,) * generic]
        else:
            with self.assertRaises(TypeError):
                datatype[Any]

    def test_generic(self: Self, /) -> None:
        data: Any
        name: str
        for name, data in Lazy.lazy.datatypes.items():
            with self.subTest(datatype=name):
                self._test(name, data.get("varia", {}).get("generic"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
