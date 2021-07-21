import json

import pytest

from homework7.task3 import tic_tac_toe_checker


@pytest.fixture()
def get_data():
    with open("tests/homework7/data_for_test_task3.json") as file:
        data = json.loads(file.read())
    return data


def test_1(get_data):
    for d in get_data:
        assert tic_tac_toe_checker(d["board"]) == d["result"]
