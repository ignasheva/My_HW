from typing import Sequence, Generator


def is_fib(start: int) -> Generator[int, None, None]:
    fib1, fib2 = 0, 1
    while True:
        if fib1 >= start:
            yield fib1
        fib1, fib2 = fib2, fib1 + fib2


def check_fibonacci(data: Sequence[int]) -> bool:
    if data[0] == 1 and data[1] == 2:
        data.insert(0, 1)
    for value, fib in zip(data, is_fib(data[0])):
        if value != fib:
            return False
    return True
