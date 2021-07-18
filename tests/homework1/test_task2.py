import pytest

from homework1.task2 import check_fibonacci


@pytest.mark.parametrize(
    "value",
    [[1, 1, 2, 3], [5, 8, 13, 21]],
)
def test_is_fib_sequence(value):
    assert check_fibonacci(value) is True


@pytest.fixture()
def fib_tuple():
    return (1, 1, 2, 3)


def test_check_fib_works_with_tuple(fib_tuple):
    assert check_fibonacci(fib_tuple) is True


@pytest.mark.parametrize(
    "value",
    [[3, 4, 7, 11]],
)
def test_is_not_fib_sequence(value):
    assert check_fibonacci(value) is False


def test_range_is_not_fib_sequence():
    assert check_fibonacci(range(1, 10)) is False
