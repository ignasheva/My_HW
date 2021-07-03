import pytest

from homework2.task3 import combinations


def test_2_lists_with_2_items():
    assert combinations([1, 2], [3, 4]) == [
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
    ]


def test_3_lists_with_different_lengths():
    assert combinations([1, 2, 3], [4, 5], [6]) == [
        [1, 4, 6],
        [1, 5, 6],
        [2, 4, 6],
        [2, 5, 6],
        [3, 4, 6],
        [3, 5, 6],
    ]
