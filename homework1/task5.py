from typing import List


def find_maximal_sub_array_sum(nums: List[int], k: int) -> int:
    lists = [[]]
    for i in range(len(nums)+1):
        for j in range(i):
            lists.append(nums[j:i])

    total = 0
    for i in lists:
        if len(i) <= k:
            next = sum(i)
            if next > total:
                total = next
        else:
            continue
    return total
