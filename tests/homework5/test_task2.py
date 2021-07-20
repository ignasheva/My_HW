import pytest

from homework5.task2 import custom_sum


@pytest.fixture()
def doc():
    return """This function can sum any objects which have __add___"""


@pytest.fixture()
def name():
    return "custom_sum"


def test_custom_sum_documentation(doc):
    assert custom_sum.__doc__ == doc


def test_custom_sum_name(name):
    assert custom_sum.__name__ == name


def test_custom_sum_is_working():
    assert custom_sum(1, 3) == 4


def test_original_func_returns_wrapped_func(name):
    assert custom_sum.__original_func.__name__ == name
