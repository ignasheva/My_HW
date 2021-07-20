from typing import Callable


def cache(times: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        cache = dict()

        def cache_f(*args: int) -> Callable:
            if args in cache:
                cached = cache[args]
                if cached["times"] > 1:
                    cache[args]["times"] -= 1
                    return cached["result"]
                else:
                    return cache.pop(args)["result"]
            result = func(*args)
            cache[args] = {"result": result, "times": times}
            return result

        return cache_f

    return decorator
