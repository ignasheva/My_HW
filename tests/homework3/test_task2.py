import pytest

from homework3.task2 import *


def test_time_calculate():
    assert faster_calculate(5) == 11261


def test_timer():
    assert timer() <= 60
