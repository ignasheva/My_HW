from typing import Dict, List, Tuple


def find_the_most_common_element(massive: Dict, inp: List) -> List:
    max_value = max(massive.values())
    major = (key for key in massive if massive[key] == max_value)
    return major if max_value > len(inp) // 2 else []


def find_the_least_common_element(massive: Dict) -> List:
    min_value = min(massive.values())
    minor = [key for key in massive if massive[key] == min_value]
    return minor


def major_and_minor_elem(inp: List[int]) -> Tuple[int, int]:
    massive = {}
    for i in range(len(inp)):
        massive[inp[i]] = massive.get(inp[i], 0) + 1
    major = find_the_most_common_element(massive, inp)
    minor = find_the_least_common_element(massive)
    return (*major, *minor)
