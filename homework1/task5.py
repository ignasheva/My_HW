from typing import List


def find_maximal_sub_array_sum(nums: List[int], k: int) -> int:
    variants = []
    for i in range(len(nums) + 1):
        [variants.append(nums[j:i]) for j in range(i) if len(nums[j:i]) <= k]
    sum_array = []
    [sum_array.append(sum(i)) for i in variants]
    return max(sum_array)
