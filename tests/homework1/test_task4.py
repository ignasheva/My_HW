import pytest

from homework1.task4 import check_sum_of_four


def test_empty_lists():
    """Testing that actual empty lists give 0 tuples"""
    assert check_sum_of_four([], [], [], []) == 0


def test_only_positive_lists():
    """Testing that actual not empty lists
    with only positive numbers more than zero give 0 tuples"""
    assert check_sum_of_four([8, 4], [2, 3], [2, 7], [4, 1]) == 0


def test_only_negative_lists():
    """Testing that actual not empty lists
    with only negative numbers give 0 tuples"""
    assert (
        check_sum_of_four([-3, -4, -1], [-2, -5, -3], [-6, -2, -7], [-8, -4, -1]) == 0
    )


def test_lists_with_different_values():
    """Testing that actual not empty lists
    with positive and negative values given n tuples"""
    assert check_sum_of_four([-8, 4, 0], [2, 3, 1], [2, 7, -1], [4, 1, 0])
