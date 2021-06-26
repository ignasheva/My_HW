import pytest
from homework1.task3 import find_maximum_and_minimum


def test_check_work():
    assert find_maximum_and_minimum('homework1/some_file.txt')
