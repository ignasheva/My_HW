import os

import pytest

from homework4.task1 import function_opens_a_file


@pytest.fixture()
def create_and_remove_text_file():
    with open("test.txt", "x") as t:
        t.close()
    yield t
    os.remove("test.txt")


def test_to_check_if_file_exists(create_and_remove_text_file):
    assert os.path.exists("test.txt") == True


def test_positive_case_if_number_in_an_interval(create_and_remove_text_file):
    with open("test.txt", "w+") as t:
        t.write("2\n2\n3\n")
        t.close()
    assert function_opens_a_file("test.txt") == True


def test_negative_case_if_number_not_in_an_interval(create_and_remove_text_file):
    with open("test.txt", "w+") as t:
        t.write("5\n2\n3\n")
        t.close()
    assert function_opens_a_file("test.txt") == False


def test_if_item_is_not_digit(create_and_remove_text_file):
    with open("test.txt", "w+") as t:
        t.write("r\n2\n3\n")
        t.close()
    assert function_opens_a_file("test.txt") == "Could not convert data to an integer"
