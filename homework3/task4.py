def is_armstrong(number: int) -> bool:
    length = len(str(number))
    numbers = map(int, str(number))
    return sum(map(lambda x: x ** length, numbers)) == int(number)
