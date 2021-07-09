from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(file_name) as fi:
        data = fi.read().split()
    i = iter(data)
    num = list(iter(lambda: int(next(i)), None))
    return tuple((min(num), max(num)))
