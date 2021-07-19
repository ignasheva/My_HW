from collections import defaultdict
from datetime import datetime, timedelta


class DeadlineError(Exception):
    pass


class Homework:
    def __init__(self, text: str, deadline: int):
        self.text = text
        self.deadline = timedelta(days=deadline)
        self.created = datetime.now()

    def is_active(self):
        return self.created + self.deadline > datetime.now()


class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class HomeworkResult:
    def __init__(self, author, homework, solution: str):
        if type(homework) is not Homework:
            raise ValueError("You gave a not Homework object")
        if type(author) is not Student:
            raise ValueError("You gave a not Student object")
        self.homework = homework
        self.author = author
        self.solution = solution
        self.created = datetime.now()


class Student(Person):
    def do_homework(self, homework: Homework, solution: str):
        if homework.is_active() is False:
            raise DeadlineError("You are late")
        return HomeworkResult(self, homework, solution)


class Teacher(Person):
    homework_done = defaultdict(list)

    @staticmethod
    def create_homework(text: str, deadline: int):
        return Homework(text, deadline)

    def check_homework(self, homework_result: HomeworkResult):
        if len(homework_result.solution) < 5:
            return False
        homework = homework_result.homework
        if Teacher.homework_done[homework].count(homework_result) == 0:
            Teacher.homework_done[homework].append(homework_result)
        return True

    @staticmethod
    def reset_results(homework: Homework = None):
        if homework is None:
            Teacher.homework_done.clear()
            return
        Teacher.homework_done.pop(homework)


if __name__ == "__main__":
    opp_teacher = Teacher("Daniil", "Shadrin")
    advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

    lazy_student = Student("Roman", "Petrov")
    good_student = Student("Lev", "Sokolov")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)

    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
    result_3 = lazy_student.do_homework(docs_hw, "done")
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print("There was an exception here")
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results(docs_hw)
