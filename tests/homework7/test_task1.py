import json

import pytest

from homework7.task1 import find_occurrences


@pytest.fixture()
def get_data():
    with open("tests/homework7/example_tree.json") as file:
        data = json.loads(file.read())
    return data


def test_find_red_occurrences(get_data):
    assert find_occurrences(get_data, "RED") == 6


def test_find_blue_occurrences(get_data):
    assert find_occurrences(get_data, "BLUE") == 2
