import json

import pytest

from homework2.task3 import combinations


@pytest.fixture()
def get_data():
    with open("tests/homework2/data_for_test_task3.json") as file:
        data = json.loads(file.read())
    return data


def test_lists_with_different_lengths(get_data):
    for d in get_data:
        assert combinations(*d[0]) == d[1]
