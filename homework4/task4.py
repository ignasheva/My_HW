import doctest
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']

    >>> fizzbuzz(15)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']
    """
    f = lambda num: "fizz" * (num % 3 == 0) + "buzz" * (num % 5 == 0) or str(num)
    return list(f(num) for num in range(1, n + 1))


if __name__ == "__main__":
    doctest.testmod()
