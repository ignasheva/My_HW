from string import ascii_lowercase

import pytest

from homework2.task5 import custom_range


def test_func_accept_string_args():
    expected = ["p", "n", "l", "j", "h"]
    assert custom_range(ascii_lowercase, "p", "g", -2) == expected


def test_func_accept_int_args():
    assert custom_range([1, 2, 3, 4], 1, 3) == [2, 3]
