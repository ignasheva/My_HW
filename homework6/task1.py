import functools
from typing import Callable


def instances_counter(cls) -> Callable:
    @functools.wraps(cls)
    def wrapper(*args, **kwargs) -> Callable:
        instance = cls(*args, **kwargs)
        wrapper.instances.append(instance)
        return instance

    wrapper.instances = []

    def get_created_instances(self=None) -> int:
        return len(wrapper.instances)

    setattr(cls, get_created_instances.__name__, get_created_instances)
    wrapper.get_created_instances = get_created_instances

    def reset_instances_counter(self=None) -> int:
        count = len(wrapper.instances)
        wrapper.instances = []
        return count

    setattr(cls, reset_instances_counter.__name__, reset_instances_counter)
    wrapper.reset_instances_counter = reset_instances_counter
    return wrapper


@instances_counter
class User:
    pass


if __name__ == "__main__":

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
