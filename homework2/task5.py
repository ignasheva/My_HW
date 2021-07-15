from typing import List, Sequence


def custom_range(source: Sequence, *args: (int, str)) -> List:
    params = []
    for arg in args:
        params.append(source.find(arg) if type(arg) is not int else arg)
    return list(source[slice(*params)])
