import json

import pytest

from homework1.task4 import check_sum_of_four


@pytest.fixture()
def get_data():
    with open("tests/homework1/data_for_test_task4.json") as file:
        data = json.loads(file.read())
    return data


def test_sum_of_four_lists_with_different_values(get_data):
    for d in get_data:
        assert check_sum_of_four(d[0], d[1], d[2], d[3]) == d[4]
