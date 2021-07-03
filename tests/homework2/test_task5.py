import string

import pytest

from homework2.task5 import custom_range


def test_func_accept_string_args():
    assert custom_range(string.ascii_lowercase, "p", "g", -2) == [
        "p",
        "n",
        "l",
        "j",
        "h",
    ]


def test_func_accept_int_args():
    assert custom_range(custom_range([1, 2, 3, 4], 1, 3)) == [2, 3]
