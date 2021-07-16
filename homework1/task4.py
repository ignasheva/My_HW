from collections import Counter
from itertools import product
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    return len([Counter(comb) for comb in product(a, b, c, d) if sum(comb) == 0])
