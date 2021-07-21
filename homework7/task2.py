def find_the_end_value_of_a_string(string: str) -> list[str]:
    value = []
    for s in range(len(string)):
        value.pop() if string[s] == "#" and value else value.append(string[s])
    return value


def backspace_compare(first: str, second: str) -> bool:
    s = find_the_end_value_of_a_string(first)
    t = find_the_end_value_of_a_string(second)
    return s == t
