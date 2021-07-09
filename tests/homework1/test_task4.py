import pytest

from homework1.task4 import check_sum_of_four


@pytest.mark.parametrize(
    "a, b, c, d, result_sum_of_four",
    [([-8, 4, 0], [2, 3, 1], [2, 7, -1], [4, 1, 0], 3)],
)
def test_check_sum_of_four_with_no_zero_result(a, b, c, d, result_sum_of_four):
    assert check_sum_of_four(a, b, c, d) == result_sum_of_four


@pytest.mark.parametrize(
    "a, b, c, d, result_sum_of_four",
    [
        ([8, 4], [2, 3], [2, 7], [4, 1], 0),
        ([-3, -4], [-5, -3], [-6, -2], [-4, -1], 0),
        ([], [], [], [], 0),
    ],
)
def test_check_sum_of_four_with_zero_result(a, b, c, d, result_sum_of_four):
    assert check_sum_of_four(a, b, c, d) == result_sum_of_four
