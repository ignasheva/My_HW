import json

import pytest

from homework1.task5 import find_maximal_sub_array_sum


@pytest.fixture()
def get_data():
    with open("data_for_test_task5.json") as file:
        data = json.loads(file.read())
    return data


def test_maximal_sub_array_sum_with_length_less_equal_to_k(get_data):
    for d in get_data:
        assert find_maximal_sub_array_sum(d[0], d[1]) == d[2]
