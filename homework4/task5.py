from typing import Generator


def fizz_buzz(n: int) -> Generator[str, None, None]:
    yield [
        "fizz" * (not n % 3) + "buzz" * (not n % 5) or str(n) for n in range(1, n + 1)
    ]


def generator(n):
    for g in fizz_buzz(n):
        return g
