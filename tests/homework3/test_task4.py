import pytest
from homework3.task4 import is_armstrong


def test_it_is_armstrong_number():
    assert is_armstrong(153) == True

def test_it_is_not_armstrong_number():
    assert is_armstrong(10) == False
