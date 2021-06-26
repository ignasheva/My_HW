import pytest
from homework1.task2 import check_fibonacci


def test_simple_fib_sequence():
    assert check_fibonacci([1, 1, 2, 3])


def test_hard_fib_sequence():
    assert check_fibonacci([5, 8, 13, 21])


def test_not_fib_sequence():
    assert check_fibonacci([3, 4, 7, 11])
