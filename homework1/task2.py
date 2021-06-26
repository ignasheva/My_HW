from typing import Sequence


def _check_window(x: int, y: int, z: int) -> bool:
    return (x + y) == z


def is_fib(number):
    num1 = 1
    num2 = 0
    while True:
        if num2 <= number:
            if num2 == number:
                return True
            else:
                temp_num = num2
                num2 += num1
                num1 = temp_num
        else:
            return False


def check_fibonacci(data: Sequence[int]) -> bool:
    flag = True
    assert len(data) >= 3, 'Not enough values in sequence'
    a, b, c = data[0], data[1], data[2]
    while data and flag:
        if not _check_window(a, b, c):
            flag = False
            break
        for n in data:
            if not is_fib(n):
                flag = False
                break
            else:
                data = data[1:]
                if len(data) < 3:
                    if a + b == c:
                        flag = True
                        break
                    else:
                        flag = False
                        break
                a, b, c = b, c, data[2]
    return flag
