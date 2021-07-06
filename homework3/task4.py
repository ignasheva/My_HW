def is_armstrong(number: int) -> bool:
    list_of_numbers = list(map(int, str(number)))
    sum_of_numbers = list(map(lambda x: x ** len(str(number)), list_of_numbers))
    result = True if (sum(sum_of_numbers) == int(number)) else False
    return result