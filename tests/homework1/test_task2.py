import pytest

from homework1.task2 import check_fibonacci


@pytest.mark.parametrize(
    "value",
    [[1, 1, 2, 3], [5, 8, 13, 21]],
)
def test_is_fib_sequence(value):
    assert check_fibonacci(value) is True


@pytest.mark.parametrize(
    "value",
    [[3, 4, 7, 11]],
)
def test_is_not_fib_sequence(value):
    assert check_fibonacci(value) is False
