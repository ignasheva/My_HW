import pytest

from homework6.task2 import HomeworkResult, Student, Teacher

teacher_1 = Teacher("Dmitry", "Petrov")
teacher_2 = Teacher("Andrey", "Popov")
student_1 = Student("Anton", "Ivanov")
student_2 = Student("Vadim", "Smirnov")

# Create homework
func_homework = teacher_1.create_homework("Learn new functions", 5)
oop_homework = teacher_2.create_homework("Learn smth new about oop", 3)
last_homework = teacher_2.create_homework("Great topic", 0)
# Student_1 do homework
result_1 = student_1.do_homework(func_homework, "I have done this hw")
result_2 = student_1.do_homework(oop_homework, "This is my solution")
# Student_2 do homework
result_3 = student_2.do_homework(func_homework, "Done")
result_4 = student_2.do_homework(oop_homework, "Completed")


def test_hw_done_correctly():
    assert teacher_1.check_homework(result_1) is True


def test_hw_done_wrong():
    assert teacher_1.check_homework(result_3) is False


def test_two_teachers_have_the_same_result_check_one_hw():
    temp_1 = teacher_1.homework_done[func_homework]
    temp_2 = teacher_2.homework_done[func_homework]
    assert temp_1 == temp_2


def test_raise_gave_not_hw_object():
    with pytest.raises(ValueError, match="You gave a not Homework object"):
        HomeworkResult(student_2, "fff", "Solution")


def test_hw_is_not_active():
    assert last_homework.is_active() is False


def test_number_of_completed_tasks():
    teacher_2.check_homework(result_2)
    teacher_2.check_homework(result_4)
    assert len(Teacher.homework_done[oop_homework]) == 2


def test_set_to_zero_hw_done():
    Teacher.reset_results()
    assert len(Teacher.homework_done) == 0
