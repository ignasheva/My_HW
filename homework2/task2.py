from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    massive = {}
    for i in range(len(inp)):
        if inp[i] in massive:
            massive[inp[i]] += 1
        else:
            massive[inp[i]] = 1

    # find the most common element
    max_value = max(massive.values())
    max_keys = (k for k in massive if massive[k] == max_value)
    major = [j for j in max_keys if max_value > len(inp) // 2]

    # find the least common element
    min_value = min(massive.values())
    min_keys = [k for k in massive if massive[k] == min_value]
    minor = [j for j in min_keys]

    return (*major, *minor)
