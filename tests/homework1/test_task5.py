import pytest

from homework1.task5 import find_maximal_sub_array_sum


@pytest.mark.parametrize(
    "nums, k, result",
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([1, 3, -1, -3, 5, 0, -1, 15], 3, 15),
        ([-1, -13, -1, -3, -5, -3, -6, -7], 4, -1),
    ],
)
def test_maximal_sub_array_sum_with_length_less_equal_to_k(nums, k, result):
    assert find_maximal_sub_array_sum(nums, k) == result
