import pytest
from homework1.task5 import find_maximal_sub_array_sum


def test_len_sub_equal_k():
    """Returns sub-array with max sum where len sub-array equal k'"""
    assert find_maximal_sub_array_sum(nums= [1, 3, -1, -3, 5, 3, 6, 7], k= 3)

def test_len_sub_less_k():
    """Returns sub-array with max sum where len sub-array less than k'"""
    assert find_maximal_sub_array_sum([1, 3, -1, -3, 5, 0, -1, 15], 3)

def test_sub_array_sum_zero():
    """Returns sub-array with zero sum when all numbers less or equal 0'"""
    assert find_maximal_sub_array_sum([-1, -13, -1, -3, -5, -3, -6, -7], 4) == 0