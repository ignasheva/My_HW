from typing import Callable


def func(a, b):
    return (a ** b) ** 2


def cache(func: Callable) -> Callable:
    cache = dict()

    def cache_f(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return cache_f


cache_func = cache(func)
