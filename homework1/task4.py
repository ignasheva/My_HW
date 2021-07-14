import itertools
from collections import Counter
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    return len(
        [
            Counter(combination)
            for combination in itertools.product(a, b, c, d)
            if sum(combination) == 0
        ]
    )
