import pytest

from homework2.task4 import cache_func


def test_check_cache_func():
    some = 2, 3
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2
