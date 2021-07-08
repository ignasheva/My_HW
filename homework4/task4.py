import doctest
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']

    >>> fizzbuzz(15)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']
    """
    return [
        ("fizz" if not i % 3 else "") + ("buzz" if not i % 5 else "") or str(i)
        for i in range(1, n + 1)
    ]


if __name__ == "__main__":
    doctest.testmod()