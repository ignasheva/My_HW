from typing import Generator


def fizz_buzz(n: int) -> Generator[str, None, None]:
    f = lambda num: "fizz" * (num % 3 == 0) + "buzz" * (num % 5 == 0) or str(num)
    yield list(f(num) for num in range(1, n + 1))


def generator(n):
    for g in fizz_buzz(n):
        return g
