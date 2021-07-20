import pytest

from homework5.task1 import Student, Teacher


@pytest.fixture()
def initialise_active_homework():
    teacher = Teacher("Oleg", "Petrov")
    new_homework = teacher.create_homework("New task about something", 7)
    return new_homework


def test_homework_is_active(initialise_active_homework):
    assert initialise_active_homework.is_active() is True


@pytest.fixture()
def initialise_inactive_homework():
    teacher = Teacher("Oleg", "Petrov")
    new_homework = teacher.create_homework("New task about something", 0)
    return new_homework


def test_homework_is_not_active(initialise_inactive_homework):
    assert initialise_inactive_homework.is_active() is False


@pytest.fixture()
def initialise_student():
    student = Student("Ivan", "Ivanov")
    return student


def test_student_does_active_homework(initialise_student, initialise_active_homework):
    assert (
        initialise_student.do_homework(initialise_active_homework)
        == initialise_active_homework
    )


def test_student_doesnt_do_inactive_homework(
    initialise_student, initialise_inactive_homework
):
    assert initialise_student.do_homework(initialise_inactive_homework) is None
