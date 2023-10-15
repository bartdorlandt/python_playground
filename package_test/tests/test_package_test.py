"""test_package_test"""
from package_test import package_test
import pytest


@pytest.mark.parametrize(
    "number,expected",
    [
        (1, 2),
        (-5, -4),
        (0, 1),
    ],
)
def test_add_one(number: int, expected: int):
    add = package_test.add_one(number)
    assert add == expected
