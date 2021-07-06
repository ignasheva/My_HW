import pytest
from homework3.task1 import cache


def test_cache_is_working():
    times_called = 0

    @cache(times=3)
    def func(a, b):
        nonlocal times_called
        times_called += 1
        return (a ** b) ** 2

    assert func(2, 2) == 16
    assert times_called == 1

    assert func(2, 2) == 16
    assert times_called == 1
