import pytest

from homework6.task1 import instances_counter


@instances_counter
class Person:
    pass


def test_get_created_instances_is_working():
    person, _ = Person(), Person()
    assert person.get_created_instances() == 2


def test_reset_instances_counter_is_working():
    person = Person()
    assert person.reset_instances_counter() == 3


def test_instances_counter_is_working():
    assert Person.get_created_instances() == 0
