# check_listlike_covariance.py

import unittest

from datahold import FrozenListLike, FrozenListSlot, ListLike


class Animal:
    pass


class Bear(Animal):
    pass


# Valid exactly when covariant:
def cast_ListLikeAnimal(
    x: ListLike[Bear],
) -> ListLike[Animal]:
    return x


def cast_FrozenListLikeAnimal(
    x: FrozenListLike[Bear],
) -> FrozenListLike[Animal]:
    return x


def cast_FrozenListSlotAnimal(
    x: FrozenListSlot[Bear],
) -> FrozenListSlot[Animal]:
    return x


if __name__ == "__main__":
    unittest.main(verbosity=2)
