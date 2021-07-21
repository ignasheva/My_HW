from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    count = 0
    for key, value in tree.items():
        if isinstance(value, dict):
            count += find_occurrences(value, element)
        elif isinstance(value, (tuple, list, set)):
            count += find_occurrences(dict(enumerate(value)), element)
        elif value == element:
            count += 1
    return count
